# Import  dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Calculate the date one year from the last date in data set.
def year_before_date(most_recent_date):
    
    most_recent_date = most_recent_date.date 
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d').date() 
    one_year_before = most_recent_date - dt.timedelta(days=365)

    return one_year_before
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query last 12 months of precipitation
    most_recent_date = session.query(Measurement.date).\
        order_by((Measurement.date).desc()).first()

    # Calculate the date one year from the last date in data set.
    one_year_before = year_before_date(most_recent_date)

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_before).all()   

    session.close()

    # Convert list of tuples into normal list 
    precip_dict = {}
    for date, prcp in results:
        precip_dict[date] = prcp

    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query last 12 months of precipitation
    most_recent_date = session.query(Measurement.date).\
        order_by((Measurement.date).desc()).first()

    # Calculate the date one year from the last date in data set.
    one_year_before = year_before_date(most_recent_date)

    # Query all most active station data
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_before).\
        filter(Measurement.station == 'USC00519281').all()

    session.close()

    # Convert list of tuples into normal list 
    all_results = list(np.ravel(results))

    return jsonify(all_results)

@app.route("/api/v1.0/<start>")
def start(start):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert start string to a date object
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()

    # Query for lowest, highest, and average temperature
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    session.close()

    # Convert list of tuples into normal list 
    all_results = list(np.ravel(results))

    return jsonify(all_results)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert start string to a date object
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()

    # Query for lowest, highest, and average temperature
    results = session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)).\
        filter((Measurement.date >= start_date) & (Measurement.date <= end_date)).all()

    session.close()

    # Convert list of tuples into normal list 
    all_results = list(np.ravel(results))

    return jsonify(all_results)

if __name__ == '__main__':
    app.run(debug=True)
