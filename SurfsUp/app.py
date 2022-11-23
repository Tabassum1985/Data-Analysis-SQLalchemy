import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

 # Create our session (link) from Python to the DB
session = Session(engine)

# Query the last date
results = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Calculate the date 1 year ago from the last data point
query_date = dt.date(2017,8,23) - dt.timedelta(days=365)

session.close()

# Flask Setup

app = Flask(__name__)


# Flask Routes


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Hawaii!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
        
    )

# create precipitation route 
@app.route("/api/v1.0/precipitation")
def precipitation():
     # Create our session (link) from Python to the DB
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    # Convert into a dictionary
    precipitation = []

    for date, prcp in results:
        precip_dict ={}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
      
    precipitation.append(precip_dict)
    print(precipitation)

    return jsonify(precipitation)

# # create station route 
# @app.route("/api/v1.0/stations")
# def stations():

#     stations = session.query(Station.name, Station.station).all()
#     session.close()
#     # convert results to a dict
#     stations_list = []
#     for station, name in stations:
#         dict = {}
#         dict["name"] = name
#         dict["station"] = station
      
#         stations_list.append(dict)

#     # return json list of dict 
#     return jsonify(stations_list)

# # create tobs route
# @app.route("/api/v1.0/tobs")
# def tobs():
#     # create session link
#     session = Session(engine)
    
#     # """Return a JSON list of Temperature Observations (tobs) for the previous year."""
#     #query_date  is "2016-08-23" for the last year query
#     tobs = session.query(Measurement.tobs, Measurement.date).filter(Measurement.date >= query_date).all()

#     session.close()

#     # convert list to dictionary
#     tobs_list = []
#     for date, temperature in tobs:
#         tobs_dict= {}
#         tobs_dict["date"] = date
#         tobs_dict["temprature"] = temperature
#         tobs_list.append(tobs_dict)

#     # jsonify the list
#     return jsonify(tobs_list)

# # create start route

# @app.route("/api/v1.0/min_max_avg/<start>")
# def start(start):
#     # create session link
#     session = Session(engine)

#     """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date."""

#     # convert date to yyyy-mm-dd format
#     start_dt = dt.datetime.strptime(start, '%Y-%m-%d')

#     # query for the start date value
#     results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_dt).all()

#     session.close()

# # Create a list to hold results
# temperature_list = []
# for result in results:
#     result = {}
#     result["StartDate"] = start_dt
#     result["TMIN"] = TMIN
#     result["TAVG"] = TAVG
#     result["TMAX"] = TMAX
#     temperature_list.append(result)

# # jsonify the result
# return jsonify(temperature_list)

# ##################################################################
# #  create end route

# @app.route("/api/v1.0/min_max_avg/<start>/<end>")
# def start_end(start, end):
#     # create session link
#     session = Session(engine)

#     """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start and end dates."""

#     # convert date to yyyy-mm-dd format 
#     start_dt = dt.datetime.strptime(start, '%Y-%m-%d')
#     end_dt = dt.datetime.strptime(end, "%Y-%m-%d")

#     # query data for the start date value
#     results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_dt).filter(Measurement.date <= end_dt)

#     session.close()

#     # Create a list to hold results
#     end_list = []
#     for result in results:
#         end_dict = {}
#         end_dict["StartDate"] = start_dt
#         end_dict["EndDate"] = end_dt
#         end_dict["TMIN"] = result[0]
#         end_dict ["TAVG"] = result[1]
#         end_dict["TMAX"] = result[2]
#         end_list.append(end_dict)
# # jsonify the result
#     return jsonify(end_list)


if __name__ == '__main__':
    app.run(debug=True)
