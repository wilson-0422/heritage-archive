from app import db
from app.models import CraftStep, Collection


class CraftService:
    @staticmethod
    def get_all_craft_steps():
        return CraftStep.query.order_by(CraftStep.collection_id, CraftStep.step_number).all()

    @staticmethod
    def get_craft_steps_by_collection(collection_id):
        return CraftStep.query.filter_by(collection_id=collection_id).order_by(CraftStep.step_number).all()

    @staticmethod
    def get_craft_step(craft_id):
        return CraftStep.query.get(craft_id)

    @staticmethod
    def create_craft_step(data):
        craft = CraftStep(
            collection_id=int(data.get("collection_id", 0)),
            step_number=int(data.get("step_number", 1)),
            title=data.get("title", ""),
            description=data.get("description", ""),
            duration=data.get("duration", ""),
        )
        db.session.add(craft)
        db.session.commit()
        return craft

    @staticmethod
    def get_collection(collection_id):
        return Collection.query.get(collection_id)
