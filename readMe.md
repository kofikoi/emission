# Emissions Tracking App

## Introduction
This web application tracks CO2 emissions data for various countries around the world. Users can view a list of countries and their total emissions, as well as detailed emissions data for individual countries. The application is built using Python, Django, and Sqlite3.

## Design
The app consists of three main pages:

Home Page - Displays a brief introduction to the app and provides links to the list of countries and the about page.

List of Countries - Displays a table of all the countries in the database along with their total emissions. The table is paginated to display 15 countries per page. Each country name in the table is a link to the country detail page.

Country Detail Page - Displays a table of all the emissions data for a particular country. The table shows the total emissions, as well as emissions by year and by type (coal, oil, gas fuel, cement, gas flaring, other, and per capita). The page includes a back button to return to the list of countries page.

## Development
Clone the repository to your local machine.
Install the necessary requirements with pip install -r requirements.txt.
Run the migrations with python manage.py migrate.
Load the sample data with python manage.py loaddata emissions.json.
Start the development server with python manage.py runserver.

## Usage
To use the app:

Navigate to the home page at http://your-domain.com/.
Click the "List of Countries" link to view the list of countries.
Click on a country name in the table to view the country detail page.
Click the "Back" button on the country detail page to return to the list of countries page.


## Testing
To run the automated test suite:

Ensure that the development server is not running.
Run the tests with python manage.py test.