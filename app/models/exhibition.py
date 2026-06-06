from app import db


class Exhibition(db.Model):
    __tablename__ = "exhibitions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
    end_date = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, default="")
    status = db.Column(db.String(20), default="未开始")
    capacity = db.Column(db.Integer, default=100)

    reservations = db.relationship("Reservation", backref="exhibition", lazy="dynamic")
