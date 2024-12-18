# Haircut Hysteria Hackathon

<img src=static/images/readme/responsive_mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

The deployed site can be found [here]().

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

<img src=static/images/readme/planning/capstone_miro_board.jpg image alt="Screenshot of project Miro board" width="600" height="300">

<br>

Initially the project was planned out using a Miro board to start to brainstorm some ideas, concepts and content.

[View Miro board](https://miro.com/app/board/uXjVLA4YJ9I=/?share_link_id=560098034555)

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

<img src=static/images/readme/agile/capstone_project_board.png alt="Screenshot of GitHub project board" width="600" height="300">

<br>

The completed sprint was composed of X separate items. Having used the MoSCoW approach to prioritisation, X were classified as "Must-Have", X as "Should-Have" and "Could-Have". The rest of the first sprint was made up of "Won't-Have" items and remain in the backlog.

Full [Project Board](https://github.com/users/els-390/projects/9).

## Flowchart & ERD

<img src=static/images/readme/planning/flowchart.png image alt="Flowchart for the application functions and features" width="600" height="">

<br>

A flowchart to show the potential flow of users across the application and to help understand potential issues and the best approach to planning the project and future iterations.

<br>

The ERD (Entity Relationship Diagram) shows all relationships for the models used within the project including the custom Reviews model. 


<img src=static/images/readme/erd/ERD.png image alt="ERD diagram" width="600" height="300">

## Design Decisions & UX

Many different wireframes were produced to help plan the project including for desktop, tablet and mobile devices.

Initially the project was planned to have multiple sections to the homepage but this was scaled back for the first iteration due to time constraints so further sections will be added in future to make the homepage more informative and link to other areas of the applications.

### Desktop

<img src=static/images/readme/wireframes/desktop_homepage_wireframes.png image alt="desktop wireframe for homepage" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_project_detail_1_wireframes.png image alt="desktop wireframe for project detail page showing project info" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_project_detail_2_wireframes.png image alt="desktop wireframe for project detail page showing comments" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_about_wireframes.png image alt="desktop wireframe for about page" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/desktop_contact_wireframes.png image alt="desktop wireframe for contact page" width="600" height="300">

<br>

### Tablet

<img src=static/images/readme/wireframes/tablet_wireframes_1.png image alt="tablet wireframes for all pages" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/tablet_wireframes_2.png image alt="tablet wireframes for all pages" width="600" height="300">

<br>

### Mobile

<img src=static/images/readme/wireframes/mobile_wireframes_1.png image alt="mobile wireframes for all pages" width="600" height="300">

<br>

<img src=static/images/readme/wireframes/mobile_wireframes_2.png image alt="mobile wireframes for all pages" width="600" height="300">

<br>

### Typography

[Google Fonts](www.googlefonts.com)

<img src=static/images/readme/design/fonts.png image alt="Alt text" width="600">

<br>

### Colours and Images

<img src=static/images/readme/design/colour_pallette.png image alt="Alt text" width="600">

<br>

### Images & Icons

### Accessibility

<img src=static/images/readme/responsive_mockup.png alt="A screenshot showing the project on multiple devices" width="600" height="300">

<br>

### Accessibility Considerations

## Features

<br>

**Home Page**

The Home page of the site shows a selection of projects available to select to view more information or navigate to the next page to see more projects.

**Navigation Bar**

The navigation bar is fully responsive and provides links for the Home, About, Reviews and Contact page.

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

<img src=static/images/readme/validation/css.png alt="css validation screenshot">

<hr>

- Javascript

<img src=static/images/readme/validation/comments_js.png alt="JS Hint for comments.js">

<br>

<img src=static/images/readme/validation/reviews_js.png alt="JS Hint for reviews.js">

### Bugs

## AI

<img src=static/images/readme/ai/chatgpt.png alt="Screenshot from use of ChatGPT">

<br>

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

### Final Thoughts

### Future Improvements & Iterations

## Credits

- This project is based on the "I Think Therefore I Blog" project from the Code Institute LMS
- Help received to troubleshoot various issues during the project from Coding Coach team at Code Institute and Headforwards Bootcamp cohort

