from app import db


class Inheritor(db.Model):
    __tablename__ = "inheritors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    heritage_item = db.Column(db.String(100), nullable=False)
    province = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, default="")
    phone = db.Column(db.String(20), default="")

    collections = db.relationship("Collection", backref="inheritor", lazy="dynamic")
