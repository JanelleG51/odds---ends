# Odds & Ends

At Odds & Ends we never like to see a good bottle of wine being neglected, so it is our mission to gather all of the odd bottles and bin ends that vineyards have lying around and pass them on to our customers by the case for a great price. The offering is simple, pick a case at one of our three price points and you will receive a selection of 12 bottles from the stock you can see on our site. The more you pay for the case, the more expensive the overall value and your case is always guaranteed to be worth at least 50% more than you’ve paid! You can buy once or as many times as you like to take the opportunity to sample wines from all over the world that you may not get anywhere else for a bargain price.

You can view the live site [here.](https://odds-and-ends.herokuapp.com/)

![amiresponsive]()

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

____
## UX
### Strategy 

### Target Consumer 

The target customer for this site is anyone who likes and enjoys wine but might be a little uninspired by what is on offer in supermarkets and those who would like to sample lesser-known or expensive wines for a reduced price.  

### User Stories

#### As a site visitor, I want to be able to: 
- Understand the sites purpose at first glance. 
- View the wines on offer at that time. 
- Know the prices of the cases on offer.
- See the market value of each individual bottle of wine.
- Filter wines by multiple options. 
- See the number of results returned for each catergory.  

#### As a buyer, I want to be able to:
- Clearly see the purchase options available to me. 
- Complete the checkout process without the requirement to create an account.
- View the selection in my bag to be purchased.  
- Add additonal cases to purchase or delete an exisiting case.
- Easily enter payment details. 
- Know the payment process is safe and secure.
- View an order confirmation after checkout. 
- Receive a confirmation email once the sale has completed.

#### As a registered user, I want to be able to:
- Easily register for an account. 
- Easily login and logout. 
- Reset my password. 
- Receive confirmation of registration. 
- View all my details and orders in my own profile. 
- Update the details in my profile.

#### As a site owner, I want to be able to:
- Have administrator access directly through the site.
- Add, edit or delete the wines in stock. 
- Add, edit or delete the cases for sale.
- Be notified by email when customers or wineries make contact using the [Contact](https://odds-and-ends.herokuapp.com/contact/) page.

## Design
____
### Impression 

The site is one of basic presentation meant to give the feel of a handwritten specials board that can be updated daily. The site offers quality wines at a discounted price and as such the stock can change depending on what is available. The impression of basic and changable but quality is what the developer wanted the site to deliver. 

### Typography

To acheive the handwritten specials board feel, the font [Permanent Marker](https://fonts.google.com/specimen/Permanent+Marker?query=perm) was chosen for the logo and headings. 

The body of the site use [Concert One](https://fonts.google.com/specimen/Concert+One?query=concert). The curved edges of the lettering wth no sharp edges complements the Permanent Marker font and is in keeping with the overall theme.

### Colour Scheme 

### Imagery

### Wireframes


## Features 
___

## Features left to implement 
___

### Database
The build of this site used two relational databases. SQLite was used during the intial development of the site with Postgres being ustlised once the site was moved to deployment on Heroku. The database models and their relationships are illustrated and described below:

![Database Schema](readme_docs/database_schema.png)

#### User Model
- Holds a user’s registration information provided at sign up.
- Information from the User Model is used to create the UserProfile.
#### UserProfile
- Stores the user’s delivery and order history.
- Takes information from the User model to create the profile.
- The Order model receives this information to create the order history on the profile page.

#### Wines Model
- Stores the details of all wines currently held in stock and available as part of the case selections. 
- Information is pulled from the categories model to supply the wine colour.
#### Cases Model
- Stores the details of all cases currently for sale on the site (case category, type and price).
- Information is pulled from the categories model to supply the case name.
- The OrderLineItem model receives the category name to generate the correct order.
#### Categories Model
- Contains all categories for both the wines and cases models.
#### OrderLineItem
- Stores the case details that have been added to the user’s bag.
- Takes information from the cases model to add cases to the user’s order.
- Information from the OrdeLineItem is sent to the Order model to update the order.
#### Order
- Stores all of the order information for each purchase made by the user.
- Pulls information from the OrderLineItem model to add a case/s to the order.
- The order detail are used in the UserProfile model to attach the order to the user’s profile.




## Testing

The developer used [W3C HTML Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), [JSHint Validator](https://jshint.com/) [PEP8 Validator](http://pep8online.com/) for code validation.


 ### Manual Testing

The result of manual testing for the site are below:

![testing]()


## Technologies Used 
- [HTML5](https://en.wikipedia.org/wiki/HTML5) – used to complete the structure of the site.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - used to style the presentation of the content on the site.
- [JavaScript](https://www.javascript.com/) & [jQuery](https://jquery.com/) - were used for front-end dynamic interaction
- [Python](https://www.python.org/) – was incorporated as the back-end logic and the means to run/view the site. 
Python Modules: 

- [Google Fonts](https://fonts.google.com/) – provided the fonts for this site.
- [GitHub](https://github.com/join/get-started) - is the hosting platform used to store the source code for the site.
- Git - is used as version control software to commit and push code to the GitHub repository where the source code is stored.
- [Heroku](https://id.heroku.com/login) - to deploy the live website.
- [Balsamiq](https://balsamiq.com/) - was used to create wireframes for the design.
- [Font Awesome](https://fontawesome.com/) - icons displayed throughout the site are taken from Font Awesome.

## Configuration
### Deployment to Heroku
#### Requirements.txt
Heroku deployment requires a populated file of all dependencies used during the site build:
- In the GitPod terminal, type pip3 freeze --local > requirements.txt to create your requirements file.
#### Procfile
- Create a Procfile providing the app name where required web: gunicorn [app_name].wsgi:application 

### Create application:

- Login to Heroku.
- Click on 'Create New App' from your dashboard.
- Enter a unique app name.
- Select the appropriate region closest to your location.

Set up connection to Github Repository:

- From the 'Deploy' tab, set your deployment method to 'GitHub'
- From 'Deployment Method' choose 'GitHub'
- Connect to GitHub and login
- Search for the repository you wish to deploy from
- Click the 'Connect' button

### Heroku Postgres Database
- Select the resources tab in Heroku.
- In Add-ons, search for Heroku Postgres and select.
- Select the Hobby Dev-Free option in plans.
- Click submit.
- This will prvide you with the DATABASE_URL you require for the Config Vars.

In the build environment, install two requirements and add to requirements.txt:
- pip3 install dj_databse_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.txt


### Set environment variables:

In Heroku, click the settings tab and then select 'Reveal Config Vars' button and add the following:

Variable | Source | 
-----|-------------|
DATABASE_URL | Heroku Postgres   
SECRET_KEY | [Django Random Key Generator](https://miniwebtool.com/django-secret-key-generator/)
AWS_SECRET_ACCESS_KEY | AWS File 
AWS_ACCESS_KEY_ID | AWS File 
EMAIL_HOST_PASS | Email Host Generated 
EMAIL_HOST_USER | Email address being used
USE_AWS | True
STRIPE_PUBLIC_KEY | Stripe Dashboard > Developers tab > API Keys > Publishable key
STRIPE_SECRET_KEY | Stripe Dashboard > Developers tab > API Keys > Secret key
STRIPE_WH_SECRET | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret



Enable automatic deployment:

- Click the Deploy tab
- In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automatic Deploys.

### AWS

### Email

## Forking
Forking results in a secondary branch of the site being created. The secondary branch can be worked on simultaneously without the Master Branch being altered. The steps below should be followed:

1. Log into GitHub.
2. Select your desired repository from the options to the left.
3. From the options available at the top right of the screen, which include Watch, Star and Fork, select Fork.
4. A forked branch of the repository is then created. This is a copy of the repository up to the point the forked branch was created.
5. Changes can then be made in the forked repository without those changes taking effect in the Master Branch.
6. Both repositories can be merged by selecting New Pull Request from the original repository.

## Cloning
1. Log into GitHub.
2. Select your desired repository from the options to the left.
3. From the options available just above the commit list, which include Go to File, Add File, Code and Gitpod, select Code.
4. From the HTTPS tab, copy the URL for the repository.
5. Once in your local IDE open a new terminal.
6. Chose the working directory where you would like the cloned directory to be created.
7. Type git clone into the terminal and paste the repository URL
- $ git clone https://github.com/JayMacG51/odds---ends
8. Press enter to finish the cloning process.

All requirements will need to be reinstalled. You can do this in the terminal using pip3 install -r requirements.txt 

## Credits

### Content
 
### Code

### Acknowledgements

