## Bark & Brew Booking site
![](READMEfiles/Responsive.png)
[Click Here To Visit Live Site](https://bark-and-brew-1096d5f890c8.herokuapp.com/)

## Table Of Contents:
1. [Design & Planning](#design)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Colour Scheme](#colour-scheme)
    * [Database Diagram](#database-diagram)
    
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Libraries](#libraries-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Design

Bark & Brew was designed with dog lovers and coffee enjoyers offering a welcoming booking webpage.
The design remains clean and minimal, ensuring that users can easily focus on the content and navigate the site without distractions.

### Colour Scheme
**Colors:** Originally I used a site to get colors from the main background picture.  
![](READMEfiles/Canvas.png)

I then used coolors and just brightened up the colors and generated an orange to use as a stand out color.  
![](READMEfiles/Coolors.png)


**Fonts:** I chose the Montserrat and Roboto fonts because they were simple and clean looking to not distract the user away from the content on the site.

**Images:** Most Images were taken from [Pexels.com](https://www.pexels.com/)
            Thank you, Jemma, Teddy, Tyson and Botila for staring as the waiters & waitresses

### Agile Methodology
I used the Projects tool within GitHub to manage the different processes needed for this project to be completed. At the beginning, a Project titled "Bark & Brew Project Board" was created on GitHub and linked to the Bark & Brew repository. I did change the name of the repository as originally it was titled django-project. The project board can be found [here](https://github.com/users/MEdw4rds/projects/6/views/1).

I found it diffcult to work on agile as it was an individual project and I was already aware of all the changes and what I wished for things to do and look like.  
I understand the practice and know why it's important as the scope of a project gets bigger and as the team size increases but other than just noting down ideas to do later on it wasn't a gigantic contributor to my project as I found myself just knowing what I had to do next as the scope of the project is narrower however it is useful for deciding future features. 

### User Stories

[#1 User Story: Users Can Create an Account](https://github.com/MEdw4rds/django-blog/issues/13)  
[#2 User Story: Users Can book a timeslot to visit](https://github.com/MEdw4rds/django-blog/issues/11)  
[#3 User Story: Users Can manage their bookings ](https://github.com/MEdw4rds/django-blog/issues/20)  
[#4 User Story: Users can't book a timeslot for a past date](https://github.com/MEdw4rds/Bark-and-Brew/issues/1)  
[#5 User Story: Admin can manage and disable timeslots if required](https://github.com/MEdw4rds/django-blog/issues/12)  
[#6 User Story: Welcoming and easy to navigate homepage](https://github.com/MEdw4rds/Bark-and-Brew/issues/2)  
[#7 User Story: A simple booking form for users to fill out](https://github.com/MEdw4rds/Bark-and-Brew/issues/3)  

### Wireframes
I didn't do alot of wireframes but I knew I wanted to keep it simplistic.
![](READMEfiles/wireframe_homepage.png)
![](READMEfiles/wireframe_booking.png)
![](READMEfiles/wireframe_login.png)

### DataBase Diagram
![](READMEfiles/ERD.png)

## Features:
Explain your features on the website,(navigation, pages, links, forms, input fields, CRUD....)
### Navigation
<details><summary>Navbar</summary>
<img src="READMEfiles/full navbar.png">
</details>
<details><summary>Navbar medium screens</summary>
<img src="READMEfiles/small closed navbar.png">
<img src="READMEfiles/small open navbar.png">
</details>

### Footer

### Home-page
![](READMEfiles/chrome.png)

### CRUD
![](READMEfiles/edit.png)
![](READMEfiles/delete.png)

### Profile-page
<img src="READMEfiles/bookings page.png">

### Authentication-Authorisation 
## Technologies Used

## Testing

### Google's Lighthouse Performance
Lighthouse is green other than performance the main culprit being the LCP.
I would show other pages however as all other pages require logins to access and will redirect to the login page lighthouse is getting redirected everytime.
However I believe that it the same issue would persist for all pages as most the images are very high resolution.
<details><summary>Lighthouse Desktop</summary>
<img src="READMEfiles/lighthouse desk.png">
</details>
<details><summary>Lighthouse Mobile</summary>
<img src="READMEfiles/lighthouse mob.png">
</details>

### Browser Compatibility
<details><summary>Chrome homepage</summary>
<img src="READMEfiles/chrome.png">
</details>
<details><summary>Edge booking page</summary>
<img src="READMEfiles/booking page on edge.png">
</details>

### Code Validation

**HTML**
<details><summary>Homepage</summary>
<img src="READMEfiles/Homepage.png">
</details>
<details><summary>Login</summary>
<img src="READMEfiles/login.png">
</details>
<details><summary>Logout</summary>
<img src="READMEfiles/logout.png">
</details>

The errors on the signup page are caused by the allauth form used.
<details><summary>Signup</summary>
<img src="READMEfiles/Signup page valid.png">
</details>

<details><summary>Booking Page</summary>
<img src="READMEfiles/booking.png">
</details>
<details><summary>User Booking Page</summary>
<img src="READMEfiles/profile page.png">
</details>
<details><summary>User Booking Page</summary>
<img src="READMEfiles/edit booking valid.png">
</details>
<details><summary>Success Page</summary>
<img src="READMEfiles/html success page.png">
</details>

**CSS**
<details><summary>Main styling</summary>
<img src="READMEfiles/style style.png">
</details>
<details><summary>Booking styling</summary>
<img src="READMEfiles/style booking.png">
</details>


**Python**
<details><summary>booking admin.py</summary>
<img src="READMEfiles/booking admin.png">
</details>
<details><summary>booking forms.py</summary>
<img src="READMEfiles/booking forms.png">
</details>
<details><summary>booking model.py</summary>
<img src="READMEfiles/booking model.png">
</details>
<details><summary>booking views.py</summary>
<img src="READMEfiles/booking views.png">
</details>
<details><summary>booking urls.py</summary>
<img src="READMEfiles/booking urls.png">
</details>

### Manual Testing features
Test all your features, you can use the same approach 
| Feature | Action | Status | 
|:-------:|:--------| :--------|
| Login | Input name and password | &check; |
| Signup | Input name and password and password again | &check; |
| Create Booking | Sign in and pick a free date and time | &check; |
| Cannot create duplicate booking | Sign in and pick the same date and time  | &check; |
| Cannot create bookings on sunday | Sign in and pick a sunday date at anytime | &check; |
| Cannot book a past date | Sign in and pick a date and time and be shown a message stating that it isn't possible to book a past date | &check; |
| Edit Booking | Sign in go to bookings page and see created bookings, click edit, edit however required and submit | &check; |
| Cancel Booking | Sign in go to bookings page and see created bookings, click edit, click cancel booking | &check; |
| Delete Booking | Sign in go to bookings page and see created bookings, look under Cancelled Bookings and click delete on the desired booking to delete | &check; |
| Admin panel link in navbar | When logged in as a superuser a new link appears on the navbar that will open the admin panel in a new tab | &check; |

<details><summary>Login Screenshot</summary>
<img src="READMEfiles/login form.png">
</details>
<details><summary>Book Screenshot</summary>
<img src="READMEfiles/book.png">
</details>
<details><summary>No Duplicate Screenshot</summary>
<img src="READMEfiles/no duplicates.png">
</details>
<details><summary>No bookings on Sunday Screenshot</summary>
<img src="READMEfiles/no sunday.png">
</details>
<details><summary>Cannot book a past date Screenshot</summary>
<img src="READMEfiles/no past date.png">
</details>
<details><summary>Edit bookings & Cancel booking Screenshot</summary>
<img src="READMEfiles/crud.png">
<img src="READMEfiles/edit booking form.png">
</details>
<details><summary>Delete booking Screenshot</summary>
<img src="READMEfiles/crud.png">
</details>
<details><summary>Admin panel link in navbar for admins only</summary>
<img src="READMEfiles/admin nav.png">
<img src="READMEfiles/admin panel.png">
</details>


## Bugs
Bookings being made on the same time even while being added to unique, fixed with the help of Copilot. 

## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/gitpod-full-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository from template**.
- Once the repository was created, I clicked the green **gitpod** button to create a workspace in gitpod so that I could write the code for the site.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Create a database 
- Log into [CIdatabase maker](https://www.heroku.com/](https://dbs.ci-dbs.net/))
- add your email address in input field and submit the form
- open database link in your email
- paste dabase URL in your DATABASE_URL variable in env.py file and in Heroku config vars

#### Deploying to Heroku.
- Head back over to [heroku](https://www.heroku.com/) and click on your **app** and then go to the **Settings tab**
- On the **settings page** scroll down to the **config vars** section and enter the **DATABASE_URL** which you will set equal to the elephantSQL URL, create **Secret key** this can be anything,
**CLOUDINARY_URL** this will be set to your cloudinary url and finally **Port** which will be set to 8000.
- Then scroll to the top and go to the **deploy tab** and go down to the **Deployment method** section and select **Github** and then sign into your account.
- Below that in the **search for a repository to connect to** search box enter the name of your repository that you created on **GitHub** and click **connect**
- Once it has been connected scroll down to the **Manual Deploy** and click **Deploy branch** when it has deployed you will see a **view app** button below and this will bring you to your newly deployed app.
- Please note that when deploying manually you will have to deploy after each change you make to your repository.

## Credits
List of used resources for your website (text, images, snippets of code, projects....)
I Think Therefor I blog for the navbar/footer
Bootstrap card/ classes

### AI uses:
I used copilot for a small amount of content just for a dog profile as well as helping with the booking view, getting the success or error messages to show up for the user and the clean part of the booking model to stop bookings on certain days.