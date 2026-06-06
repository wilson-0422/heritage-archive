from flask import Blueprint, render_template
from app.models import Inheritor, Collection, Exhibition, Reservation

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    inheritor_count = Inheritor.query.count()
    collection_count = Collection.query.count()
    exhibition_count = Exhibition.query.count()
    reservation_count = Reservation.query.count()
    recent_exhibitions = Exhibition.query.order_by(Exhibition.id.desc()).limit(5).all()
    recent_collections = Collection.query.order_by(Collection.id.desc()).limit(6).all()
    return render_template(
        "index.html",
        inheritor_count=inheritor_count,
        collection_count=collection_count,
        exhibition_count=exhibition_count,
        reservation_count=reservation_count,
        recent_exhibitions=recent_exhibitions,
        recent_collections=recent_collections,
    )


@main_bp.route("/dashboard")
def dashboard():
    inheritor_count = Inheritor.query.count()
    collection_count = Collection.query.count()
    exhibition_count = Exhibition.query.count()
    reservation_count = Reservation.query.count()
    active_exhibitions = Exhibition.query.filter_by(status="进行中").count()
    pending_exhibitions = Exhibition.query.filter_by(status="未开始").count()
    return render_template(
        "dashboard/overview.html",
        inheritor_count=inheritor_count,
        collection_count=collection_count,
        exhibition_count=exhibition_count,
        reservation_count=reservation_count,
        active_exhibitions=active_exhibitions,
        pending_exhibitions=pending_exhibitions,
    )
