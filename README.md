# Code Institute Project 4 HTML, CSS, JavaScript, Python, Django

# Fürstenhof Equestrian 
### Fürstenhof Equestrian is a website for managing horses, using Django. Posts can be created by admins to present the individual horses. As a visitor to the site, you have access to the landing page, where information about the Fürstenhof and the training can be found. You have the option of sending an email to the Fürstenhof on the contact page. The email form is controlled via EmailJS. The email goes directly to the site owner's private email address. An automatic response will be sent to the user. Much like a regular blog site, a registered user has the opportunity to access the Horses Page. On this page, the horses are presented in post form. You can open the individual posts to access details. In the details, you will find 2 images, breed, age, focus, and the current feeding plan. The logged-in user has the opportunity to give and take back likes as well as create, edit, and delete comments.
![View on multiple screens](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698157591/readme/f5hnfiwqk6wwalzhsiun.png)

[The live website can be seen on HEROKU](https://mrhaju-pp4-horse-planer-9051a41351ce.herokuapp.com/post-detail/quarterback/)

[View Repository on Github Pages](https://github.com/MrHaJu/Code-Institute-Projekt-4-Django-horseplaner)
## Table of Contents

- [UI/UX](#uiux)
    - [Agile](#agile)
    - [Wireframes](#wireframes)
    - [Site Goals](#site-goals)
    - [5 Planes of UX](#5-planes-of-ux)
    - [Visual Design Choices](#visual-design-choices)

- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#possible-future-features)
   
- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [Custom Model](#custom-model)
    - [CRUD](#crud)

- [Technologies Used](#technologies-used)
    - [Work Environments and Hosting](#work-environments-and-hosting)
    - [Python Libraries](#python-libraries)
    - [Django Libraries](#django-libraries)
    - [External Libraries](#external-libraries-and-applications)
    - [Database](#database) 

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    - [Media and Styling](#media-and-styling)

## UI/UX

The general layout of the site is based on warm summery colors.

The general layout, navigation, and functionality are plain and intuitive.

Features and interactivity are kept to a minimum, to not overwhelm the user with too many options.   

### Agile

This project was designed and built using the agile approach. From the initial planning through to final development. To help visualize the process I created a [GitHub project](https://github.com/MrHaJu/Code-Institute-Projekt-4-Django-horseplaner) and utilized the provided Kanban board method to make sure I implemented every necessary feature.

To view all user stories including their required acceptance criteria and tasks, refer to the project linked below.


[View Agile on Github Pages](https://github.com/users/MrHaJu/projects/4/views/1)


### Wireframes

The initial [wireframes in Figma](https://www.figma.com/file/JgWIf92LDhSdwyxbOAf9Ar/F%C3%BCrstenhof-Equestrian?type=design&node-id=0%3A1&mode=design&t=2l7GDAVULiM33wx4-1) are an overly simplified version of the finished product and merely served the purpose of listing most of the site's essential features.

Not all features and functions are covered in this early state. For a full list of existing features see [Features](#features)

<details>
    <summary>
        Wireframe images
    </summary>
    <img src="https://res.cloudinary.com/db6t1xmmn/image/upload/v1698405799/readme/wireframes/qix5ab6r6yha2nzjwbcr.png" alt="-Index">
    <img src="https://res.cloudinary.com/db6t1xmmn/image/upload/v1698405800/readme/wireframes/huefzlpyrdttzwhp84ww.png" alt="Horses">
    <img src="https://res.cloudinary.com/db6t1xmmn/image/upload/v1698405799/readme/wireframes/x2bwuiwaoaevthwwiya8.png" alt="Details 1">
    <img src="https://res.cloudinary.com/db6t1xmmn/image/upload/v1698405799/readme/wireframes/jpercl8kha1xmg9h5ixy.png" alt="Details 2">
    <img src="https://res.cloudinary.com/db6t1xmmn/image/upload/v1698405799/readme/wireframes/qqjma4txgok4dpsumzns.png" alt="Contact">
</details>


### Site Goals

The goal of this website is to provide the user with an overview of the horses, their background, and their feeding schedule. User actions are deliberately limited.

For example, only the admin can create a post. Comments can be created, updated, and deleted by logged-in users and must be approved by the admin.
Likes can be given and withdrawn by logged-in users.

In summary, the website is intended to present information about the horses and to provide information in the form of comments.

### 5 Planes of UX

#### Strategy

Addresses user needs and product goals.
This project wasn't about ignoring the needs that the rest of the web is trying to meet - it's not about buying and selling, social media, discussions, and not an excessive visual feed.
The goal is to give a clear overview and provide important information.

#### Scope

Covers which functions and features are within the scope of the project.
Minimal functionality was the key to this project. This means that most of the included features are a basic requirement. Features such as user registration and login as well as basic CRUD functionality for authenticated users needed to be implemented. For a detailed explanation of all existing features, see [Existing Features](#existing-features).
The prospects discussed in [Future Features](#possible-future-features) were deemed unnecessary at this time, although they are still within the possible scope of this project.

#### Structure

Defines how users can navigate the website and use all existing functions.
The structure of the website is modeled on a simple blog site. Most simple online blog sites follow a similar template to this website.
The structure allows users to visit the website, view posts, open and view details, comment, and like. This is only possible through user authentication, which requires an account to be created.

#### Skeleton

Inserts features defined in the structure into navigation elements.
You can find an initial overview of the project framework under [Wireframes](#wireframes).
To ensure intuitive navigation of the site, both the navigation bar and the main content follow a standard layout pattern that should be familiar to most users.
The navigation bar provides links to the site's main features and functionality, which vary depending on whether a user is authenticated or not. On small to medium screen sizes, the dropdown burger menu replaces the full navigation bar. A home button for the second option is present as a small logo opposite all other navigation links. According to research, this is also common practice.
The main content is presented in a list view, pointing to the details and other features of each post.
Buttons and links are named accordingly. A footer with social media links completes the “framing” effect of the website.

#### Surface

Covers visual design and how to convey desired emotions and achieve desired effects.
For more details about surface layer planning, see [Visual Design Choices](#visual-design-choices).

### Visual Design Choices

**Colour Scheme:**

### #fff8bd

This soft, warm shade of beige represents the welcoming and serene atmosphere of Fürstenhof Equestrian. It evokes a sense of tranquility and comfort.

 ### #FFE500

The warm yellow signifies the radiance of the sun, reflecting the energy and vibrancy of the equestrian world. It symbolizes the passion and enthusiasm that both horses and riders bring to Fürstenhof.

 ### #4a4a4f

This neutral gray color provides a balanced backdrop for your content. It ensures readability and complements the other colors, giving a professional and polished look to your text.

 ### #1cc54f

The light green tone represents the lush pastures and vibrant outdoor spaces where horses roam freely. It symbolizes growth, nature, and the healthy environment at Fürstenhof.

 ### #158b39

The darker green complements the light green and represents the deep, rich heritage of equestrian traditions. It embodies stability and knowledge, reflecting the expertise of your trainers.

 ### #23bbbb

This shade of turquoise adds a touch of modernity and excitement to your website. It draws attention to links and interactive elements, inviting visitors to explore further.

 ### #1A1A1A

The very dark color is used for text and elements that require strong contrast. It provides readability and sharpness.

 ### #FFFFFF

The very light color represents purity and clarity. It's used to enhance the spaciousness and openness of your website's design, making it feel airy and welcoming.

----

Overall, this color palette reflects the holistic approach and expertise of Fürstenhof Equestrian. It combines the warmth and passion of equestrian activities with a professional and inviting design, inviting visitors to embark on a journey into the world of horses and riding.

![Primary colour](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698157413/readme/gbzjdo15gamvscd5vhpb.png)

To set a background for the navbar and footer, a background gradient using CSS was built from the two yellow tones.
The call-to-action buttons have a light green tone as the default color and a dark green tone when you hover over them

**Fonts:**

As in my previous projects, I used the Google font Josefin sans in font-weight 300

**Images and Icons:**

All pictures and videos were created by ourselves. For social media links, I used Font Awesome icons

## Features

### Existing Features

#### Navigation

- Navbar with icon and nav links
- Different links visible for authenticated and unauthenticated users
- Active link rendered with a green line underneath
- Collapsible burger menu with drop-down on small to medium screens
- go back button to bring always one page back
- logged user will be displayed in the center of the navbar if log in
- Alerts display also in the navbar center

![navbar](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395073/readme/dqpmqzmhdkpl6fwdj4td.png)

![navbar logged in](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395073/readme/cwm3cxhv5dznvkkps4lv.png)

![navbar alert](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395522/readme/eagu94oktttppq920iw9.png)

![burger menu](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395073/readme/wl2xgl7hspcf5vljmotw.png)

![burger menu open](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395073/readme/tvbih62tukg38s6sdw7l.png)

#### Site introduction

- Introductory paragraph at the top of the home page
- Explain to the user what the site is about
- Links "Sign Up" and "Login" inside paragraph are clickable

![site intro](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698218886/readme/rwfqhhxrrlcyljkhefvv.png)

#### Home page
![Home Page](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220144/readme/seumxzyvsto1x68e6fvb.png)
![site intro](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220080/readme/apwvjp2iybdvle1nixap.png)
![Trainer](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220081/readme/ai4i8wnxjxrglkwl3ljm.png)
![ridetrack](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220080/readme/ngu1qpvthzkb22pwfyca.png)
![Summer pasture](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220080/readme/gyod4kdieuvpgme9sajb.png)
![Winter paddock](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220080/readme/sqofaqwlkjoc8zhrxku4.png)
![stable](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220080/readme/oqeca8b9rdenysx8eayc.png)

#### Contact Page

![Contact Form](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220144/readme/awcbcdesfphjaltlc2hu.png)

#### Register Page
- Allows the user to create an account
- Fields include Username, Email (optional), Password and Password confirmation

![Signup](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220143/readme/q2xwa8jgfrhns9rnymdg.png)
#### Login Page

- Login form asking for username and password of signed-up user
- Includes "Remember me" checkbox option

![Login](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220143/readme/rsdslraqt7jvklvg5yd6.png)
![]()
#### Logout Page

- Separate page prompts the user to confirm action to sign out.

![Logout](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220143/readme/stmmmueodz4xsipe2cth.png)
![]()

#### Footer

- Footer with social media icon links
- Links open in separate tabs

![footer](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698233156/readme/ncpskgiwtfn3l6tywwgn.png)

#### Horses Page

- Horses Page with filter function.
- Filter by race or brand
![Horse Posts](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395073/readme/j8saykh1n9ntgu2qctlq.png)

#### filtered posts page

![Filtered horse Posts](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395073/readme/wyggfdgalyjquvftrdxs.png)


#### Details Page

on the details page, you can see an Image of the horse, its name, and when the post was made as well as who posted
beneath you can see the Breed/Race, birth year of the horse, and if it's a Dressage, Jumping, cutting, pleasure, or trail horse.
The last is a blog image


![Header](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220101/readme/lcvl44qkjr6nksmacidf.png)

In the admin panel, you have a text input field which in my case is used as a food plan

![Content field / Food Plan](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220137/readme/h3j5hcjqjoouwkdmfsrn.png)

you can like and unlike via clicking on the little heart and see how many info comments are given

![Likes and comments](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698230392/readme/mcdhqboupfzk95junmkn.png)

As a user, you can write a comment. You have to put your email and comment in the form fields

![Write comment field](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220143/readme/h13oirxovcz4rht8dpzl.png)

As a user, you update or delete your own comment

![Comments as User](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220149/readme/vwcqad7ymgyhubbnljia.png)

As an admin, you are able to update and delete every given comment

![Comments as Admin](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698220142/readme/dpmjzzrtngtoc9w7cuz6.png)


#### edit comment Page

If you click on edit comment, you will be redirected to the edit comment page where you can edit your comment. E-mail and Body fields are pre-filled with your data

![edit comment](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698230537/readme/othnoyr2xbyrbzgxnmmr.png)

#### delete comment Page

If you click on delete comment, you will be redirected to the delete comment page where you can delete your comment 

![delete comment](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698230537/readme/uase0xe1icqbuum18fw4.png)

#### Admin Panel

![Site administration](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698232656/readme/pjcnxngflm51ul6tuopq.png)

as an admin, you are able to create a new post

![add post](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698232656/readme/xrnvjnph6guw01rgu75t.png)

change or delete posts

![select post to change](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698232656/readme/ii0s0eby93bwshngdlgf.png)



![change post](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698232656/readme/s0pbrtqiixuad9xzwj0h.png)

you can select comments to approve or delete them

![select comment](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698232656/readme/xncwxjbjae9bnqbfsjoo.png)

you can change comments

![change comment](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698232655/readme/wbfityb0omdrdzssy4xa.png)


### Possible Future Features

**post function for user**

- add posts as a user

- add a user-specific training plan and video link to a camera in the horse box. So that the User/Horse owner can see only on his horse's detail page the training plan and a live feed of his horse.

**user profile edit**

after registration, the user can click on the name in the navbar to get to the user profile page and update the profile

## Database Design

### Database Model

The database model diagram was designed using [Canva](https://www.canva.com/).
The first draft of the entity relationship diagram does not include all models used in the final database.

![ERD](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698245039/readme/ilwyhyhu5bxkljqmsvnd.png)

### Custom Model

I integrated 5 custom models.

![Race](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698233860/readme/z1rpl0zizzoutkhrcotw.png)
![Birthyear](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698233860/readme/fnyzxb0lpvft5nputiks.png)
![Brand](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698233859/readme/c5fmubfr9us7dprdcccj.png)
![Blog image](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698233859/readme/wmrwq54xf6fdlamugusx.png)
![filter function](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395764/readme/fzorxyyj6ipwjjyqrh3g.png)

As required by the assessment criteria for this project, one custom model (the ``race``, ``birthyear``, ``brand``, ``blog image`` and ``filter function`` models) was added which was not covered by Code Institute's tutorial.

### CRUD

The CRUD principle was the main part of the design process for this project. For a detailed description of all CRUD features see [Features](#features)

**Create:**
An authenticated user can create and save a comment.

**Read:**
A user can read their own and other users' comments.

**Update:**
An authenticated user can edit and update their own saved comments.

**Delete:**
An authenticated user can delete their own saved comments.

## Technologies Used

### Work Environments and Hosting

- [Figma](https://www.figma.com/) (Wireframes)
- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [Cloudinary](https://cloudinary.com/) (Serving static media files)

### Python Libraries

- [Gunicorn](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/gunicorn/) (Python HTTP server for WSGI applications)
- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [Pillow](https://pypi.org/project/Pillow/) (Pillow Python Imaging Library (Fork) )

### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behavior of Django forms)

### Database

- [ElephantSQL](https://www.elephantsql.com/) (PostgreSQL database hosting)


## Testing

### Test Guide

For extensive instructions on how to manually test this site and its user stories, please refer to these [testing instructions](testing.md)

### Validator Testing

#### HTML [W3C validator](https://validator.w3.org/)

As this is a Django project, the HTML couldn't be tested via the site's URL, due to Django tags and Jinja templating language in HTML files. Instead, the source code of each page was pasted into the validator directly.

**Home page**

No errors or warnings to show.

**Horses page**

No errors or warnings to show.

**filtered posts page**

No errors or warnings to show.

**Contact page**

No errors or warnings to show.

**post_details page**

2 errors 1warning


- trailing slash ``<hr />``.
- image must have an alt attribute
- image must have an alt attribute

*Fix:*

- Remove trailing slash from ``<hr />``.
- add an alt attribute to the image
- add an alt attribute to the image


**edit comment page**

No errors or warnings to show.


**Delete comment page**

If click on cancel, error 404 appears

*Fix*

change {% url 'post_detail' comment.post.id %} to {% url 'post_detail' comment.post.slug %}

**Sign Up page**

No errors or warnings to show.

**Login page**

No errors or warnings to show.

**Sign Out page**

No errors or warnings to show.

#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)

No error was found.
14 Warnings about box-shadow and gradients

![jigsaw result](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698239290/readme/testing/okeewghykxmvsnq4pugt.png)

#### JavaScript [JSHint](https://jshint.com/) 

- Contact form
3 missing semicolon
1 trailing comma

![jshint result](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698239477/readme/testing/eygdwzm1tmoq4a7efoir.png)

*Fix:*

removed comma and added semicolon

![jshint result](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698239476/readme/testing/k5jmgh70eagxpwocc5ut.png)

- go back button

![jshint result](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698395988/readme/h11sx3fqasp1245pdkqu.png)

#### Python [CI Python Linter](https://pep8ci.herokuapp.com/)

Only files with custom-written Python code have been verified with the above validator.
All files yielded the same result. See the image of test results for models.py as an example output.

![python linter result](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698245884/readme/testing/asywky0lrbqsdvumx8at.png)

**admin.py**

All clear, no errors found

**forms.py**

All clear, no errors found

**models.py**

All clear, no errors found
Lines too long

**fuerstenhof/urls.py**

All clear, no errors found
Line too long

**views.py**

All clear, no errors found

**settings.py**

Lines too long
All clear, no errors found

**horse_planer/urls.py**

All clear, no errors found

**birthyear.py**

All clear, no errors found

**brand.py**

All clear, no errors found

**race.py**

All clear, no errors found

#### Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)

**Desktop results**

![lighthouse results desktop](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698240577/readme/testing/edaa2bafnddcxbhwt0tp.png)

**Mobile results**

![lighthouse results mobile](https://res.cloudinary.com/db6t1xmmn/image/upload/v1698240961/readme/testing/nsnokjulogvdx7izwc7p.png)


### Browser Testing

**Layout:** 
Testing layout and appearance of the site for consistency throughout browsers.

**Functionality:** 
- Testing complete functionality of the site. This includes:
    - Sign Up
    - Login
    - Logout
    - External social media links
    - Navigation
    - Like/unlike entries
    - Comment/extend entries
    - Delete and edit entries
    - Admin user functions
    
- Ensuring all links, navigation, and form submit functions as expected throughout browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
| Firefox     | ✔          | ✔             |
| IE          |deprecated by Microsoft, not tested|


### Fixed bugs

### Unfixed bugs

There are no known bugs

## Deployment

This project was deployed using [Heroku](https://heroku.com/), [Cloudinary](https://cloudinary.com/) and [ElephantSQL](https://www.elephantsql.com/). For a full list of libraries refer to [Technologies Used](#technologies-used).

#### Installing libraries

The following steps outline all libraries needed for successful deployment on Heroku. All neccessary-requirements and settings updates will not be discussed in this section as they are assumed as logical follow-up steps to installments. For a full explanation of how to install these libraries, refer to the links provided in [Technologies Used](#technologies-used).

- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Cloudinary** (host static files and images): ``pip3 install dj3-Cloudinary-storage``
- Install **pillow** (prevent issues with Heroku not rendering custom stylesheet): ``pip3 install pillow``

#### Creating the Heroku App

- Log into Heroku and go to the Dashboard
- Click **New** and select **Create new app** from the drop-down
- Name the app appropriately and choose the relevant region, then click **Create App**

#### Create a PostgreSQL database using ElephantSQL

This is necessary to create a database that can be accessed by Heroku. The database provided by Django can not be accessed by the deployed Heroku app.

- Log into ElephantSQL and go to Dashboard
- Click **Create New Instance**
- Set up a plan by providing a Name (project name) and select a Plan (for this project the free plan "Tiny Turtle" was chosen). Tags are optional.
- Click **Select Region** and choose appropriate Datacenter
- Click **Review**, check all details and click **Create Instance**
- Return to Dashboard on click on the name of the newly created instance
- Copy the database URL from the details section

#### Hiding sensitive information

- Create ``env.py`` file and ensure it is included in the ``.gitignore`` file
- Add ``import os`` to env.py file and set environment variable **DATABASE_URL** to the URL copied from ElephantSQL (``os.environ["DATABASE_URL"]="<copiedURL>"``)
- Below, set **SECRET_KEY** variable (``os.environ["SECRET_KEY"]="mysecretkey"``, but be more inventive about the key string!)


#### Update Settings

- Add the following code at the top of ``settings.py`` to connect the Django project to env.py:
    ````
      import os
      import dj_database_url
      if os.path.isfile('env.py'):
          import env
    ````
- Remove the insecure secret key provided by Django in settings.py and refer to a variable in env.py instead (``SECRET_KEY = os.environ.get('SECRET_KEY')``)

- To connect to the new database, replace the provided **DATABASE** variable with 
    ````
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ````
- Save and migrate all changes made

#### Connecting Heroku to Database

- In the Heroku dashboard, go to **Settings** tab
- Add new config vars **CLOUDINARY_URL** (value is CLOUDINARY_URL), **DATABASE_URL** (value is database URL), **HEROKU_HOSTNAME** (value is Heroku app), **SECRET_KEY** (value is secret key string) and **PORT** (value "8000")

#### Connect to Cloudinary

- In the Cloudinary dashboard, copy **API Environment variable**
- In ``env.py`` file, add new variable ``os.environ["CLOUDINARY_URL"] = "<copied_variable"`` and remove ``CLOUDINARY_URL=`` from the variable string
- Add same variable value as new Heroku config var named **CLOUDINARY_URL**
- In ``settings.py``, in ``INSTALLED_APPS`` list, above ``django.contrib.staticfiles`` add ``cloudinary_storage``, below add ``cloudinary``
- To define Cloudinary as static file storage add the following to settings.py
    ````
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ````

#### Allow Heroku as host

- In ``settings.py`` add
    ````
    ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
    ````

## Development

The following options are available to work with this code or run in a local environment.

### Fork

Any changes made to a forked repository do not affect the original repository.

- Log into GitHub and click on the repository to download ([Code-Institute-Projekt-4-Django-horseplaner
](https://github.com/MrHaJu/Code-Institute-Projekt-4-Django-horseplaner))
- Click the **Fork** button in the top right-hand corner
- Select a different owner if necessary
- Click **Create Fork**
- The repo is now in your chosen account and can be cloned or changed

### Clone

Changes made to a cloned repository will affect the original one.

- Navigate to the main page of the repository (this could be a forked instance)
- Click on the **Code** dropdown menu above the list of files
- Choose a method to copy the URL for the repository: either via **HTTPS**, by using an **SSH key**, or by using **GitHub CLI**
- In your work environment, open Git Bash and change the current directory to the target location for the cloned repository
- Type ``git clone`` followed by the copied URL and press enter **Enter**

### Download as ZIP

- Log into GitHub and click on the repository to download ([Code-Institute-Projekt-4-Django-horseplaner
](https://github.com/MrHaJu/Code-Institute-Projekt-4-Django-horseplaner))
- Select **Code** and click "Download Zip" file
- Once the download is completed, extract the ZIP file and use it in your local environment

## Source Credits

### References/Documentation/Tutorials

**General**:

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.
The skeleton of this project is based on the [Code Institute](https://codeinstitute.net/) tutorials ["I Think Therefore I Blog"](https://github.com/Code-Institute-Solutions/Django3blog).

For Edit and delete functions I used a youtube tutorial by [Django World](https://www.youtube.com/@DjangoWorld) as a reference
[Adding edit and delete button in blog detail page | Django | Python](https://www.youtube.com/watch?v=wFci3tnRNFw&t=426s&ab_channel=DjangoWorld)

**Main page pagination**

The code to add conditional pagination to the ``index`` template, including page navigation links was taken as Django and Bootstrap boilerplate from [Code Institute source code](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/06_creating_our_first_view/templates/index.html). Styling was customized. 

### Media and Styling

**Images:**

All Images are self-made

**Icons:**
Icons are taken from [Fontawesome](https://fontawesome.com/search)

**Fonts:**

Font taken from [Google Font](https://fonts.google.com/).

## Credits

### Code Used

* [Othman Adi (Coding with Adi) Java Script for contact form](https://gist.github.com/OthmanAdi)
* [EmailJS Java Script for sending Emails to my Googlemail](https://www.emailjs.com/)
* [Bootstrap CSS](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)
* [Example readme file by Kera Cudmore](https://github.com/kera-cudmore)

### Content

The content of the website was written by the owner (Andreas Huppertz)

### Acknowledgments

* [Othman Adi (Coding with Adi) Java Script for contact form](https://gist.github.com/OthmanAdi), for teaching me how to use my first Java Scripts and CSS.
* [Jubril Akolade](https://github.com/Jubrillionaire), my Code Institute Mentor.