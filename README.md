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
2. I want to be able to authenticate my registration via email confirmation. So that I can confirm my account registration was a success.
3. I want to be able to login to my Profile. So that I can access my Developer Profile.
4. I want to be able to logout of my Profile. So that I can protect my Profile from unauthorised access.
5. I want to be able to have a unique Developer Profile. So that I can provide Supporters with my exclusive content and save my payment details.

- Supporter
6. I want to be able to register for a Supporter Account. So that I can purchase access to Developer Profiles.
7. I want to be able to authenticate my registration via email confirmation. So that I can confirm my Account registration was a success.
8. I want to be able to login to my Account. So that I can purchase and access Developer Profiles.
9. I want to be able to logout of my Account. So that I can protect my Account from unauthorised access.
10. I want to be able to have a unique Supporter Account. So that I can view my Account details and purchased Developer Profiles.

### Site Navigation and Views 

- Developer 
11. I want to be able to view my Profile from both the perspective of a Developer and a Supporter. So that I can edit my Profile, and also check that the Supporter view meets my needs.
12. I want to be able to view data on my Supporters. So that I can use this information to tailor my Profile content if required.
13. I want to be able to easily create and edit my Profile content. So that I can provide content to my Subscribers.
14. I want to be able to amend my Profile details. So that I can ensure my details are correct and up to date.

- Supporter
16. I want to be able to view a list of Developer Profiles. So that I can choose which Profiles I would like to purchase access to.
17. I want to be able to view details of a Developer's Profile content. So that I can decide if the content is of interest to me.
18. I want to be able to amend my Account details. So that I can ensure my details are correct and up to date.
19. I want to be able to sort Developer Profiles by multiple criteria. So that I can quickly identify Developer profiles by price, category or post count.
20. I want to be able to view a list of Developer Profiles I have purchased access to. So that I can quickly navigate to a Developer's Profile.

### Structure

The website structure consists of the main "Base" page, with the following sections being added to this page dependant on the URL; Index Page, Explore Developers Page, Login Page, Register Page, Developer Profile/My Developer Profile Page, Create Developer Profile Page, Edit Developer Profile Page, Add a New Post Page, Edit Post Page, My Account Page, Shopping Cart Page, Checkout Page, Checkout Success Page, 404 Error Page and 500 Error Page.

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

<details><summary>404 Page</summary>
<img src="">
</details>
- A 404 page was created to ensure that a user can easily navigate back to the main site if they encounter a page which does not exist.

<details><summary>500 Page</summary>
<img src="">
</details>
- A 500 page was created to ensure that a user can easily navigate back to the main site if they encounter an internal server error.
