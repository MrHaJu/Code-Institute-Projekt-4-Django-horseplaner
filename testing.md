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

All navigation links, including home icon, can be found in navbar or on small to medium screens in the burger drop-down menu.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Home Link Icon** | While not on homepage, click icon. | User is redirected back to homepage. |
| **Go back button** | while on any page, click back button. | user is redirected one page back. |
| **"Contact" Link** | click "Contact". | User is redirected to Contact page. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Sign Up" Link** | While not authenticated, click "Sign Up". | User is directed to Sign Up form. |
| **"Horses" Link** | While authenticated, click "Horses". | Renders list view of Horses posts. |
| **"Details" Link** | While authenticated, click on any post. | Renders detail view of Horses posts. |
| **"Like" Link** | While authenticated, click on the heart. | heart changes color to green. |
| **"unlike" Link** | While authenticated, click on the heart. | heart changes color to grey. |
| **"Social Links" Link** | click "Social Links". | opens new page in Browser and redirect to social media. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |

## CRUD

The full CRUD functionality is only available to logged in users.

### Create

Write and submit a new comment via comment submit form on details page (logged in users only)

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Email field** | Click on Email field and insert your email address. | Email displays. |
| **Content field** | Select field and start typing. | written text displays. |
| **Submit** | After completing comment form, click submit button. |  User is re-directed to details page. Alert message informs user that comment awaits approval. |
| **Incomplete form** | clicking on submit button without filling email or Body field | message is displayed to make sure the field will be filled |
| **View Comment** | After submitting comment, wait for admin approval | once admin has appproved submission, comment can now be read below Information |


### Read

Read Posts and comments (logged in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **post detail link** | On horses page, click on any post. | New view opens displaying detail view, title, author Race, birthyear, brand, blog image, Foodplan, likes and comments. |


### Update

Option to edit existing comments via post detail view (logged in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On post detail page, click edit button below your comment. | detail view does only show edit button of the users own comments to ensure users can only update their own comments. |
| **Edit-Btn** | From post detail view, click edit button below comment. Button is only visible after login. | Renders comment edit form with email and content field pre-populated by original post. |
| **Cancel** | Below edit form, click "Cancel". | User is redirected to details page with no action taken. |
| **Submit** | Alter form input according to desired update. Click edit button below form. | User is re-directed to details page with the newly edited comment showing. |


### Delete

Option to delete existing comments via post detail view (logged in users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **User match** | On homepage, click delete button below your comment. | detail view does only show delete button of the users own comments to ensure users can only delete their own comments. |
| **Confirm Delete** | On delete page, click "Delete". | User is re-directed to details page, selected comment has been deleted. |
| **Cancel** | On delete page, click "Cancel". | User is re-directed to details page with no delete action taken. |


## Sign Up

Account creation for unauthenticated users.

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Sign Up form** | Go to Sign Up page via nav link | Renders form input fields Username, Email (optional), Password, Password (confirm). |
| **Submit** | Fill in form fields accordingly. Click "Sign Up". | Self-closing message informs user of successfull account creation, including username. User is re-directed to homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign Up". | User remains on Sign Up form view and is prompted to complete missing fields. |

## Login

Signing into existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Login form** | Go to Login page via nav link | Renders form input fields Username, Password, Remember me (checkbox). |
| **Submit** | Fill in form fields accordingly. Click "Sign In". | Self-closing message informs user of successfull login, including username. User is re-directed to homepage and navigation shows links for authenticated users. |
| **Incomplete form** | Failing to fill out all form fields, click "Sign In". | User remains on Sign Up form view and is prompted to complete missing fields. |
| **Remember me** | When signing in, tick "Remember me". Logout and sign in again. | Login form is pre-populated with username and hidden password. |

## Logout

Allows user to sign out of existing account (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Logout form** | When authenticated, go to Logout page via nav link | User is directed to Logout page, asking user to confirm action. |
| **Sign Out** | On Logout page, click "Sign Out". | Self-closing message informs user of successfull logout. User is re-directed to homepage and navigation shows links for unauthenticated users. |


## Liking

Option to like/unlike posts (authenticated users only).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Like** | In post detail view, click like button (heart icon) below body of post that isn't already liked. | Icon color changes from green border to green. Like count is incremented by 1. |
| **Unlike** | In post detail view, click like button (heart icon) below body of post that is already liked. | Icon color changes from green to green border. Like count is decremented by 1. |

## Social Links

Links to social media sites located in footer (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Link Icons in Footer** | Click on any of the social media icons | New tab opens with respective social media site |

## Contact Form

Contact form located in Navbar (available to all users).

| Feature | Action                             | Expected Result                 |
| :-----: | :---------------------------------:| :------------------------------:|
| **Contact Form** | Go to Contact page via nav link | Renders form input fields Name, Email, Message. |
| **Submit** | Fill in form fields accordingly. Click "Submit". | Self-closing message informs user of successfull contact form submission. |
| **Incomplete form** | Failing to fill out all form fields, click "Submit". | User remains on Contact form view and is prompted to complete missing fields. |