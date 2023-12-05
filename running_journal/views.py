from flask import Blueprint, flash, Markup, redirect, render_template, url_for

from .forms import SleepForm
from .models import db


tracking = Blueprint("running", __name__)


@tracking.route("/")
def index():
    sleep_form = SleepForm()
    return render_template("index.html", sleep_form=sleep_form,)


# @tracking.route("/sleep", methods=("GET", ))
# def sleep():
#     sleep_form = SleepForm()
#     result = find_sleep_data("2023-11-20", "2023-11-30")
#     return render_template("sleep.html", data=result)

