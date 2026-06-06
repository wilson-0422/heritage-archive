from app import db
from app.models import Exhibition


class ExhibitionService:
    @staticmethod
    def get_exhibitions(status=""):
        query = Exhibition.query
        if status:
            query = query.filter(Exhibition.status == status)
        return query.order_by(Exhibition.id.desc()).all()

    @staticmethod
    def get_exhibition(exhibition_id):
        return Exhibition.query.get(exhibition_id)

    @staticmethod
    def create_exhibition(data):
        exhibition = Exhibition(
            title=data.get("title", ""),
            location=data.get("location", ""),
            start_date=data.get("start_date", ""),
            end_date=data.get("end_date", ""),
            description=data.get("description", ""),
            status=data.get("status", "未开始"),
            capacity=int(data.get("capacity", 100)),
        )
        db.session.add(exhibition)
        db.session.commit()
        return exhibition

    @staticmethod
    def get_reservation_count(exhibition_id):
        from app.models import Reservation
        result = db.session.query(db.func.sum(Reservation.people_count)).filter_by(
            exhibition_id=exhibition_id
        ).scalar()
        return result or 0
