from flask import Blueprint, flash, Markup, redirect, render_template, url_for
import sleep

tracking = Blueprint("running", __name__)


@tracking.route("/")
def index():
    return render_template("index.html")


@tracking.route("/sleep", methods=("GET", ))
def sleep():
    result = find_sleep_data("2023-11-20", "2023-11-30")
    return render_template("sleep.html", data=result)

