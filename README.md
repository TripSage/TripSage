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
Navigate to the folder TripSage, this is the Django project. </br>
Run on the command line: </br>
python manage.py runserver </br>
</br>
## Project Structure:</br>
(Disclaimer: Need some knowledge of Django to understand Project structure, please go through above resources if needed)</br>
TripSage/</br>
  tripHome/</br>
    models.py - Describes tables for database</br>
      Each function describes a table in the database (check documentation for more information)</br>
    views.py - Render the pages, call APIs, send information back to the database </br>
			getResponse - </br>
        1. Calls API </br>
        2. Checks results for duplicates and standard number of places for each activity according to the dictionary type_places_map </br>
        3. Stores results in JSON object </br>
    </br>
		resultsPage - renders results.html </br>
		index - renders index.html </br>
		urls.py - maps url patterns to functions in views.py </br>
		templates/ </br>
			index.html - extends to base_generic.html </br>
			base_generic.html - landing page </br>
			result.html - results page </br>
		static/ </br>
			js/ </br>
				custom.js </br>
          saveData() - saves data from landing page and redirects to results.html </br>
</br>
</br>
## Inspirations: </br>
1. Sygic Travel </br>
This travel website creates a personalized itinerary when users give information about where they are going for the number of days they plan for by creating a custom itinerary of the top attractions in that place, along with where they should go on which day. The app clubs nearby attractions together, along with timings of nearby attractions.

</br>
## Group:

1. [Dhruvil Shah](mailto:dshah4@ncsu.edu) (dshah4)<br>
2. [Neeraj Shukla](mailto:nshukla2@ncsu.edu) (nshukla2)<br>
3. [Poorvaja Penmetsa](mailto:ppenmet@ncsu.edu) (ppenmet)<br>
4. [Sreemoyee Ray](mailto:sray9@ncsu.edu) (sray9)<br>
5. [Sameer Adhikari](mailto:sadhika2@ncsu.edu) (sadhika2)<br>
