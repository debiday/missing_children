
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/debiday/The_Lost_Children">
    <img src="static/images/logo1.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">The Lost Children</h3>

  <p align="center">
    This project visualizes data of children who went missing at 18 years or younger from 2007 to 2021.
    <br />
    <br />
    <br />
    <a href="https://github.com/debiday/The_Lost_Children">View Demo</a>
    ·
    <a href="https://github.com/debiday/The_Lost_Children/issues">Report Bug</a>
    ·
    <a href="https://github.com/debiday/The_Lost_Children/issues">Request Feature</a>
    ·
    <a href="https://debiday.wordpress.com">Process Blog</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

![Front-page](https://github.com/Debiday/The_Lost_Children/blob/master/static/images/front-page.gif)


This project visualizes the record of children who went missing when they were 18 years or younger from 2007 to 2021. The data is generated from the [NAMUS-National Missing and Unidentified Persons System](https://www.namus.gov/) with the search criteria set to search for historical records of all missing children in the US including all 52 states. 

The data is supplemented with geolocation data converted by [Geocodio](https://www.geocod.io/docs/#introduction), integrated into a Mapbox tileset and visualized with [Mapbox studio](https://docs.mapbox.com/api/overview/). The same dataset is used to generate the Age to Year Missing Graph with Gender colour legends and built with React and D3. 

Information from the [NCMEC](https://www.missingkids.org/footer/media/keyfacts#:~:text=According%20to%20the%20FBI%2C%20in,represents%20reports%20of%20missing%20children.) is used to supplement the information on both the map and graph by showing categories of children who are missing. 

To sign up as a web sleuth, users log into the app with their email and password. Users are then able to perform advanced searches through the database. Search result data is retrieved from the backend asynchronously with AJAX. With the generated results, users are able to securely add notes, save, update and delete their searches with sessions.

![Tracking-page](https://github.com/Debiday/The_Lost_Children/blob/master/static/images/tracking-page.gif)

### Built With

* Python
* Javascript
* React
* Flask
* Jinja
* SQLalchemy
* postgreSQL

APIs
* [Mapbox](https://docs.mapbox.com/api/overview/)
* [Geocodio] (https://www.geocod.io/docs/#introduction)
* [Google Charts](https://developers.google.com/chart/image/docs/making_charts)

Front-end
* Javascript
* React
* JQuery
* AJAX
* Bootstrap
* HTML/ CSS


<!-- ROADMAP -->
## Roadmap
### MVP
Working map showing first names of missing children mapped to state and city. 

### 1.0 (Current)
Increasing awareness by providing input form for users to generate a list of missing children who are currently at their age. A number of visualizations with graphs and figures.

### 2.0 (Current)
Buttons for subscribing to [Missing Children's Network](https://www.missingchildrensnetwork.ngo/) and volunteering opportunities. A search bar for users to search for entries based on state and city. An account page to store user's saved searches and notes.

### 3.0
A community forum for web sleuths to compare notes, web scraping to get latest cases to the database, and secure login features. 

<!-- USAGE EXAMPLES -->
## Usage

You may like to use the data or view the data behind the visualizations which was accessed from [NAMUS](https://www.namus.gov/)-The National Missing and Unidentified Persons System on the 3rd of April 2021, and supplemented with GPS co-ordinates. 

(As of April 10, the future availabilty of this data [remains undercertain](https://www.kxan.com/investigations/the-future-of-a-national-missing-persons-database-uncertain/) due to funding cuts by the [National Institute of Justice](https://nij.ojp.gov/).)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/debiday/The_Lost_Children.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```

<!-- CONTACT -->
## Contact

Deborah Ong - [@debieday](https://twitter.com/debieday) - Deborah.oyt@gmail.com

Project Link: [https://github.com/debiday/The_Lost_Children](https://github.com/debiday/The_Lost_Children)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [NAMUS Database](https://www.namus.gov/)
* [NCMEC- National Centre for Missing and Exploited Children](https://www.missingkids.org/HOME)
* [Hackbright Academy](https://hackbrightacademy.com/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/debiday