import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# Routing for the index page
@app.route("/get_index")
def get_index():
    return render_template("index.html")

# Refactoring code after 2nd Mentor session with Antonio Rodrigez


@app.route("/get_reviews")
# Routing for the the main reviews page
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    for review in reviews:
        review["category_name"] = mongo.db.categories.find_one(
            {"_id": review["category_name"]})["category_name"]
        review["username"] = mongo.db.users.find_one(
            {"_id": review["username"]})["username"]
    return render_template("reviews.html", reviews=reviews)

# Refactoring code after 2nd Mentor session with Antonio Rodrigez


@app.route("/user_reviews")
# Routing for the user reviews page
def user_reviews():
    # finding the reviews in the db and listing them
    reviews = list(mongo.db.reviews.find())
    for review in reviews:
        review["category_name"] = mongo.db.categories.find_one(
            {"_id": review["category_name"]})["category_name"]
        review["username"] = mongo.db.users.find_one(
            {"_id": review["username"]})["username"]
    return render_template("user_reviews.html", reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
# Routing for the Add reviews page
def add_review():
    if request.method == "POST":
        category_id = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")})["_id"]
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        review = {
            "category_name": ObjectId(category_id),
            "bike_name": request.form.get("bike_name"),
            "model_year": request.form.get("model_year"),
            "image_url": request.form.get("image_url"),
            "bike_description": request.form.get("bike_description"),
            "recommend": request.form.get("recommend"),
            "username": ObjectId(user_id)
        }
        mongo.db.reviews.insert_one(review)
        flash("Thank you for your review")
        return redirect(url_for("user_reviews"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_review.html", categories=categories)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # Routing for the edit review page
    if request.method == "POST":
        category_id = mongo.db.categories.find_one(
            {"category_name": request.form.get("category_name")})["_id"]
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        submit = {
            "category_name": ObjectId(category_id),
            "bike_name": request.form.get("bike_name"),
            "model_year": request.form.get("model_year"),
            "image_url": request.form.get("image_url"),
            "bike_description": request.form.get("bike_description"),
            "recommend": request.form.get("recommend"),
            "username": ObjectId(user_id)
        }
        # Update the review and leave message on the screen
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("You have updated the review")
        return redirect(url_for("user_reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
# Routing for the delete review page
def delete_review(review_id):
    # Remove the review where the id's match and leave message on screen
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("user_reviews"))


@app.route("/search", methods=["GET", "POST"])
# Routing of the search functionality
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    for review in reviews:
        review["category_name"] = mongo.db.categories.find_one(
            {"_id": review["category_name"]})["category_name"]
        review["username"] = mongo.db.users.find_one(
            {"_id": review["username"]})["username"]
    if reviews == []:
        # If there are no results leave message on screen
        flash("No results? Impossible! Perhaps the archives are incomplete...")
    # Render the reviews which match search criteria
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
# Routing for Registration
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
# Routing for Login
def login():
    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
# Routing for LogOut
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
# Routing for the profile page
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/get_categories")
# Routing for Categories page
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
# Routing for Add category page form
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
# Routing for Edit category page form
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
# Routing for Deleting category
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")))
