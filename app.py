
import os 

from flask import Flask, jsonify

app = Flask(__name__)

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
measure= inspect(engine)
measure.get_table_names()
station = Base.classes.station
stat= inspect(engine)
stat.get_table_names()
high = [0][0]

@app.route("/api/v1.0/precipitation")
def percipitation():
    data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= "2017-08-23").\
    order_by(measurement.date).all()
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
   results = session.query(station.station).all()
   names = list(np.ravel(results))
   return jsonify(names)

@app.route("/api/v1.0/tobs")
def tobs():
    most = session.query(measurement.station, measurement.tobs).filter(measurement.station == high).\
    filter(measurement.date >= "2017-08-23").all()
    return jsonify(most)

@app.route("/api/v1.0/<start>")
def start(start):
    start1 = start.replace(" ", " ")
    all = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.date >= "2010-01-01").all()
    new = list(np.ravel(all))
    return jsonify(new)

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    new_start = start.replace(" ", "")
    new_end = end.replace(" ", "")
    results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
    filter(measurement.date >= "2010-01-01").\
    filter(measurement.date <= "2017-08-23").all()
    new_data = list(np.ravel(results))
    return jsonify(new_data)

if __name__ == "__main__":
    app.run(debug=True)