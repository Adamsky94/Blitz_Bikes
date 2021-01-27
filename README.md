# Blitz Bikes 

Code Institute Diploma in Full-Stack Web Development Milestone 3 Project

##### <u>Project name:</u> Blitz Bikes | Bombardment of Biking Reviews

<img src="./static/images/jpg/readme_img/project_logo.jpg" />

### View the live project: https://blitz-bikes.herokuapp.com/

### <u>Scope of the project</u>

The "Blitz Bikes" website is a database based collective of community cycling reviews. Registered members can leave reviews on this site for the general public and other members to see, 
modify their published reviews or delete them. The reviews size are maximised in 550 characters. There is functionality to search amongst the stored reviews. Pages are generated from a 
Python app running from Heroku and the HTML code is rendered using the Jinja templating language. This page is created to demonstrate the CRUD functionality in a data-centric environment.

-----------------

### <u>Contents</u>

- [User Stories](#User-Stories)

- [Wireframing](#Wireframing)
- [Landing](#Landing)
  - [Page layout](#Page-layout)
  - [Navigation](#Navigation)
  - [Footer](#Footer)

- [Technologies Used](#Technologies-used)

- [Version Control](#Version-control)

- [Testing](#Testing)

  - [Bug fixes](#Bug-fixes)
  - [Lighthouse](#Lighthouse)

- [Deployment](#Deployment)

- [Cloning repository](#Cloning-repository)

- [Credits](#Credits)

-----------------

### <u>UX Design / Presentation</u>

#### User Stories

###### As a visitor I expect:

- To be able to enter the site past the landing page
- To be able to see all reviews posted containing all relevant information
- To be able to see non-broken layout on all resolutions
- To be able to view all pictures and an easy to use navigation with buttons and links functioning properly
- To be able to register to the site

###### As a registered user I expect in addition to the above:

- To be able to log in and out of my personal profile
- To be able to leave a review
- To be able to see the collection of reviews I left
- To be able to edit the reviews I left
- To be able to delete the reviews I left

###### As the administrator I expect in addition to the above:

- To be able to see all categories for the reviews
- To be able to create a category for the reviews
- To be able to modify a category for the reviews
- To be able to delete a category for the reviews
- To be able to modify/claim any user's review
- To be able to delete any user's review

-----------------

#### **Wireframing**

###### Landing layout

<img src="./static/images/wireframes/landing.png" />

> I imagined a full-size landing page wich would contain a video as a background, the name of the site and an Enter button. All visitors would see this first.

Edit: I have used both a background image and video blended as the background. I have disabled the video on small screen devices with a media query.

###### Reviews layout

<img src="./static/images/wireframes/reviews.png" />

> The reviews page would contain a navbar on top with a searchbox below it so users can search amongst all posted reviews. The main content would be the review cards in rows of 3
containing the bike's make and model, model year, the category of the type of the bike, the username of the reviewer and the review itself. The bottom of the page would hav the footer.

Edit: I have decided to leave just 2 cards in a row as it seems to be a better layout. Below medium screensizes the reviews would be go under after each other.

###### Login/Register/Logout  layout

<img src="./static/images/wireframes/login_register.png" />

> The main element here is a simple form which requires a username and a password to be entered. The logout option in the navigation would return the user to the login page with the form. 
The form check if an existing username is entered for registration it shows an error. It also shows an error if there is an invalid username & password combination on login.

###### Add/Edit Reviews layout

<img src="./static/images/wireframes/add_edit_review.png" />

> This would be the form where a registered user can enter the details of the bike they are about to review. They can chose the category, add the make and model, select manufacturing year, 
add a URL for an image (a default image would load if the field is left empty), type the 550 character review and on a final dropdown they can select wether they'd recommend the bike or not.

Edit: I couldn't figure how to upload and store an image in a MongoDB database so I implemeted this "enter image URL" design. The only downside to it if the user is entering an invalid or broken 
URL no image would be displaying. No failsafe implemented for this.

###### Edit Categories layout

<img src="./static/images/wireframes/categories.png" />

> This page would only show up when the Administrator is logged in. There would be all current categories listed here with the option to edit or delete each of them. There would be also the option to 
create new categories.

###### Navigation

<img src="./static/images/wireframes/navigation.png" />

> There is a uniform navigation bar for all types of users on all pages. It contains the page logo on the left and links on the right. The links would show up differently for the different type of users. For example a visitor will not see the "Add review" page before registrating and logging in. 
A registered user will not see the "Register" page logged in as it is irrelevant at this point and they will not be able to modify any other reviews than their own, nor review categories. The administrator would have acces to all of these. 
On small screen devices the navigation would collapse to a hamburger icon and would load in from the left of the screen upon clicking on it. Again, only the appropriate links for certain users.

###### Footer

> A uniform page footer would contain the brand and some more information on the left side and basic navigation links for all users for loggin in, registering and the reviews page. If a user clicks on these links while logged in it does not end their session. The very bottom of the footer contains basic copyright info and further links.

**Color scheme and typography**

> I have imported the 'Dosis' and 'Germania One' fonts from Google Fonts. 'Germania One' is used for the logo of the page. All other text through the pages are set for 'Dosis' as default. 'Georgia', 'Times New Roman', 'Times', 'serif' are used as fallback fonts. I used the Materialize CSS for the layout and colors. Chosen black for text and 
light and dark shades of red for the navbar, footer and the buttons. For the background image, user image, category image and background video I used the linear-gradient CSS property to create a uniform light-grey overlay and added opacity to the video. I intented to achieve a nice contrast between the red top and bottom and the lighter colors 
of the main page content.

-----------------

### Technologies Used

- HTML5
- CSS3
- JavaScript
- Python3
- Flask Microframework
- dnspython
- Flask-PyMongo
- pymongo
- Werkzeug
- Git Version Control 
- GitHub - to host the repository and the live site
- GitPod IDE - remote developer environment
- Balsamiq Wireframes - used in the design process for wireframing
- [Heroku](https://www.heroku.com/)
- [MongoDB](https://www.mongodb.com/)
- [JQuery](https://jquery.com/)
- [Materialize CSS](https://materializecss.com/)
- [FontAwesome](https://fontawesome.com/) - for the icons used
- [Favicon.io](https://favicon.io/) - for creating the favicon
- [Animate.css](https://animate.style/) - for animating headings
- [Typora](https://typora.io/) - The README.md file was partially edited in Typora

-----------------

### **Version Control**

I used Git for version control and uploading the project to GitHub.

My GitHub repository for this project: https://github.com/Adamsky94/Blitz_Bikes

### Testing write-up

HTML code validated on - https://validator.w3.org/

CSS code validated on - https://jigsaw.w3.org/css-validator/ 

<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
</a>

Responsivity for mobile devices tested on:

- http://www.responsinator.com/ and https://techsini.com/multi-mockup/
- Google Chrome Developer Tools
- Microsoft Edge
- Opera Browser
- Mozilla Firefox on Galaxy S9 setting
- The deployed site on Samsung Galaxy S7 and S8

Used online [autoprefixer](https://autoprefixer.github.io/) for maximum browser compatibility 

Used online [code formatter](https://webformatter.com/) to achieve optimal syntax 


##### Bug Fixes

- 

##### Lighthouse Speed Tool

<img src="./static/images/jpg/readme_img/lighthouse_seo.png" />

## Deployment

### Creating GitHub repository

First step in order to deploy the project is to set up a new repository. You can read on [how to do that](https://docs.github.com/en/github/getting-started-with-github/create-a-repo) if you don't already know it on the official GitHub Documentation.

### Deploying on Heroku

- Create a requirements.txt file in your editor using the following command in your CLI.
```
pip3 freeze --local > requirements.txt
```
- Create a Procfile (always with an uppercase P)  in your editor through the command line using this command. 
```
echo web: python app.py > Procfile
```
- Commit and Push to your repository.
- Create an account on [**Heroku**](https://www.heroku.com/home).
- Create a new app with **unique name**.
- Select your **nearest region**.
- Create a **new python project** within the project.
- Link that project through your **GitHub repository** in the **deployment** section. There are other ways than this to integrate GitHub. You can read more on this particular approach on 
the official Heroku documentation [here](https://devcenter.heroku.com/articles/github-integration#automatic-deploys).
- Navigate to Heroku Settings and set up the following in **Config Variables**
```
_IP = 0.0.0.0
MONGO_DBNAME = [Name of DB]
MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?r
PORT = 5000
SECRET_KEY = [Your Secret key]
```
- Go back to the **Deploy** section, select the **master branch** and deploy the project.

#### The live project page: https://blitz-bikes.herokuapp.com/

<img src="./static/images/jpg/readme_img/multimockup.png" />

------

### Cloning this repository

If you'd like to see and work on my code locally feel free to clone the repository. When you clone a repository, you copy the repository from GitHub to your local machine. 

1. On GitHub, navigate to the main page of the repository.

2. Above the list of files, click **Code**.

3. To clone the repository using HTTPS, under "Clone with HTTPS", click . To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click **Use SSH**, then click . To clone a repository using GitHub CLI, click **Use GitHub CLI**, then click .

4. Open Git Bash.

5. Change the current working directory to the location where you want the cloned directory.

6. Type `git clone`, and then paste the URL you copied earlier.

   ```shell
   $ git clone https://github.com/Adamsky94/Blitz_Bikes.git
   ```

7. Press **Enter** to create your local clone.

GitHub documentation on cloning repository includes other methods to using the console. You can read more [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

-----------------

### Credits

***Antonio Rodriguez*** - My mentor at Code Institute - Helping to set the database relations and in the python code

***Tim Nelson*** - Lecturer/Developer at Code Institute - For the creation of the code used in the Mini-project. The "Blitz Bikes" Project is based on that code.

***Matt Rudge*** - Lecturer/Developer at Code Institute -  https://github.com/Code-Institute-Org/gitpod-full-template - for template used with GitPod IDE for developing this project, and lecture on Email JS

***Ross Dallaire*** - https://codepen.io/rdallaire/pen/apoyx - for return-to-top arrow

***Mezo Istvan*** - https://medium.com/@mezoistvan/finally-a-css-only-solution-to-hover-on-touchscreens-c498af39c31c - for solution to the touchscreen :hover state of return-to-top arrow

***GerrardSlippedHahaha*** on ***Reddit*** - https://www.reddit.com/r/learnpython/comments/6xsg51/django_default_image_for_filefield/ - idea for how to have a default review image

***Erik Mclean*** on ***Pexels*** - https://www.pexels.com/photo/stop-sign-on-the-street-4061973/ - for categories background image

***Jan Kroon*** on ***Pexels*** - https://www.pexels.com/photo/grayscale-photo-of-road-1169116/ - for page background image

***Saravanan*** on ***codehim.com*** - https://www.codehim.com/date-time/jquery-datepicker-year-only/ - for CSS and JavaScript of Year only Date Picker

***TK*** on ***redstapler.co*** - https://redstapler.co/responsive-css-video-background/ - on how to do responsive CSS video background

***coverr.co*** - https://coverr.co/videos/spinning-bike-wheel-kwdjraJSwY - for the background video

***W3Schools*** - https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp - for code on creating custom scrollbar

***web.dev*** - https://web.dev/meta-description/?utm_source=lighthouse&utm_medium=devtools - on reccomendating how to achieve better SEO

***Font Awesome*** -  https://fontawesome.com/ - CDN for icons used in the project

***Google Fonts*** - https://fonts.google.com/ - CDN for fonts used in the project

***Animate.css*** -  https://animate.style/ - for animation on the landing page

***JQuery*** - https://jquery.com/

***Autoprefixer CSS online*** - https://autoprefixer.github.io/