from app import db
from app.models import Reservation, Exhibition


class ReservationService:
    @staticmethod
    def get_reservations_by_user(user_id):
        return Reservation.query.filter_by(user_id=user_id).order_by(Reservation.id.desc()).all()

    @staticmethod
    def create_reservation(data):
        exhibition_id = int(data.get("exhibition_id", 0))
        exhibition = Exhibition.query.get(exhibition_id)
        if not exhibition:
            return None

        people_count = int(data.get("people_count", 1))
        current_count = ExhibitionService.get_reservation_count(exhibition_id)
        if current_count + people_count > exhibition.capacity:
            return None

        reservation = Reservation(
            exhibition_id=exhibition_id,
            user_id=int(data.get("user_id", 0)),
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            people_count=people_count,
            visit_date=data.get("visit_date", ""),
            note=data.get("note", ""),
        )
        db.session.add(reservation)
        db.session.commit()
        return reservation

    @staticmethod
    def get_reservation(reservation_id):
        return Reservation.query.get(reservation_id)

    @staticmethod
    def delete_reservation(reservation_id):
        reservation = Reservation.query.get(reservation_id)
        if reservation:
            db.session.delete(reservation)
            db.session.commit()
            return True
        return False


from app.services.exhibition_service import ExhibitionService
