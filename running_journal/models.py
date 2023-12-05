from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SleepInfo(db.Model):
    __tablename__ = 'sleep_info'

    id = db.Column(db.Integer, primary_key=True)
    sleep_date = db.Column(db.String, nullable=False)
    average_hrv = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, sleep_date, average_hrv):
        self.sleep_date = sleep_date
        self.average_hrv = average_hrv

    def __repr__(self):
        return f"<sleep_date {self.sleepdate}>"
    