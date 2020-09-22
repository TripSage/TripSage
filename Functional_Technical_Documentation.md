![](media/image1.png)

![A picture containing drawing Description automatically
generated](media/image5.png){width="1.9582983377077865in"
height="1.9042465004374454in"}

> **Developed by:**
>
> Dhruvil Shah dshah4\@ncsu.edu\
> Neeraj Shukla nshukla2\@ncsu.edu\
> Poorvaja Penmetsa ppenmet\@ncsu.edu\
> Sreemoyee Ray sray9\@ncsu.edu\
> Sameer Adhikari sadhika2\@ncsu.edu

# Table of Contents

## 1.0 General Information

### 1.1 Purpose

### 1.2 Scope

### 1.3 Acronyms/Definitions

### 1.4 Why TripSage

## 2.0 Functional Requirements

### 2.1 Overview

### 2.2 Why Django

### 2.3 Features

### 2.4 Use Cases

## 3.0 Technical Specification

### 3.1 Software

### 3.2 Django Architecture

### 3.3 Description of Models

### 3.4 Description of Functions

### 3.5 Data Models

### 3.6 ER Diagram for the Models

### 3.7 Logical Flow of Control

### 3.8 Code Design Tools

## 4.0 Future improvements: suggestions

### 4.1 What has been Implemented?

4.2 What needs to be done?**

**4.3 Ambitious Suggestions**

**5.0 Appendix and References**

**5.1 Appendix A**

**5.2 Inspirations**

**5.3 Resources**

**1.0 General Information**

**1.1 Purpose: **

The purpose of this document is to provide information about the
TripSage web application to the current and future software developers.
This document explains the high-level technical and functional
requirements of the app. It details the features, design aspects, and
future work on the website for further developments. It is used to
describe this web application's intended capabilities, appearance, and
interactions with users in detail. This also acts as a kind of guideline
and continuing reference point as the developers write the programming
code to extend the application's features.

**1.2 Scope: **

This Functional and Technical Requirements Document outlines the
functional, performance and other system requirements for theTripSage
application. The scope of this work includes the initial features of the
web application. Suggested features that can be added are provided in
section 4.0. Use cases for the suggested features can be found in
section 2.3

Low level technical requirements and implementation details of suggested
features are out of the scope of this document.

**1.2 Acronyms/Definitions**

API: Application Programming Interface, a set of protocols or standards
for communicating with web based applications

CSS3: Cascading Style Sheets; language used to describe the presentation
of a document written in markup language, e.g., HTML

Django: A python based web framework used for development of web
applications

HTML: Hypertext Markup Language (HTML) is the standard markup language
for documents designed to be displayed in a web browser

Javascript: Javascript is a text-based programming language which is
used to make web pages interactive

Ajax: Ajax is a set of web development techniques using many web
technologies on the client side to create asynchronous web applications

Google Geolocation API: It returns a location and accuracy radius based
on information about cell towers and WiFi nodes that the mobile client
can detect

**1.4 Why TripSage**

Travelling to a new country can be stressful. Couple that with COVID,
almost impossible. But the mental health benefits of travelling to new
and exciting places doesn't have to be so risky and expensive.

TripSage is a website that plans trips for users inside their home
country. Simply, pick a destination state and cities, and you'll be
directed to your ideal trip. We have plans to include tags for: COVID
-19 hotspots, whether the location is indoors, and the general
population at that location to make sure users can practice safe
travelling.

A new way of life doesn't have to mean you can't travel.

Explore the new way of travelling with TripSage.

**2.0 Functional Specifications:**

**2.1 Overview**

TripSage is the ultimate itinerary planner to help users in their travel
plans. This application will allow a user to plan their trip according
to their vacation preferences. Whether you are travelling with your
kids, want an adventurous trip with your friends group or want a weekend
to relax and unwind, TripSage will create the perfect itinerary for you.
It will guide the user with the best time to visit their preferred
places, the latest Covid -- 19 updates and the best route to travel, all
while adhering to the user's budget.

The scope of TripSage can be defined using the following functionalities
in a broad sense

-   Users can login to the website

<!-- -->

-   Flow 1:

    -   Accept the inputs \[Appendix-A\] from the user.

    -   Display/suggest places to visit with the tags - 1. Best time to
        > visit, 2. Covid warnings

> 3\. Type of the place (Adventurous, Sightseeing, good for food, sport,
> etc)

-   Users can pick the places to visit from these suggestions and press
    > next.

-   TripSage will generate itineraries using the places users want to
    > visit.

-   Tripsage will suggest the cheapest route to the user

<!-- -->

-   Flow 2:

    -   Accept the inputs \[Appendix-A\] from the user.

    -   From the type of trip the user wants, TripSage generates an
        > itinerary using the places to visit from the destination
        > cities the user is planning to visit.

    -   Tripsage will suggest the cheapest route to the user

**2.2 Why Django?**

Why Django?

> The purpose behind choosing Django was two-fold. We wanted to
> challenge ourselves with this project, but set realistic expectations.
> So, instead of learning a new language for web development, we decided
> to use a Python framework, a language our entire team (and many
> others) are comfortable with.
>
> Also, Django follows MVT(model-view-template) architecture which can
> be used independently making it reliable, flexible and simple.
> Moreover, it has its own server and the learning curve is pretty
> minimum. Compared to Flask, Django is used for applications that serve
> more than just one requirement. We envision and designed TripSage to
> include many features, making Django the better choice.

**2.2 Features**

General set of features designed for TripSage:

1.  User account creation

2.  Saving a trip

3.  Sharing a trip with other users

4.  Type of Trip: Suggestions for places to visit as per user's
    > preferred type of vacation like relaxed, adventurous, travelling
    > with kids.

5.  Travel Dates: Suggestions based on the user's preferred travel dates

6.  Mode of Transportation: Suggestions based on the user\'s preferred
    > transportation mode like flight, car or bus.

7.  Budget: Adjustable budget to suit every user's needs

8.  Route: Suggests the best route for the trip

9.  Best Time to Visit: Suitable months, time of the day

10. Covid -- 19 Statistics:

    a.  Specified as \"High\", \"Medium\", \"Low\" based on the
        > population at the specified location and whether the location
        > is indoors or outdoors.

**2.3 Use Cases**

**Planning a New Trip**

![](media/image3.png){width="6.5in" height="3.564583333333333in"}

**Saving a Trip**

![](media/image9.png){width="6.15625in" height="2.6666666666666665in"}

**Sharing a Trip**

![](media/image6.png){width="6.375in" height="3.1979166666666665in"}

**Editing a Trip**

![](media/image7.png){width="5.635416666666667in"
height="2.6666666666666665in"}

**3.0 Technical Specifications:**

**3.1 Software**

The TripSage application is built with Django, an open source web
application framework, written in Python. The location data displayed in
the itinerary is fetched using Google Geolocation API. Alternatively, in
a different version, data will be stored in a SQLite3, also open source.
The user interface is developed in HTML5, CSS3, JavaScript and Ajax. The
backend is coded in Python. The application is compatible with all web
browsers. The application code uses Git version control, and all commits
will be archived in a designated repository.

**3.2 Django Architecture**

![](media/image4.png){width="6.5in" height="2.073611111111111in"}

TripSage is developed with Django, a high-level Python web application
framework that enables the rapid development of web applications. It
follows the MTV (Model Template View) architecture:

1.  User requests for Django based website

2.  URL calls corresponding function in **views.py** (mapping found in
    > urls.py)

    a.  view can take a request and return a response

    b.  view interacts with Model and Template

3.  Template is combination of static HTML and Django Syntax (Python)

4.  Model is a class representing table/collection in models.py

**3.3 Models**

Following is the list of Models in TripSage and a brief description of
each:

> City: To store cities
>
> Trip: To store the trips generated from the itinerary planner
>
> Places: Locations/spots within cities that will be displayed as part
> of the itinerary
>
> Destinations: The cities that can be destinations
>
> Contains: To store the mapping between Places and Cities
>
> Tags: Different tags which will be used to tag Places
>
> Tagged\_as: To store the mapping between Places and Tags

**3.4 Functions**

***TripSage/***

***tripHome/***

> *[models.py]{.underline}* - Describes tables for database. Each
> function describes a table in the database (check documentation for
> more information)
>
> *[views.py]{.underline}* - A View is a python function or classe that
> takes a request and provides a response.
>
> It can render the HTML pages, call APIs, push and retrieve data from
> tables in the database
>
> *getResponse* -
>
> 1\. Calls Google Geolocation API to fetch locations as per user\'s trip
> preference
>
> 2\. Checks results for duplicates and standard number of places for each
> activity according to the dictionary type\_places\_map
>
> 3\. Stores results in JSON object
>
> *resultsPage* - renders results.html
>
> *index* - renders index.html
>
> *[urls.py]{.underline}* - maps url patterns to functions in views.py
>
> ***templates/***
>
> *[index.html]{.underline}* - extends to base\_generic.html
>
> *[base\_generic.html]{.underline}* - landing page
>
> *[result.html]{.underline}* - results page
>
> ***static/***
>
> ***js/***
>
> *[custom.js]{.underline} -* Functionality for base\_generic.html.
>
> *saveData()* - saves data from landing page and redirects to
> results.html
>
> *[resultsPage.js]{.underline}* - Functionality for results.html.
> Connects results.html to getResponse in views.py
>
> *showData() -* JS for results.html
>
> [ ]{.underline}

**3.5 Entity Relationship Diagram for the Models**

![](media/image10.png){width="6.713542213473316in"
height="6.958333333333333in"}

**3.6 Logical Flow of Control:**

The diagram below shows the flow of control from when a user enters
their trip details on the landing page of tripHome to seeing their
results The bold text signifies start and end states.

*(results,js has been changed to resultsPage.js)*

![](media/image2.jpg){width="6.942708880139983in" height="3.09375in"}

**3.7 Code Design Tools:**

Our team uses VSCode and Pycharm.

[Linter:]{.underline}

VSCode, Pycharm: pylint

[Style Checker:]{.underline}

VSCode, Pycharm: pylint (pep8)

[Code Formatter:]{.underline}

Black

**4.0 Future improvements:**

**4.1 What has been Implemented?**

The TripSage application currently supports the following
functionalities:

Allow user to create a Trip using Flow\#2 where, the user only inputs
the destination city/cities to visit and Type/types of trip along with
the estimated Trip time.

The website uses Google Maps api to fetch the appropriate places for the
given destination along with their ratings and displays the list of
places.

**4.2 What needs to be done?**

The following functionalities have not been implemented yet:

User Login: Update models.py \[Left to acquaint Team 2 about the
database structure\] to include User\[[EmailId]{.underline}, Password\]
and Trips\_Planned\[[EmailId, TripId]{.underline}\]. Implement
authentication page and retrieve Trips saved by User.

Sharing Trips: Allow users to share trips they created with other users.

Implementation of an algorithm to create an itinerary from the places
retrieved using the api. The algorithm will be a Constraint Satisfaction
Problem, constrained by best time to visit a place and the location of a
place. However, details of exact implementation are left for the next
team.

Implementation of functionality using Google Maps \[or any other api
(decision left for next team)\] to determine the cheapest Travel route
based on the destinations and number of people.

Implementation of Trip Creation using Flow\#1, where a user already has
a trip planned to the exact dot, including the places, they want to
visit and only need our assistance to schedule and get the cheapest
travel route.

**4.3 Ambitious Suggestions:**

While showing the suggestions itself, users can remove suggested places,
modifying the itinerary dynamically.

Dynamic computation of Popularity and covid tags based on the no of
trips generated for the particular place on a given date.

**5.0 Future improvements:**

**5.1 Appendix A**

[Inputs from User:]{.underline}

1.  Trip Name

2.  No of people in the trip

3.  Source City

4.  Destination Cities

5.  Start Date

6.  End date

7.  Places to visits \-\-- optional, but have to enter if not entered
    > the "type of the trip"

8.  Type of the trip \-- optional, but have to enter if not entered the
    > list of places to visit

**5.2 Inspirations**

1.  Sygic Travel \[[https://travel.sygic.com/en]{.underline}\] - Tell
    > Sygic where you\'re going and for how many days. Based on that,
    > the app will create a custom itinerary of the top attractions in
    > that place, along with where you should go on which day.

2.  Inspirock
    > \[[[https://www.inspirock.com]{.underline}](https://www.inspirock.com)\] -
    > A very close Itinerary planner with suggestion algorithm inbuilt
    > into the website, with the only feature missing is the ability to
    > suggest a cheapest route.

**5.3 Resources**

1.  Django

> Check out the basics: [[Writing your first Django app, part
> 1]{.underline}](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
>
> The first three parts of this 7 part tutorial cover most of the
> material needed for our project.
>
> For a more in-depth look at server-side development using Django:
> [[Server-side website programming - Learn web development \|
> MDN]{.underline}](https://developer.mozilla.org/en-US/docs/Learn/Server-side)

2.  AJAX

> Check out the basics of ajax at
> [[https://api.jquery.com/jquery.ajax/]{.underline}](https://api.jquery.com/jquery.ajax/).
> The site covers all the basics of ajax about writing asynchronous
> calls and provides in depth information about its parameters.
>
> For ajax documentation, please visit
> [[https://api.jquery.com/category/ajax/]{.underline}](https://api.jquery.com/category/ajax/)

3.  Google Map API
