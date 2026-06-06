from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.exhibition_service import ExhibitionService

exhibitions_bp = Blueprint("exhibitions", __name__)


@exhibitions_bp.route("/")
def list_exhibitions():
    status = request.args.get("status", "")
    exhibitions = ExhibitionService.get_exhibitions(status=status)
    return render_template(
        "exhibitions/list.html", exhibitions=exhibitions, current_status=status
    )


@exhibitions_bp.route("/<int:exhibition_id>")
def detail(exhibition_id):
    exhibition = ExhibitionService.get_exhibition(exhibition_id)
    if not exhibition:
        flash("展览不存在", "danger")
        return redirect(url_for("exhibitions.list_exhibitions"))
    reservation_count = ExhibitionService.get_reservation_count(exhibition_id)
    return render_template(
        "exhibitions/detail.html",
        exhibition=exhibition,
        reservation_count=reservation_count,
    )


@exhibitions_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        data = {
            "title": request.form.get("title", ""),
            "location": request.form.get("location", ""),
            "start_date": request.form.get("start_date", ""),
            "end_date": request.form.get("end_date", ""),
            "description": request.form.get("description", ""),
            "status": request.form.get("status", "未开始"),
            "capacity": request.form.get("capacity", 100),
        }
        result = ExhibitionService.create_exhibition(data)
        if result:
            flash("展览创建成功", "success")
            return redirect(url_for("exhibitions.detail", exhibition_id=result.id))
        flash("创建失败", "danger")
    return render_template("exhibitions/create.html")
