# Haircut Hysteria Hackathon

<img src=static/images/readme/responsive_mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

The deployed site can be found [here](https://hh-booking-project-05701fec89a2.herokuapp.com/).

# Index
- [Purpose](#purpose)
- [Planning](#planning)
- [User Stories](#user-stories)
- [Project Board](#project_board)
- [Flowchart & ERD](#flowchart_&_erd)
- [Design Decisions & UX](#design_decisions_&_ux)
- [Features](#features)
- [Testing and Validation](#testing-and-validation)
- [AI](#ai)
- [Deployment](#deployment)
- [Reflection](#reflection)
- [Technologies Used](#technologies-used)
- [Credits](#credits)

## Purpose

This project is a web appplication for a fictional hair salon with online booking functionality.

## Planning

<img src=static/images/readme/planning/Hackathon_Booking_System_Planning_Board.jpg image alt="Screenshot of project Miro board" width="600">

<br>

Initially the project was planned out using a Miro board to start to brainstorm some ideas, concepts and content.

[View Miro board](https://miro.com/welcomeonboard/ZWx3Q2VRZDR3QVlGL3hSbW5naXhRYVJVYjRnR3Z3UnkzNFFUZ3BBWXZoNDJoRS8zdG52MDJUZkdVWHV4cXJCYjRTWFEzYmg0UFArZGxmT25Oc0kvLy9JakhRbC9OQkhFYTY0YkNHUWNsZk5GaEt0ay93ZEtlSUl1U0FNSXQyWEIhZQ==?share_link_id=365652369506)

## User Stories

<table>

  <tr>
    <th>User Story</th>
    <th>Moscow</th>
    <th>Acceptance Criteria</th>
  </tr>

  <tr>
    <td>As an Admin/Stylist,
    I can manage bookings on the admin dashboard </td>
    <td>Must Have</td>
    <td>
    - Be able to cancel or reschedule bookings
    - 
    </td>
    </tr>

  <tr>
    <td>As a User,
    I want to log in using my login details 
    So that I can access my current bookings.</td>
    <td>Must Have</td>
    <td>
    - User can log in using credentials they register with
    - If login is successful, the user can see their bookings
    </td>
  </tr>

  <tr>
    <td>As a User,
    I want to update or cancel my appointment 
    So that I can modify my booking if necessery</td>
    <td>Must Have</td>
    <td>
    - The user can update their appoinment's date or time
    - the user can cancel an appointment 
    - after updating or canceling, the user receives a notification</td>
  </tr>

  <tr>
    <td>As a User,
    I want to be able to leave a message in the booking form,
    So that I can provide additional information or special requests for my appointment</td>
    <td>Must Have </td>
    <td>
    - Booking form includes an optional "Message" text box
    - The user can enter up to 500 characters in the message field
    - Message field optional
    </td>
  </tr>
  
  <tr>
    <td>As a Admin,
    I want to be able to view and manage all user appoinments
    So that I can assist users with their bookings.</td>
    <td>Must Have</td>
    <td>
    - Admin can view all user appointments in a list
    - Admin can filter appointments by date, stylist, and status
    - Admin can cancel or modify any user appointments
    </td>
  </tr>

  <tr>

  <tr>
    <td>As a User</td>
    <td>Won't Have</td>
    <td>Feature for future iteration.</td>
  </tr>

</table>

All user stories can be found on the [Project Board](https://github.com/users/E-Printer/projects/4/views/1) including the relevant tasks, MOSCOW prioritisation for them and current status. 

## Agile Methodolgies & Project Board

<img src=static/images/readme/planning/haircut-hysteria-project-board.png alt="Screenshot of GitHub project board" width="600">

<br>

The completed sprint was composed of 14 separate items. Having used the MoSCoW approach to prioritisation, 9 were classified as "Must-Have", 3 as "Should-Have" and 1 "Could-Have". The rest of the first sprint was made up of "Won't-Have" items and remain in the backlog. 

We partially applied some of the acceptance criteria of some of our Should Have Critieria such as including contact information with the rest of acceptance criteria in the backlog such as adding maps and contact forms.

Full [Project Board](https://github.com/users/E-Printer/projects/4/)

## Flowchart & ERD

<img src=static/images/readme/planning/readme-flowchart.png image alt="Flowchart for the application functions and features" width="600" height="">

<br>

A flowchart to show the potential flow of users across the application and to help understand potential issues and the best approach to planning the project and future iterations.

<br>

The ERD (Entity Relationship Diagram) shows all relationships for the models used within the project.


<img src=static/images/readme/planning/model_relationships.png image alt="ERD diagram" width="600" height="300">

## Design Decisions & UX

Many different wireframes were produced to help plan the project including for desktop, tablet and mobile devices.

We had several ideas during the wireframing process and as the project took shape our designs evolved. 

### Desktop

<img src=static/images/readme/wireframes/wireframes-1.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-2.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-3.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-4.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-5.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/wireframes-6.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/Desktop_Create_Booking.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/Desktop_Booking_Confirmed.png image alt="desktop wireframe for homepage" width="600">

<br>

<img src=static/images/readme/wireframes/Desktop_Booking_Deleted.png image alt="desktop wireframe for homepage" width="600">

<br>

### Tablet

<img src=static/images/readme/wireframes/Tablet_Create_Booking.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Tablet_Booking_Confirmed.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Tablet_Booking_Deleted.png image alt="tablet wireframes for all pages" height="300">

<br>

### Mobile

<img src=static/images/readme/wireframes/Mobile_Create_Booking.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Mobile_Booking_Confirmed.png image alt="tablet wireframes for all pages" height="300">

<br>

<img src=static/images/readme/wireframes/Mobile_Booking_Deleted.png image alt="tablet wireframes for all pages" height="300">

<br>

### Typography

We selected our fonts from [Google Fonts](www.googlefonts.com) and choose Roboto for the main body text, Lato for H1 headings and Noticia Text for the Brand. 

<img src=static/images/readme/design/hh_fonts.png image alt="screenshot of Google fonts selected for project" width="600">

<br>

### Colours and Images

<img src=static/images/readme/design/hh_colours.png image alt="screenshot of colours selected for project" width="600">

<br>

### Images & Icons

We sourced images from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/) as well as lifting some of our stylist images from Google images of celebrities and this hairdressing website [scar](https://scarhair.com/) Full links to stock images can be found on our [Miro board](https://miro.com/welcomeonboard/ZWx3Q2VRZDR3QVlGL3hSbW5naXhRYVJVYjRnR3Z3UnkzNFFUZ3BBWXZoNDJoRS8zdG52MDJUZkdVWHV4cXJCYjRTWFEzYmg0UFArZGxmT25Oc0kvLy9JakhRbC9OQkhFYTY0YkNHUWNsZk5GaEt0ay93ZEtlSUl1U0FNSXQyWEIhZQ==?share_link_id=365652369506).

### Accessibility

<img src=static/images/readme/responsive_mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

### Accessibility Considerations

## Features

<br>

**Home Page**

The Home page of the site shows a carousel of images of the hair salon and an about section for the stylists at the salon.

**Appointments**

The Appointments section allows site visitors to create, edit and delete upcoming appointments and receive confirmation that this has been done. 

When a user is logged in, they can see My Bookings to view all their bookings and amend them.

**Services**

**The Footer**

The Footer has links to the various relevant professional and social media pages for the site owner.

**Reigster**

The site has a facility to sign up as a user in order this enables them to create, edit or delete their own reviews or comments on project posts.

**Sign In**

The site has a facility to sign in, once a user creates an account, this enables them to create, edit or delete their own reviews or comments on project posts.

**Sign Out**

The site has a facility for a user to sign out of their account.

**Admin**

The site has a facility for designated administrators to sign in, in order to administrate the site via the standard Django admin interface.

## Testing and Validation

### Manual Testing

The site was tested on the following browsers for compatibility:

### Chrome

| Test                                    | Expected Result | Actual Result |
| --------------------------------------- | --------------- | ------------- |
| Click Home menu                         | Success         | Success       |
### Safari

| Test                                    | Expected Result | Actual Result |
| --------------------------------------- | --------------- | ------------- |
| Click Home menu                         | Success         | Success       |

### Lighthouse

The site was tested using Lighthouse acheiving the following results:

<img src=static/images/readme/testing/lighthouse_1.png alt="A screenshot showing the results of Lighthouse testing" width="600">

<br>

<img src=static/images/readme/testing/lighthouse_2.png alt="A screenshot showing the results of Lighthouse testing" width="600">

#### Further results for Lighthouse testing shown below:

##### Performance

<img src=static/images/readme/testing/lighthouse_3.png alt="A screenshot showing the results of Lighthouse testing" width="600">

<br>

##### Accessibility

<img src=static/images/readme/testing/lighthouse_4.png alt="A screenshot showing the results of Lighthouse testing" width="600">

<br>

##### Best Practises

<img src=static/images/readme/testing/lighthouse_5.png alt="A screenshot showing the results of Lighthouse testing" width="600">

<br>

##### SEO

<img src=static/images/readme/testing/lighthouse_6.png alt="A screenshot showing the results of Lighthouse testing" width="600">

### Responsive Testing


### Validator Testing

- HTML

**Homepage**<hr>
<img src=static/images/readme/validation/home_html.png alt="HTML validation screenshot">

**Project Detail**<hr>
<img src=static/images/readme/validation/project_detail_html.png alt="HTML validation screenshot">

**About**<hr>
<img src=static/images/readme/validation/about_html.png alt="HTML validation screenshot">

**Reviews**<hr>
<img src=static/images/readme/validation/reviews_html.png alt="HTML validation screenshot">

**Contact**<hr>
<img src=static/images/readme/validation/contact_html.png alt="HTML validation screenshot">

<hr>

- CSS

<br>

<img src=static/images/readme/testing/css_validator.png alt="css validation screenshot">

<hr>

- Javascript

<img src=static/images/readme/testing/services_js.png alt="JS Hint for services.js">

<br>

<img src=static/images/readme/testing/toasts_js.png alt="JS Hint for toasts.js">

### Bugs

We had some bugs involving the carousel, carousel buttons and CTA button for Book Now and how this changed on different views and devices.

## AI

We utilised Claude AI and ChatGPT to support with fixing our code and troubleshooting.

## Deployment

The site was deployed to Heroku from the main branch of the repository early in the development stage for continuous deployment and checking.

The Heroku app is setup with 3 environment variables, repalcing the environment variables stored in env.py (which doesn't get pushed to github).

In order to create an Heroku app:

1. Click on New in the Heroku dashboard, and Create new app from the menu dropdown.

2. Give your new app a unique name, and choose a region, preferably one that is geographically closest to you.

3. Click "Create app"

4. In your app settings, click on "Reveal Config Vars" and add the environment variables for your app. These are:

- DATABASE_URL - your database connection string
- SECRET_Key - the secret key for your app
- CLOUDINARY_URL - the cloudinary url for your image store

The PostgreSQL database is served from NeonDB provided by Code Institute.

Once the app setup is complete, click on the Deploy tab then follow these steps:

1. Connect to the required GitHub account
2. Select the relevant repository to deploy from
3. Click the Deploy Branch button to start the deployment.
4. Once deployment finishes the app can be launched.

The deployed site can be found [here](https://ci-full-stack-portfolio-app-7c4baf7a6f9d.herokuapp.com/).

## Reflection

### Successes

### Challenges

### Future Improvements & Iterations

There were some features in our project board that we would like to build on including adding a contact form and map within the contact information.

## Credits

- This project is based on the "I Think Therefore I Blog" project from the Code Institute LMS and modified by the team to produce a booking system using HTML, CSS, Python, PostgreSQL and Django.

