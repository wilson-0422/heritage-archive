from app import db
from app.models import Inheritor


class InheritorService:
    @staticmethod
    def get_inheritors(category="", keyword=""):
        query = Inheritor.query
        if category:
            query = query.filter_by(category=category)
        if keyword:
            query = query.filter(
                db.or_(
                    Inheritor.name.contains(keyword),
                    Inheritor.heritage_item.contains(keyword),
                    Inheritor.city.contains(keyword),
                )
            )
        return query.order_by(Inheritor.id.desc()).all()

    @staticmethod
    def get_inheritor(inheritor_id):
        return Inheritor.query.get(inheritor_id)

    @staticmethod
    def create_inheritor(data):
        inheritor = Inheritor(
            name=data.get("name", ""),
            gender=data.get("gender", ""),
            birth_year=int(data.get("birth_year", 0)),
            category=data.get("category", ""),
            heritage_item=data.get("heritage_item", ""),
            province=data.get("province", ""),
            city=data.get("city", ""),
            description=data.get("description", ""),
            phone=data.get("phone", ""),
        )
        db.session.add(inheritor)
        db.session.commit()
        return inheritor

    @staticmethod
    def update_inheritor(inheritor_id, data):
        inheritor = Inheritor.query.get(inheritor_id)
        if not inheritor:
            return None
        inheritor.name = data.get("name", inheritor.name)
        inheritor.gender = data.get("gender", inheritor.gender)
        inheritor.birth_year = int(data.get("birth_year", inheritor.birth_year))
        inheritor.category = data.get("category", inheritor.category)
        inheritor.heritage_item = data.get("heritage_item", inheritor.heritage_item)
        inheritor.province = data.get("province", inheritor.province)
        inheritor.city = data.get("city", inheritor.city)
        inheritor.description = data.get("description", inheritor.description)
        inheritor.phone = data.get("phone", inheritor.phone)
        db.session.commit()
        return inheritor

    @staticmethod
    def get_categories():
        results = db.session.query(Inheritor.category).distinct().all()
        return [r[0] for r in results]
