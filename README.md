# TripSage
The only Itinerary planner, you will ever need 

[![Build Status](https://travis-ci.com/TripSage/TripSage.svg?branch=master)](https://travis-ci.com/TripSage/TripSage) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4019814.svg)](https://doi.org/10.5281/zenodo.4019814)
[![Maintainability](https://api.codeclimate.com/v1/badges/f04f12b5653d3a7a20ed/maintainability)](https://codeclimate.com/github/TripSage/TripSage/maintainability)![GitHub issues](https://img.shields.io/github/issues-raw/TripSage/TripSage)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/TripSage/TripSage)
![GitHub](https://img.shields.io/github/license/TripSage/TripSage)

See UI Mockups at : [TRIPSAGE](http://xd.adobe.com/view/4b11902d-7907-4938-846e-cf4fd00181af-1e42/)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yO8Xo6UvWUQ/0.jpg)](https://www.youtube.com/watch?v=yO8Xo6UvWUQ)
</br>
</br>
</br>
## Hello! Welcome to TripSage! </br>
### Why TripSage? </br>
Travelling to a new country can be stressful. Couple that with COVID, almost impossible. But the mental health benefits of travelling to new and exciting places doesn’t have to be so risky and expensive. </br>
TripSage is a website that plans trips for users inside their home country. Simply, pick a destination state and cities, and you’ll be directed to your ideal trip. We have plans to include tags for: COVID -19 hotspots, whether the location is indoors, and the general population at that location to make sure users can practice safe travelling.</br>
</br>
A new way of life doesn’t have to mean you can’t travel.</br>
Explore the new of travelling with TripSage.</br>
</br>
### Tools used </br>
We use Django, SQLite3, HTML, CSS, and Javascript. </br>
</br>
### New to Django? </br>
Check out the basics: https://docs.djangoproject.com/en/3.1/intro/tutorial01/ </br>
The first 3 tutorials should be enough to get you started with our project. </br>
</br>
Want a more in-depth look at server-side development? </br>
Check out the basics: https://developer.mozilla.org/en-US/docs/Learn/Server-side </br>
This tutorial also covers Django.</br>
</br>
### How to Run: </br>
Clone the git repository to the desired folder location on your system
Navigate to the folder TripSage. This is the Django project. tripHome is the application for the project. A project can have multiple applications. </br>
Run on the command line: </br>
python manage.py runserver </br>
</br>
### Project Structure:</br>
(Disclaimer: Need some knowledge of Django to understand Project structure, please go through above resources if needed)</br>
TripSage/</br>
&nbsp; tripHome/</br>
&nbsp;&nbsp; models.py </br>
&nbsp;&nbsp; views.py </br>
&nbsp;&nbsp;&nbsp; urls.py </br>
&nbsp;&nbsp;&nbsp; templates/ </br>
&nbsp;&nbsp;&nbsp;&nbsp; index.html </br>
&nbsp;&nbsp;&nbsp;&nbsp; base_generic.html </br>
&nbsp;&nbsp;&nbsp;&nbsp; result.html</br>
&nbsp;&nbsp;&nbsp; static/ </br>
&nbsp;&nbsp;&nbsp;&nbsp; js/ </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; custom.js </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; resultsPage.js </br>
</br>

</br>

### Phase 1 Completed Deliverables

<ul>
  <li>Setup design and architecture of project (Django MVC)</li>
  <li>Implemented call to Google Maps API to retrieve location details.</li>
  <li>Setup Database Models required for the application. </li>
  <li>Designed UI Mockups for the front end of the application.</li>
</ul>

### Phase 2 Planned Deliverables
<ul>
<li>Improve the front-end of the design</li>
 <li>Addition of style checkers for codebase</li>
  <li>Adding Formatting guide and Code coverage to the code</li>
  <li>Implementing core functionalities using the UI Mockups as a reference</li>
</ul>
