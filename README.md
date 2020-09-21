# TripSage
The only Itinerary planner, you will ever need

[![Build Status](https://travis-ci.com/TripSage/TripSage.svg?branch=master)](https://travis-ci.com/TripSage/TripSage) 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4019814.svg)](https://doi.org/10.5281/zenodo.4019814)
![GitHub issues](https://img.shields.io/github/issues-raw/TripSage/TripSage)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/TripSage/TripSage)
![GitHub](https://img.shields.io/github/license/TripSage/TripSage)
![](http://estruyf-github.azurewebsites.net/api/VisitorHit?user=estruyf&repo=github-visitors-badge&countColorcountColor&countColor=%237B1E7A)

[<img src = "https://github.com/TripSage/TripSage/blob/master/Assets/TripSage%20Playable.png">](https://youtu.be/N0GYVmutWzM)
</br>
</br>
</br>
## Hello! Welcome to TripSage! </br>
### We use Django, Ajax, SQLite3, HTML, CSS, and Javascript. </br>
</br>
## New to Django? </br>
Check out the basics: https://docs.djangoproject.com/en/3.1/intro/tutorial01/ </br>
The first 3 tutorials should be enough to get you started with our project. </br>
</br>
Want a more in-depth look at server-side development? </br>
Check out the basics: https://developer.mozilla.org/en-US/docs/Learn/Server-side </br>
This tutorial also covers Django.</br>
</br>
## How to Run: </br>
Clone the git repository to the desired folder location on your system
Navigate to the folder TripSage. This is the Django project. tripHome is the application for the project. A project can have multiple applications. </br>
Run on the command line: </br>
python manage.py runserver </br>
</br>
## Project Structure:</br>
(Disclaimer: Need some knowledge of Django to understand Project structure, please go through above resources if needed)</br>
TripSage/</br>
&nbsp; tripHome/</br>
&nbsp;&nbsp; models.py - Describes tables for database</br>
&nbsp;&nbsp;&nbsp; Each function describes a table in the database (check documentation for more information)</br>
&nbsp;&nbsp; views.py - A View is a python function or classe that takes a request and provides a response.</br> It can render the HTML pages, call APIs, push and retrieve data from tables in the database </br>
&nbsp;&nbsp;&nbsp; getResponse - </br>
&nbsp;&nbsp;&nbsp;&nbsp; 1. Calls Google Geolocation API to fetch locations as per user's trip preference</br>
&nbsp;&nbsp;&nbsp;&nbsp; 2. Checks results for duplicates and standard number of places for each activity according to the dictionary type_places_map </br>
&nbsp;&nbsp;&nbsp;&nbsp; 3. Stores results in JSON object </br>
&nbsp;&nbsp;&nbsp; resultsPage - renders results.html </br>
&nbsp;&nbsp;&nbsp; index - renders index.html </br>
&nbsp;&nbsp;&nbsp; urls.py - maps url patterns to functions in views.py </br>
&nbsp;&nbsp;&nbsp; templates/ </br>
&nbsp;&nbsp;&nbsp;&nbsp; index.html - extends to base_generic.html </br>
&nbsp;&nbsp;&nbsp;&nbsp; base_generic.html - landing page </br>
&nbsp;&nbsp;&nbsp;&nbsp; result.html - results page </br>
&nbsp;&nbsp;&nbsp; static/ </br>
&nbsp;&nbsp;&nbsp;&nbsp; js/ </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; custom.js </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; saveData() - saves data from landing page and redirects to results.html </br>
</br>
</br>
## Inspirations: </br>
1. Sygic Travel </br>
&nbsp; This travel website creates a personalized itinerary when users give information about where they are going for the number of days they plan for by creating a custom itinerary of the top attractions in that place, along with where they should go on which day. The app clubs nearby attractions together, along with timings of nearby attractions.

</br>
## Group:

1. [Dhruvil Shah](mailto:dshah4@ncsu.edu) (dshah4)<br>
2. [Neeraj Shukla](mailto:nshukla2@ncsu.edu) (nshukla2)<br>
3. [Poorvaja Penmetsa](mailto:ppenmet@ncsu.edu) (ppenmet)<br>
4. [Sreemoyee Ray](mailto:sray9@ncsu.edu) (sray9)<br>
5. [Sameer Adhikari](mailto:sadhika2@ncsu.edu) (sadhika2)<br>
