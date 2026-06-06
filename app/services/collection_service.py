from app import db
from app.models import Collection


class CollectionService:
    @staticmethod
    def get_collections(category=""):
        query = Collection.query
        if category:
            query = query.filter(Collection.category == category)
        return query.order_by(Collection.id.desc()).all()

    @staticmethod
    def get_collection(collection_id):
        return Collection.query.get(collection_id)

    @staticmethod
    def create_collection(data):
        collection = Collection(
            name=data.get("name", ""),
            category=data.get("category", ""),
            inheritor_id=int(data.get("inheritor_id", 0)),
            year=int(data.get("year", 0)) if data.get("year") else None,
            material=data.get("material", ""),
            size=data.get("size", ""),
            description=data.get("description", ""),
        )
        db.session.add(collection)
        db.session.commit()
        return collection

    @staticmethod
    def get_categories():
        results = db.session.query(Collection.category).distinct().all()
        return [r[0] for r in results]

    @staticmethod
    def get_collections_by_inheritor(inheritor_id):
        return Collection.query.filter_by(inheritor_id=inheritor_id).order_by(Collection.id.desc()).all()
