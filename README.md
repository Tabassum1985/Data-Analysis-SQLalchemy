
We have decided to go on a long holiday vacation in Honolulu, Hawaii. To help with trip planning, we decided to do a climate analysis about the area. The following sections outline the steps that will be taken to accomplish this task.

## Part 1: Analyze and Explore the Climate Data

In this section, we will use Python and SQLAlchemy to do a basic climate analysis and data exploration of the climate database. Specifically, we will use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

Note that we will use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete our climate analysis and data exploration.

Use the SQLAlchemy create_engine() function to connect to our SQLite database.

Use the SQLAlchemy automap_base() function to reflect our tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.

# Precipitation Analysis
Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

# Station Analysis
Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

List the stations and observation counts in descending order.

## Part 2: Design the Climate App

Now that we’ve completed the initial analysis, we will design a Flask API based on the queries that have been just developed. To do so, we will use Flask to create routes as follows:

1./

Start at the homepage.

List all the available routes.

2. /api/v1.0/precipitation

Convert the query results from the precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

Return the JSON representation of the dictionary.

3. /api/v1.0/stations

Return a JSON list of stations from the dataset.

4. /api/v1.0/tobs

Query the dates and temperature observations of the most-active station for the previous year of data.

Return a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

