from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from configparser import ConfigParser
from sqlalchemy import Table, Date, DateTime, Column, Float, Integer, String, MetaData
from .sleep import find_sleep_data

config = ConfigParser()
config.read('./config/running_config.cfg')
SQLALCHEMY_DATABASE_URI = config.get('app','db_name')
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)
# init sqlalchemy
db = SQLAlchemy(app)

from project import models

@app.route("/")
def index():
    print ("in the index")
    return  render_template("index.html")  

@app.route("/sleep")
def sleep():
    print ("sleep module")
    result = find_sleep_data("2023-11-28", "2023-11-30")
    return render_template("sleep.html", data=result)

@app.route("/running")
def running():
    return "<p>Checking the running</p>"


if __name__ == "__main__":
    app.run()
