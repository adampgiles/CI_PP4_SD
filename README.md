# supportDev (Membership creation platform, tailored to Developers)

**Developer: Adam Giles**

## Table of Content

- [Project Goals](#project-goals)
- [User Stories](#user-stories)
    - [Registration and User Accounts](#registration-and-user-accounts)
    - [Site Navigation and Views](#site-navigation-and-views)

## Project Goals
supportDev is a membership creation platform, tailored towards Developers. Developers create a Profile where they provide Supporters with access to exclusive content. This content could be; Developer Logs, Source Code, or links to products/apps. Developers set the access price for Supporters.

Supporters create an account to purchase access to Developer Profiles, as a way of supporting the Developer.

## User Stories
User stories have been separated into two groups; Developer and Supporter.

### Registration and User Accounts

- Developer
1. I want to be able to register for a Developer Profile. So that I can create a unique Profile for Supporters to purchase access to.
2. I want to be able to access my Profile.
3. I want to be able to delete my Profile.

- Supporter
4. I want to be able to register for an Account. So that I can purchase access to Developer Profiles.
5. I want to be able to authenticate my registration via email confirmation. So that I can confirm my Account registration was a success.
6. I want to be able to login to my Account. So that I can purchase and access Developer Profiles.
7. I want to be able to logout of my Account. So that I can protect my Account from unauthorised access.
8. I want to be able to have a unique Supporter Account. So that I can view my Account details and purchased Developer Profiles.

### Site Navigation and Views 

- Developer 
9. I want to be able to view my Profile from the perspective of a Developer and a Supporter. So that I can edit my Profile, and also check that the Supporter view meets my needs.
10. I want to be able to easily create and edit my Profile content. So that I can provide content to my Subscribers.
11. I want to be able to amend my Profile details. So that I can ensure my details are correct and up to date.

- Supporter
12. I want to be able to view a list of Developer Profiles. So that I can choose which Profiles I would like to purchase access to.
13. I want to be able to view details of a Developer's Profile content. So that I can decide if the content is of interest to me.
14. I want to be able to amend my Account details. So that I can ensure my details are correct and up to date.
15. I want to be able to sort Developer Profiles by multiple criteria. So that I can quickly identify Developer profiles by price, name or post count.
16. I want to be able to view a list of Developer Profiles I have purchased access to. So that I can quickly navigate to a Developer's Profile.

### Structure

The website structure consists of the main "Base" page, with the following sections being added to this page dependant on the URL; Index Page, Explore Developers Page, Login Page, Register Page, Developer Profile/My Developer Profile Page, Create Developer Profile Page, Edit Developer Profile Page, Add a New Post Page, Edit Post Page, My Account Page, Shopping Cart Page, Checkout Page, Checkout Success Page, Contact Us Page, 404 Error Page and 500 Error Page.

The pages are detailed below;

<details><summary>Base Page</summary>
<img src="">
</details>
- This page contains a header; consisting of Site Logo and Navigation Bar (Links change if the user is logged in).

<details><summary>Index Page</summary>
<img src="">
</details>
- This page contains a Hero Section with sub-sections for "Support" and "Dev", each with text and a link. If the current user is not authenticated, the links navigate to the login page. If the user is authenticated, the "Support" section link, navigates to the "Explore Developers" page. The "Dev" section link navigates to the "Create Developer Profile" page, if the user has not already created a Profile. If they have created a Developer Profile, the link navigates to their Developer Profile page. 

<details><summary>Explore Developers Page</summary>
<img src="">
</details>
- This page contains a search bar, sort by filter,and a block for each Developer's Profile. Each block containes the Developer's Profile Image, Profile Name, Profile Description, Profile Price, Purchase Count and a link to the Developer's Full Profile.

<details><summary>Login Page</summary>
<img src="">
</details>
- This page contains a form for the user to complete that will log them into the site.

<details><summary>Register Page</summary>
<img src="">
</details>
- This page contains a form for the user to complete that will create an account on the site.

<details><summary>Developer Profile/My Developer Profile Page</summary>
<img src="">
</details>
- This page contains the selected Developer's Full Profile and Posts, each post block contains the Post Title, Post Content and Post Image. If the current user is viewing their own Developer Profile, links are available to edit the profile, add a new post and edit a post.

<details><summary>Create Developer Profile Page</summary>
<img src="">
</details>
- This page contains a form for the user to complete that will create a Developer Profile on the site.

<details><summary>Edit Developer Profile</summary>
<img src="">
</details>
- This page contains a form for the user to complete that will update their Developer Profile on the site.

<details><summary>Add a New Post Page</summary>
<img src="">
</details>
- This page contains a form for the user to complete that will create new post on their Developer Profile on the site.

<details><summary>Edit Post Page</summary>
<img src="">
</details>
- This page contains a form for the user to complete that will update a post on their Developer Profile on the site.

<details><summary>My Account Page</summary>
<img src="">
</details>
- This page contains the users details: Username, Email address and a link to change password. The page also contains a section displaying all the Developer Profiles the user has purchased access to.

<details><summary>Shopping Cart Page</summary>
<img src="">
</details>
- This page contains a list of items the user had added to their Cart, with the totals of each item and Cart Total. The user can then click a link to Checkout.

<details><summary>Checkout Page</summary>
<img src="">
</details>
- This page contains the Cart's contents along with a input for the user's card details. The user can then click a link to Complete the Purchase.

<details><summary>Checkout Success Page</summary>
<img src="">
</details>
- This page contains text to inform the user that the purchase was made.

<details><summary>CContact Us Page</summary>
<img src="">
</details>
- This page contains a contact form for the user to complete that will submit their message to the site admin.

<details><summary>404 Page</summary>
<img src="">
</details>
- A 404 page was created to ensure that a user can easily navigate back to the main site if they encounter a page which does not exist.

<details><summary>500 Page</summary>
<img src="">
</details>
- A 500 page was created to ensure that a user can easily navigate back to the main site if they encounter an internal server error.


### Code Structure
The website was built using Django Framework; separating the site into a number of apps.

The website apps are:
    - accounts (Based on the Boutique Ado project): This app contains the functionality around the user's account and purchased developers.
    - cart (Based on the Boutique Ado project): This app contains the functionality around the user's shopping cart.
    - checkout (Based on the Boutique Ado project): This app contains the functionality around the user's shopping cart checkout and payment.
    - contactus: This app contains the functionality around the Contact Us form, for user's to submit a message to the site admin database.
    - developer (Based on the Boutique Ado project): This app contains the functionality around the Developer pages.
    - home: This app contains the functionality around the home page.

Additionally there are:
    - support_dev: This contains the settings and main site config files.
    - templates: This contains the base.html and the django authentication allauth html templates.
    - static: This contains the css stylesheet.
    - manage.py This is the main file for starting the site.
    - README.md: This is the README documentation file
    - custom_storage.py: This is the boto3 configuration file for AWS
    - Procfile: This is to run the application
    -requirements.txt: This contains a list of the python libraries that are installed.

### Database

This is a data-centric website. Utilising html, css, js and bootstrap 5 for the front-end. With python, django framework and a Postgres database for the back-end.

### Physical Database Model

This model contains an overview of all the model fields, their types and connections. This reflects how the database is structured within the website.

<img src="readme/database/database_model.png">

### Models

The following models represent the database structure of the website:

##### UserAccount Model
The UserAccount model contains data for the user's account page.
 - Contains the following fields: user(OneToOneField), is_developer, purchased_developers(ManyToManyField).

##### Order Model
The Order model contains data on the orders.
 - Contains the following fields: order_number, username, email, date, total, original_cart, stripe_pid.

##### OrderLineItem Model
The OrderLineItem model contains data on the each entry in an order.
 - Contains the following fields: order(Foreign Key), developer(Foreign Key), lineitem_total.

##### ContactUs Model
The ContactUs model contains data on the message a user submits to the site admin.
 - Contains the following fields: user(Foreign Key), subject, body, sent_date.

##### Category Model
The Category model contains data on the categories a user can attach to their Developer Profile.
 - Contains the following fields: name, friendly_name.

##### Developer Model
The Developer model contains data on the user's Developer Profile.
 - Contains the following fields: user, profile_name, description, category(Foreign Key), price, count_sold, image.

##### Post Model
The Post model contains data on the user's Developer Profile Posts.
 - Contains the following fields: title, author(Foreign Key), publish_date, content, image.


## Technologies Used

### Languages

- HTML
- CSS
- Javascript
- Python
- Django

### Frameworks, Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/), used to create a devices mock-up image. 
- [Balsamiq](https://balsamiq.com/), used to create wireframes.
- [Bootstrap 5](httpshttps://getbootstrap.com/docs/5.2/getting-started/introduction/balsamiq.com/), used to style the website pages.
- [Favicon.io](https://favicon.io), used to create the site favicon.
- [Font Awesome](https://fontawesome.com/), used for all site icons.
- [Git](https://git-scm.com/), used for version control within VSCode to push the code to GitHub.
- [GitHub](https://github.com/), used to store project code.
- [Google Fonts](https://fonts.google.com/), used to acquire the site's font.
- [Lucidchart](http://lucidchart.com), used to create database design diagrams.
- [WC3 Validator](https://validator.w3.org/), [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/), [Wave Validator](https://wave.webaim.org/), [Lighthouse](https://developers.google.com/web/tools/lighthouse/) and [Am I Responsive](http://ami.responsivedesign.is/), used to test the site's code, performance, accessibility and responsiveness. 

## Features

The website consists of fourteen pages with 18 features.

### Navigation Bar
- Situated in a persistent position at the top of every page.
- Contains links to the other website pages.
- Available links change if the user is logged into the website;
- Logged out: "Explore Developers", "Login" and "Register".
- Logged in: "Explore Developers", "My Developer Profile", "My Account", "Contact Us" and "Log out".
- When hovering over a link on Desktop devices the link colours change. This gives visible notification to the user that the link is clickable.
- Meets user stories: ???.

### Search Bar and Filter Bar
- Situated at the top of the Explore Developers page.
- User's can conduct keyword searches which will then only display Developer Profiles that contain the keyword.
- User's can order the displayed profiles by different criteria in ascending or descending order.
- Meets user stories: ???.

### Explore Developers Section
- Situated on the Explore Developers page.
- This section displays a "Developer block" for each submitted Developer Profile (Which Profiles show depends on any search criteria).
- Each "Developer block" contains the Developer's Profile Name, Category, Profile Image, Description, Purchase count and a line to view the full profile.
- Meets user stories: ???.

### Developer Profile Details Section
- Situated on the Developer Profile page.
- This page displays the selected Developer's Profile details.
- The same information as the Explore Developer Page is displayed in this section, but some content changes depending on if the user is logged in, has purchased the profile and if the Developer has added any posts.
- The Developer's Profile price and link to purchase only show if the Developer has added any posts. This is to ensure that there is content on the profile for the user to purchase.
- If the user is not logged in, the purchase link changes to a link to the login page
- If the current user is the owner of the Developer Profile, links are available on this section to edit the profile details.
- Meets user story: ???.

### Developer Posts Section
- Situated on the Developer Profile page.
- This page displays the selected Developer's Profile Posts.
- If the Developer has added any posts, they are displayed in "post blocks" here.
- Each block contains the Post Title, Published Date, Image and Content.
- The Post content is hidden and changes to a link to purchase if a user has not purchased this profile. 
- If the user is not logged in, the purchase link changes to a link to the login page
- If the current user is the owner of the Developer Profile, links are available on this section to add a new post and to edit a post.
- Meets user story: ???.

### Create a Developer Profile Section
- This page contains a form for the user to create a Developer Profile to the website.
- All field within the form are mandatory and must be completed.
- Validation exists to ensure the fields are completed and that the Price cannot be negative.
- The user then clicks a submit button, which adds the Developer Profile to the Developer database.
- Meets user story: ???.

### Edit Developer Profile Section
- This page contains a form for the user to edit their Developer Profile.
- All field are auto-populated with the current details.
- All field within the form are mandatory and must be completed.
- Validation exists to ensure the fields are completed and that the Price cannot be negative.
- This section contains a link to the delete profile page.
- The user then clicks a submit button, which updates the Developer Profile on the Developer database.
- Meets user story: ???.

### Delete Developer Profile Section
- This page contains text and a link asking if the user is sure they want to delete their profile.
- The user can confirm deletion, or return to the edit profile page.
- Meets user story: ???.

### Developer Posts Section
- Situated on the Developer Profile page.
- This page displays the selected Developer's Profile Posts.
- If the Developer has added any posts, they are displayed in "post blocks" here.
- Each block contains the Post Title, Published Date, Image and Content.
- The Post content is hidden and changes to a link to purchase if a user has not purchased this profile. 
- If the user is not logged in, the purchase link changes to a link to the login page
- If the current user is the owner of the Developer Profile, links are available on this section to add a new post and to edit a post.
- Meets user story: ???.

### Add a New Post Section
- This page contains a form for the user to add a new post to their Developer Profile.
- All field within the form are mandatory, except the image.
- Validation exists to ensure the mandatory fields are completed.
- The user then clicks a submit button, which adds the post to the Post database.
- Meets user story: ???.

### Edit Post Section
- This page contains a form for the user to edit their Developer Profile Post.
- All field are auto-populated with the current details.
- All field within the form are mandatory, except the image.
- Validation exists to ensure the mandatory fields are completed.
- This section contains a link to the delete post page.
- The user then clicks a submit button, which updates the post on the Post database.
- Meets user story: ???.

### Delete Post Section
- This page contains text and a link asking if the user is sure they want to delete their post.
- The user can confirm deletion, or return to the edit post page.
- Meets user story: ???.

### My Account Section
- This page displays the current users account details.
- Username, Email and a link to Change Password are presented to the user.
- A purchased developer section contains the details of any Developer Profiles the user has purchase with links to each profile.
- Meets user story: ???.

### Contact Us Section
- This page contains a form for the user to submit a message to the site admin.
- All field within the form are mandatory.
- Validation exists to ensure the mandatory fields are completed.
- The user then clicks a submit button, which adds the form to the contactus database.
- Meets user story: ???.

### Login Page
- This page contains a form for the user to log in to the website.
- This page is part of Django allauth.
- Meets user story: ??.

### Register Page
- This page contains a form for the user to create an account on the website.
- This page is part of Django allauth.
- Meets user story: ??.

### 404 Page
- This page is display when a user encounters a page that does not exist (HTTP 404 response code).
- The user is provided with a link to return to the index page.

### 500 Page
- This page is display when a user encounters an internal server error(HTTP 500 response code).
- The user is provided with a link to return to the index page.

### Responsive Design
<details><summary>Responsive Design</summary>
<img src="">
</details>

- The website is full responsive on desktop to mobile devices.
- Meets user story: ???.


## Deployment

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner.

### Making a Local Clone
1. Navigate to the GitHub repository 
2. Select the Code button above the files.
3. Select the "HTTPS" tab on the dropdown window to clone with HTTPS, copy the link.
4. Open Git Bash.
5. Change the current working directory to the location where you would like the cloned directory.
6. Type "git clone " and paste the URL from the clipboard (example: "$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY")
7. Press Enter to create.
8. Create an env.py file in the root folder in the project, and add the following code with the relevant key, value pairs, and ensure you enter the correct key values.

<code>import os</code><br>

<code>os.environ.setdefault("DJANGO_SECRET_KEY", "TO BE ADDED BY USER")</code><br>

<code>os.environ.setdefault("DATABASE_URL", "TO BE ADDED BY USER")</code><br>

<code>os.environ.setdefault("AWS_ACCESS_KEY_ID", "TO BE ADDED BY USER")</code><br>
<code>os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "TO BE ADDED BY USER")</code><br>
<code>os.environ.setdefault("USE_AWS", "True")</code><br>

<code>os.environ.setdefault("STRIPE_PUBLIC_KEY", "TO BE ADDED BY USER")</code><br>
<code>os.environ.setdefault("STRIPE_SECRET_KEY", "TO BE ADDED BY USER")</code><br>
<code>os.environ.setdefault("STRIPE_WH_SECRET", "TO BE ADDED BY USER")</code><br>

<code>os.environ.setdefault("EMAIL_HOST_USER", "TO BE ADDED BY USER")</code><br>
<code>os.environ.setdefault("EMAIL_HOST_PASS", "TO BE ADDED BY USER")</code>

9. Install the relevant packages as per the requirements.txt file
10. Start the application by running <code>python3 app.py</code>

## Google Emails
To allow the website to send emails we will use a Google account as an SMTP server, by using the following steps:
1. Go to Google.com and create an email account, once logged in navigate to the settings page within your Gmail account. Then click "Other Google Account Settings"
2. Turn on the 2-step verification.
3. Click on "app passwords", choose Other as the app and set the password name, eg. Django or supportDev.
4. A 16 digit password will be generated, after clicking "create. Please take note of the password.
5. In the env.py file you previously created, populate the EMAIL_HOST_USER with the gmail account email address.
6. In the env.py file you previously created, populate the EMAIL_HOST_PASS with the 16 digit password.
7. Ensure the following code exists in the settings.py file to send the emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>
8. Ensure the variable are also set within you Production Environment (Heroku)

### Heroku
1. In the settings.py file, ensure that debug is NOT set to True.
2. Create a new file called "ProcFile" in the root directory, and add the line; 

<code>web: gunicorn support_dev.wsgi:application</code>

3. Create a requirements.txt file by running the below command in the terminal.

<code>pip freeze > requirements.txt</code>

5. Ensure ProcFile and requirements.txt are committed to your git repository in the root directory.

6. Create an account on [Heroku](https://signup.heroku.com/login?redirect-url=https%3A%2F%2Fid.heroku.com%2Foauth%2Fauthorize%3Fclient_id%3Ddd0b2de7-576f-44d7-8607-788ece271310%26redirect_uri%3Dhttps%253A%252F%252Fwww.heroku.com%252Fauth%252Fheroku%252Fcallback%26response_type%3Dcode%26scope%3Didentity%2Bread%26state%3Dcbeff6caa22dd3da82260d4764c9ad34d99bca10abeb5adb)
7. On your dashboard, select "Create New App".
<img src="readme/deployment/heroku/new_app.JPG">

8. Set a unique name and select the closest region to you. Select "Create App".
<img src="readme/deployment/heroku/create_app.JPG">

8. In Application Dashboard, navigate to the deploy section and connect to your Git account,then to your Repository. Select "Connect" (After connecting the section should look like the image below).
<img src="readme/deployment/heroku/connect_repo.JPG">

9. Navigate to the "Settings" tab.
<img src="readme/deployment/heroku/settings.JPG">

10. Select "Reveal Config Vars" and set key/value pairs from env.py.
<img src="readme/deployment/heroku/config_vars.JPG">

12. Navigate back to the "Deploy" tab.
13. Select your branch then "Enable Automatic Deploys".
<img src="readme/deployment/heroku/branch_auto_deploy.JPG">

13. When the deployment has been successful, click on "Open App" in the top-right.
<img src="readme/deployment/heroku/open_app.JPG">

## Testing

### Accessibility

WAVE WebAIM web accessibility evaluation tool was utilised to ensure the website met accessibility standards.

<details><summary></summary>
<img src="">
</details>

### Performance

To test the performance of the website, Lighthouse in Google Chrome developer tools was used. Below is the outcome.

<details><summary>Performance Test Result</summary>
<img src="">
</details>

### Device Testing

The website was tested using Google Chrome Developer Tools - Device Toolbar to simulate different device viewports. 

The following device viewports were tested using the Device Toolbar;
- iPad Pro (Tablet screen test)
- iPhone 5/SE (Mobile screen test)

The website was also tested on the following physical devices;
- iPhone 12 Pro Max
- iPhone 14 Pro Max
- Samsung Galaxy Note 8
- Kindle Fire 10

The following resolutions were tested using a Windows desktop PC;
- 1920 x 1080
- 3440 x 1440

### Browser Compatibility

The website was tested on the following browsers:
- Google Chrome
- Mozilla Firefox

### User Story Testing

1. I want to be able to register for a Developer Profile. So that I can create a unique Profile for Supporters to purchase access to.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Create A Developer Profile Page                        | Complete and submit the Form to create an Developer Profile                                | A Developer Profile is created                                      | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

2. I want to be able to access my Profile.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| My Developer Profile Page                        | Navigate to the  My Developer Profile Page                               | Able to access my Profile.                                    | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

3. I want to be able to delete my Profile.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Confirm Delete Profile Page                        | Navigate to the Confirm Delete Profile Page and click link to delete                            | Profile is deleted                             | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

4. I want to be able to register for an Account. So that I can purchase access to Developer Profiles.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| allauth Register Page                        | Navigate to the Register Page and complete the form                         | Account is created after email verification                           | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

5. I want to be able to authenticate my registration via email confirmation. So that I can confirm my Account registration was a success.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| allauth Email Verification                        | Register for an account and verify the email                        | Account is created after email verification                           | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

6. I want to be able to login to my Account. So that I can purchase and access Developer Profiles.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| allauth Login page                        | Navigate to the Login Page and complete the form                      | User is logged in.                      | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

7. I want to be able to logout of my Account. So that I can protect my Account from unauthorised access.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| allauth Logout page                        | Navigate to the Logout Page and confirm logout                     | User is logged out.                      | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

8. I want to be able to have a unique Supporter Account. So that I can view my Account details and purchased Developer Profiles.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| My Account page                        | Navigate to the My Account Page                   | User can view their account details and purchases                     | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

9. I want to be able to view my Profile from the perspective of a Developer and a Supporter. So that I can edit my Profile, and also check that the Supporter view meets my needs.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| My Developer Profile page                        | Navigate to the My Developer Profile Page                   | Developer can view their account from the perspective of a Supporter                    | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

10. I want to be able to easily create and edit my Profile content. So that I can provide content to my Subscribers.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Add/Edit/Delete Post pages                        | Navigate to the My Developer Profile page, where the Developer can edit the add/edit/delete posts.                | Developer can edit their profile content             | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

11. I want to be able to amend my Profile details. So that I can ensure my details are correct and up to date.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Edit Profile page                     | Navigate to the My Developer Profile page, select the Edit Profile link and complete the form               | Developer profile details are updated          | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

12. I want to be able to view a list of Developer Profiles. So that I can choose which Profiles I would like to purchase access to.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Explore Developers page                     | Navigate to the Explore Developers page     | List of Developer Profiles displayed  | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

13. I want to be able to view details of a Developer's Profile content. So that I can decide if the content is of interest to me.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Developer Profile page                     | Select a developer in the Explore Developers page     | View details of a Developer's Profile  | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

14. I want to be able to amend my Account details. So that I can ensure my details are correct and up to date.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| My Account page                     | Navigate to My Account page     | Change Password link can be used  | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

15. I want to be able to sort Developer Profiles by multiple criteria. So that I can quickly identify Developer profiles by price, name or post count.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Search and Filter bars                     | Navigate to Explore Developers page and use the search or filter bar     | Displayed Profiles change or are ordered, based on search or filter criteria  | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>

16. I want to be able to view a list of Developer Profiles I have purchased access to. So that I can quickly navigate to a Developer's Profile.

| **Feature**                          | **Action Required**                                                                      | **Expected Outcome**                                       | **Actual Outcome**|
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| SMy Account Page                    | Navigate to My Account page and scroll down to Purchased Developers section     | Purchased Profiles displayed and a link for each can be clicked to go to the profile  | Works as expected |

<details><summary>Screenshot</summary>
<img src="">
</details>






## Credits

## Code

### Placeholder/Test Tales
- Placeholder/Test Developer Profile and Posts for "testuser1" and "testuser2", were generated using [ChatGPT](https://chat.openai.com/auth/login).

### Images/Icons/Font
- Font from [Google-Fonts](https://fonts.google.com/)
- All website Icons taken from [FontAwesome](https://fontawesome.com/).

## Acknowledgements
Thank you to the following individuals for their support during the creation of this website; 
- Mo Shami, my Mentor, who provided excellent guidance and feedback throughout. 
- My partner and friends, for supporting with device testing.