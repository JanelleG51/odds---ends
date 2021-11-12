# Odds & Ends

![amiresponsive]()

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## About

## UX
### Strategy 

### Target Audience

### User Stories



### Site Goals

## Scope
### Planned features: Backend and frontend development 
 
  
![scope diagram]()

## Structure
 

![database strcture]()

### Database Schema


![database strcture]()

![database strcture]()

## Validation and Security
.
### Backend environment:

## Features 
### Design
### Skeleton

#### Wireframes
#### Home
![Home]()
#### Register
![Register]()
#### Log In
![Login]()
#### Profile
![Profile]()

#### Contact
![Contact]()

## Features 

## Design

![Colours]()

### Typography 

## Imagery


### Alterations to design

## Features left to implement 

## Testing

The developer used [W3C HTML Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), [JSHint Validator](https://jshint.com/) [PEP8 Validator](http://pep8online.com/) for code validation.

 ![validator]()

 ### Manual Testing

The result of manual testing for the site are below:

![testing]()


## Technologies
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

### AWS


## Deployment to Heroku

### Create application:

- Login to Heroku.
- Click on the new button.
- Select create new app.
- Enter the app name.
- Select region.

Set up connection to Github Repository:

- Set your deployment method to 'GitHub'
- Connect to GitHub and login
- Search for the repository you wish to deploy from
- Click the connect button.

Set environment variables:

Click the settings tab and then click the Reveal Config Vars button and add the following:

- key: IP, value: 0.0.0.0
- key: PORT, value: 5000
- key: MONGO_DBNAME, value: (database name you want to connect to)
- key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and dbname that you set up in the link).
- key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).

Enable automatic deployment:

- Click the Deploy tab
- In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

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
7. Type git clone into the terminal and paste the repository URL.
8. Press enter to finish the cloning process.

## Credits

### Content
 
### Code

### Acknowledgements

