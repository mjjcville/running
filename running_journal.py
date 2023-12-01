from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from os.path import abspath, dirname, isfile, join
from configparser import ConfigParser


import datetime

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


def create_app(config_file=None):
    """
    Default configuration expected at: '<project_root>/config/running_config.cfg'
    Default usage:
        app = create_app()

    Usage with config file:
        app = create_app('/path/to/config.cfg')

    Returns Flask app object.
    Raises EnvironmentError if config_file cannot be found.
    """
    config = ConfigParser()
    if not config_file:
        config.read('./config/running_config.cfg')
    else:
        config.read(config_file)

    # raise error if config_file doesn't exist
    if not isfile(config_file):
        raise EnvironmentError('App config file does not exist at %s' % config_file)
    
    app = Flask(__name__)
    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = config.get('app','db_name')

    # initialize the app with the extension
    db.init_app(app)
    return app

def running_journal():
    return "<p>A New Running Journal App!</p>"


#Models
class SleepInfo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sleep_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    deep_sleep: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    efficiency: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    rem_sleep: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    restfulness: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    timing: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    score: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    average_breath: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    average_heart_rate: Mapped[float] = mapped_column(Float, unique=False, nullable=True)
    average_hrv: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    lowest_heart_rate: Mapped[int] = mapped_column(Integer, unique=False, nullable=True)
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
