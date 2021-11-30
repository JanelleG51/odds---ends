# Testing 
## Contents
  * [User Story Testing](#user-story-testing)
  * [Validator Testing](#validator-testing)
  * [Manual Testing](#manual-testing)
  * [Bugs Fixes](#bugs-fixes)
  * [Known Bugs](#known-bugs)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Story Testing 

#### As a site visitor, I want to be able to: 
- Understand the sites purpose at first glance.

The home page clearly layouts the sites name and purpose without user's having to search:
![Home Page](readme_docs/user_stories/user_story_one.png)
- View the wines on offer at that time.

There are clearly named links on the navigation bar that take user's to the wine's they wish to view:
![Wines](readme_docs/user_stories/user_story_two.png)
- Know the prices of the cases on offer.

The three price points of cases is clearly displayed on the cases page:
![Cases](readme_docs/user_stories/user_story_three.png)
- See the market value of each individual bottle of wine.

By accessing the wines page the user is able to view all wines or filter by their desired view:
![Wine Price](readme_docs/user_stories/user_story_four.png)


- Filter wines by multiple options. 

User can filter directly from the navigation bar or from the wine page itself using the dropdown filter:
![Wines Filter](readme_docs/user_stories/user_story_five.png)
- See the number of results returned for each catergory.

When user view a specific colour of wine the number of wines in that colour category appears at the top left of the screen They are also provided with a link to take them back to all wines:
![Number of wines](readme_docs/user_stories/user_story_six.png)  

#### As a buyer, I want to be able to:
- Clearly see the purchase options available to me.

User are presented with the purchase options available to them by following the cases link on the the navigaiton bar or through the Buy Our Cases buttons present on both the Home Page and on every wine details page. Once the user has selected a case, the options for each case are presented to them in a drop down menu :
![Options](readme_docs/user_stories/user_story_seven.png)  
- Complete the checkout process without the requirement to create an account.

User's are not required to have an account to purchase but are invited to login or create an account to save their details and purchase history:
![Guest](readme_docs/user_stories/user_story_eight.png)
- View the selection in my bag to be purchased. 

Buyer's are able to access their bag at the top right of the screen and can access this at anytime, whether there are items there or not. If no items have been added, the user will see that the bag is empty:
![Bag](readme_docs/user_stories/user_story_nine.png)
- Add additonal cases to purchase or delete an exisiting case.

Using the quantity buttons (plus and minus) in the picture above, user's can easily adjust the number of cases they would like to order and update the bag using the update button. Orders for each case are limited to 10 and users can remove cases they do not want anymore by clicking the remove button.
- Easily enter payment details.

Unregistered user's are required to provide their delivery details and card information on one page to make a purchase. Registered user's can use the saved delivery details from their profiles:

![Payment](readme_docs/user_stories/user_story_eleven.png)
- Know the payment process is safe and secure.

The site uses Stripe as the third party payment processor. Stripe is a well respected provider of this service for security and safety.
- View an order confirmation after checkout. 

Once a purchase had completed, the user receives a confirmation page on the site.
![Confirmation](readme_docs/user_stories/user_story_twelve.png)
- Receive a confirmation email once the sale has completed.

As well as the on screen confirmatiom, user's also receive an email:
![Email](readme_docs/user_stories/user_story_thirteen.png)

#### As a registered user, I want to be able to:
- Easily register for an account.

All user's can register for an account providing 3 pieces of information, an email, a username and a password. The email and username must unique and user's will be informed if either is already in use:

![Register](readme_docs/user_stories/user_story_fourteen.png)

![Validation](readme_docs/user_stories/registration_validation.png)
- Easily login and logout.

User can easily sign in with either their username or password and sign out by confirming they would like to sign out of the site:

![Sign in](readme_docs/user_stories/sign_in.png)
- Reset my password. 

User's can reset their password by clicking on the Forgot Password link on the sign in page. They will be sent an email to follow a link to reset:
![Reset password](readme_docs/user_stories/password_reset.png)
![Reset Email](readme_docs/user_stories/password_reset_email.png)
- Receive confirmation of registration.

User's are required to verify their email on registration and an email to allow them to do this is sent. Once verified, user's can then log in:

![Registration](readme_docs/user_stories/confirm_email_address.png)
![Verify](readme_docs/user_stories/verify_email.png)
- View all my details and orders in my own profile.

Once registered, user's will be able to see their purchase history in their profile page:
![Profile](readme_docs/user_stories/order_history.png)
- Update the details in my profile.

User's can update all of their default information directly from their profile by filling in the fields with the new information and clicking the Update Information button.

#### As a site owner, I want to be able to:
- Have administrator access directly through the site.

Site administrators can create, update and delete content directly through the frontend of the site.
- Add, edit or delete the wines in stock.

![Add wine](readme_docs/user_stories/add_wine.png)
- Add, edit or delete the cases for sale.

![Edit case](readme_docs/user_stories/edit_case.png)
- Be notified by email when customers or wineries make contact using the contact page.

Customer's and wineries are invited to contact the site admin and can do so using the site Contact page. User's are notified their email has been sent and Admin are notified by email when someone makes contact:

![Email](readme_docs/user_stories/email_toast.png)
![Contact](readme_docs/user_stories/email_received.png)


## Validator Testing 

The developer used [W3C HTML Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), [JSHint Validator](https://jshint.com/) [PEP8 Validator](http://pep8online.com/) for code validation.

When passing the HTML source code through the validator, one error for an additonal icon element appeared and this was rectifed. The code used to display the upload image field as a button to improve UX showed a duplication of id error, however this was not evident. As this particular code was serving a very specific purpose the developer chose to leave the it as it was. Once the extra element was removed all other HTML code on pages other than the edit/add pages had no errors or warnings:

![html](readme_docs/validator_images/home_page_html_error.png)
![id](readme_docs/validator_images/add_wine_error.png)

All CSS was passed through the CSS Validator with no errors or warnings:

![CSS](readme_docs/validator_images/css_validation.png)

All JS content passed through the JSHint Validator with no warnings or errors.

All Python code was passed the through PEP8 Validator and highlighted strings that were too long to be compliant, these issues were rectified and all code passed:

![Pep8](readme_docs/validator_images/pep_8_validation.png)

### Lighthouse Results

![lighthouse](readme_docs/validator_images/lighthouse_score.png)

## Manual Testing 

## Navigation 
Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Site Logo | Takes user back to home page | Pass
Account Link | Provides dropdown with links depending on permissions | Pass
Register Link | Takes user to Registration page | Pass
Sign In Link | Takes user to Sign In page | Pass
Add Wine (admin only) | Takes user to Add Wine page | Pass
Add Case (admin only) | Takes user to Add case page | Pass
Bag Link | Take user to bag page regardless of content | Pass
Navigation Bar | Each link opens a dropdown menu where appropiate and links user to the requested page | Pass 

## Home Page 

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Site Logo (on page) | Takes user back to home page | Pass
Buy Our Cases button | Takes user to Cases page | Pass
Contact Us! button | Takes user to Contact page | Pass
Browse Our Wines! button | Take user to All Wines page | Pass 

## Wine Pages 
Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Provide a view of all wines on the site | Shows all wines or a specific category and a count of the total number of each | Pass
Users can click on each wine and be taken to it's detail page | The user is navigated to the detail page for each wine | Pass
Filter all wines | When a user filters wine by the options in the dropdown filter the categories display correctly  | Pass
Back to top button | When a user scrolls down the page the back to top button stays fixed in the bottom right corner and takes users back the top of the page when clicked | Pass 
Edit button (admin only) | Takes admin to edit page for the specific wine | Pass 

## Wine Detail Page 

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Keep Browsing Wines button | Takes user back to all wines page | Pass
Buy Our Cases button | Takes user to Cases page | Pass
Edit button (admin only) | Takes admin to edit page for that specific wine | Pass
Delete button (admin only) | Reveals a confirmation modal that requires the user to confirm deletion or cancel. When confirmed, the wine is deleted | Pass


## Cases Page
Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Shows user all cases on offer | Case and their names and prices appear on view | Pass
Taken to case detail page | When clicked the user is directed to the case detail page | Pass
Edit button (admin only) | Takes admin to edit page for that specific wine | Pass

## Case Detail Page 
Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Keep Shopping button | Takes user back to all cases page | Pass
Type Selector | Dropdown menu that allows users to select what type of case they would like  | Pass
Quantity selector | Allows user to select between 1 to 10 cases | Pass
Add to Bag button | Adds the user selection the the bag and a success confirmation toast appears at the top right of the screen with added contents and link to checkout | Pass
Edit button (admin only) | Takes admin to edit page for that specific case | Pass
Delete button (admin only) | Reveals a confirmation modal that requires the user to confirm deletion or cancel. When confimred, the case is deleted | Pass

## Bag Page 

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Keep Shopping button | Takes user back to all cases page | Pass
Quantity selector | Allows user to select between 1 to 10 cases | Pass
Update button | Updates the contents of the bag to the users selected value and adjusts the total, delivey and grand total. A success toast appears to confirm the users action| Pass
Remove button | Removes the selected case from the bag adjusts the total, delivey and grand total. A success toast appears to confirm the users action. If the bag is now empty, it will say the bag is empty and show the Keep Shopping button | Pass
Secure Checkout button | Takes user to the checkout page | Pass 

## Checkout Page 

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Adjust bag button | Takes user back to bag page | Pass
Create an account button | Only shows for users with no account or not signed in. Direct users to the Register page | Pass
Login button | Only shows for users with no account or not signed in. Direct user's to the Register page | Pass
Secure Checkout button | Takes user to the checkout page | Pass 
Complete order button | Once users have completed their delivery and payment details, the complete order button triggers the Stripe payment system and the webhook creates the order. A loading spinner should appear then confirmation of the order | Pass 

## Contact Page 

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Select contact type | Dropdown lets user's select if they are a Customer or a Winery | Pass
Confirmation | On hitting the send button users receive a success toast notification at the top right of screen  | Pass
Email sent | Site admin recieves the email | Pass

## Footer

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Links in Customer Care | Links all direct to Contact Us page | Pass
Links in Account | Register and Sign in only display when user is not logged in. Profile link displays when user is logged in | Pass
Register and Sign in| Links lead to register and sign in pages | Pass
Bag Link | Displays all the time and directs users to the bag page | Pass 
Social Links | Direct users to exteral site in a new page | Pass

## Sign In Page 

Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Success message | When a user logs in a success toast appears to confirm the login and shows the users username | Pass
Remember me | Stores the users login details | Pass
Forget password | Send user an email with a link to reset their password | Pass
Register | Directs users to the register page to create and account if they don't have one | Pass 

## Register Page
Feature | Expected Behaviour | Outcome |
-------|--------------------- |---------|
Success message | When a user logs in a success toast appears to confirm an email has been sent to the users email address to complete verification | Pass
Verify Email | A message appears on screen confirming the user is required to confirm their email | Pass
Sign in link | Directs users to the sign in page | Pass




## Bugs Fixes

## Known Bugs 

