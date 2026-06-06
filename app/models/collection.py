from app import db


class Collection(db.Model):
    __tablename__ = "collections"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    inheritor_id = db.Column(db.Integer, db.ForeignKey("inheritors.id"), nullable=False)
    year = db.Column(db.Integer)
    material = db.Column(db.String(200), default="")
    size = db.Column(db.String(100), default="")
    description = db.Column(db.Text, default="")

    craft_steps = db.relationship("CraftStep", backref="collection", lazy="dynamic",
                                  order_by="CraftStep.step_number")
