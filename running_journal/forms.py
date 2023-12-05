from flask import Form
from .models import SleepInfo

class SleepForm(Form):
    sleep_date_start = fields.StringField()
    sleep_date_end = fields.StringField()