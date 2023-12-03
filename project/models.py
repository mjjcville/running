from project.app import db

class SleepInfo(db.Model):
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
    
def create_tables(meta, engine):
    sleep_info = Table(
        "sleep_info",
        meta,
        Column('id', Integer, primary_key = True),
        Column("sleep_date", DateTime),
        Column("average_hrv", Integer),
        Column("created_at", DateTime),
        Column("updated_at", DateTime)
    )
    weather_info = Table(
        "weather_info",
        meta,
        Column('id', Integer, primary_key = True),
        Column("weather_date", DateTime),
        Column("low_temperature", Integer),
        Column("humidity", Integer),
        Column("wind", Integer),
        Column("created_at", DateTime),
        Column("updated_at", DateTime)
    )

    running_info = Table(
        "running_info",
        meta,
        Column('id', Integer, primary_key = True),
        Column("sleep_date", DateTime),
        Column("avg_pace", String),
        Column("distance", Float),
        Column("created_at", DateTime),
        Column("updated_at", DateTime)
    )
    meta.create_all(engine)
