# Testing Instructions

## Table of Contents

- [Navigation](#navigation)

- [CRUD](#crud)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)

- [Sign Up](#sign-up)

- [Login](#login)

- [Logout](#logout)

- [Commenting](#commenting)

- [Liking](#liking)

- [Social Links](#social-links)


## Navigation

All navigation links, including the home icon, can be found in the navbar or on small to medium screens in the burger drop-down menu.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Home Link Icon** | While not on the homepage, click the icon. | User is redirected back to homepage. |
| **Go back button** | While on any page, click the back button. | The user is redirected one page back. |
| **"Contact" Link** | click "Contact". | User is redirected to the Contact page. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to the Login form. |
| **"Sign Up" Link** | While not authenticated, click "Sign Up". | User is directed to the Sign Up form. |
| **"Horses" Link** | While authenticated, click "Horses". | Renders list view of Horses posts. |
| **"Details" Link** | While authenticated, click on any post. | Renders detail view of Horses' posts. |
| **"Like" Link** | While authenticated, click on the heart. | Heart changes color to green. |
| **"unlike" Link** | While authenticated, click on the heart. | Heart changes color to grey. |
| **"Social Links" Link** | click "Social Links". | Opens new page in Browser and redirects to social media. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to a page with a SignOut button. |

## CRUD

The full CRUD functionality is only available to logged-in users.

### Create

Write and submit a new comment via the comment submit form on the details page (logged-in users only)

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Email field** | Click on the Email field and insert your email address. | Email displays. |
| **Content field** | Select the field and start typing. | written text displays. |
| **Submit** | After completing the comment form, click the submit button. |  User is re-directed to the details page. The alert message informs the user that the comment awaits approval. |
| **Incomplete form** | clicking on the submit button without filling email or Body field | message is displayed to make sure the field will be filled |
| **View Comment** | After submitting a comment, wait for admin approval | Once admin has approved submission, the comment can now be read below Information |


### Read

Read Posts and comments (logged-in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **post detail link** | On the horse's page, click on any post. | New view opens displaying detail view, title, author Race, birth year, brand, blog image, food plan, likes, and comments. |


### Update

Option to edit existing comments via post detail view (logged-in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On the post detail page, click the edit button below your comment. | detail view only shows the edit button of the user's own comments to ensure users can only update their own comments. |
| **Edit-Btn** | From the post detail view, click the edit button below a comment. The button is only visible after login. | Renders comment edit form with email and content field pre-populated by original post. |
| **Cancel** | Below the edit form, click "Cancel". | User is redirected to the details page with no action taken. |
| **Submit** | Alter form input according to desired update. Click the edit button below the form. | User is re-directed to the details page with the newly edited comment showing. |


### Delete

Option to delete existing comments via post detail view (logged-in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On the homepage, click the delete button below your comment. | detail view only shows the delete button of the user's own comments to ensure users can only delete their own comments. |
| **Confirm Delete** | On the delete page, click "Delete". | User is re-directed to the details page, selected comment has been deleted. |
| **Cancel** | On the delete page, click "Cancel". | User is re-directed to details page with no delete action taken. |


## Sign Up

Account creation for unauthenticated users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Sign Up form** | Go to Sign Up page via nav link | Renders form input fields Username, Email (optional), Password, Password (confirm). |
| **Submit** | Fill in form fields accordingly. Click "Sign Up". | Self-closing message informs the user of successful account creation, including username. The user is re-directed to the homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign Up". | User remains on the Sign-Up form view and is prompted to complete missing fields. |

## Login

Signing into an existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Login form** | Go to the Login page via nav link | Renders form input fields Username, Password, Remember me (checkbox). |
| **Submit** | Fill in form fields accordingly. Click "Sign In". | Self-closing message informs the user of a successful login, including username. The user is re-directed to the homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign In". | User remains on the Sign-Up form view and is prompted to complete missing fields. |
| **Remember me** | When signing in, tick "Remember me". Log out and sign in again. | Login form is pre-populated with username and hidden password. |

## Logout

Allows users to sign out of existing accounts (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout form** | When authenticated, go to the Logout page via the nav link | User is directed to the Logout page, asking the user to confirm the action. |
| **Sign Out** | On the Logout page, click "Sign Out". | Self-closing message informs the user of successful logout. The user is re-directed to the homepage and navigation shows links for unauthenticated users. |


## Liking

Option to like/unlike posts (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Like** | In the post detail view, click the like button (heart icon) below the body of a post that isn't already liked. | Icon color changes from green border to green. Like count is incremented by 1. |
| **Unlike** | In the post detail view, click the like button (heart icon) below the body of a post that is already liked. | Icon color changes from green to green border. Like count is decremented by 1. |

## Social Links

Links to social media sites are located in the footer (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Link Icons in Footer** | Click on any of the social media icons | New tab opens with respective social media site |

## Contact Form

Contact form located in Navbar (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Contact Form** | Go to Contact page via nav link | Renders form input fields Name, Email, Message. |
| **Submit** | Fill in form fields accordingly. Click "Submit". | Self-closing message informs the user of successful contact form submission. |
| **Incomplete form** | Failing to fill out all form fields, click "Submit". | User remains on Contact form view and is prompted to complete missing fields. |