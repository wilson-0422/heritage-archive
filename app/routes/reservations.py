from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.services.reservation_service import ReservationService
from app.services.exhibition_service import ExhibitionService

reservations_bp = Blueprint("reservations", __name__)


@reservations_bp.route("/")
@login_required
def list_reservations():
    reservations = ReservationService.get_reservations_by_user(current_user.id)
    return render_template("reservations/list.html", reservations=reservations)


@reservations_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    exhibition_id = request.args.get("exhibition_id", 0, type=int)
    if request.method == "POST":
        data = {
            "exhibition_id": request.form.get("exhibition_id", 0),
            "user_id": current_user.id,
            "name": request.form.get("name", ""),
            "phone": request.form.get("phone", ""),
            "people_count": request.form.get("people_count", 1),
            "visit_date": request.form.get("visit_date", ""),
            "note": request.form.get("note", ""),
        }
        result = ReservationService.create_reservation(data)
        if result:
            flash("预约成功", "success")
            return redirect(url_for("reservations.list_reservations"))
        flash("预约失败，请检查信息是否正确", "danger")
    exhibitions = ExhibitionService.get_exhibitions(status="进行中")
    return render_template(
        "reservations/create.html",
        exhibitions=exhibitions,
        pre_exhibition_id=exhibition_id,
    )
