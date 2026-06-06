from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.inheritor_service import InheritorService

inheritors_bp = Blueprint("inheritors", __name__)


@inheritors_bp.route("/")
def list_inheritors():
    category = request.args.get("category", "")
    keyword = request.args.get("keyword", "")
    inheritors = InheritorService.get_inheritors(category=category, keyword=keyword)
    categories = InheritorService.get_categories()
    return render_template(
        "inheritors/list.html",
        inheritors=inheritors,
        categories=categories,
        current_category=category,
        keyword=keyword,
    )


@inheritors_bp.route("/<int:inheritor_id>")
def detail(inheritor_id):
    inheritor = InheritorService.get_inheritor(inheritor_id)
    if not inheritor:
        flash("传承人不存在", "danger")
        return redirect(url_for("inheritors.list_inheritors"))
    return render_template("inheritors/detail.html", inheritor=inheritor)


@inheritors_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        data = {
            "name": request.form.get("name", ""),
            "gender": request.form.get("gender", ""),
            "birth_year": request.form.get("birth_year", 0),
            "category": request.form.get("category", ""),
            "heritage_item": request.form.get("heritage_item", ""),
            "province": request.form.get("province", ""),
            "city": request.form.get("city", ""),
            "description": request.form.get("description", ""),
            "phone": request.form.get("phone", ""),
        }
        result = InheritorService.create_inheritor(data)
        if result:
            flash("传承人信息添加成功", "success")
            return redirect(url_for("inheritors.detail", inheritor_id=result.id))
        flash("添加失败", "danger")
    return render_template("inheritors/create.html")


@inheritors_bp.route("/<int:inheritor_id>/edit", methods=["GET", "POST"])
@login_required
def edit(inheritor_id):
    inheritor = InheritorService.get_inheritor(inheritor_id)
    if not inheritor:
        flash("传承人不存在", "danger")
        return redirect(url_for("inheritors.list_inheritors"))
    if request.method == "POST":
        data = {
            "name": request.form.get("name", ""),
            "gender": request.form.get("gender", ""),
            "birth_year": request.form.get("birth_year", 0),
            "category": request.form.get("category", ""),
            "heritage_item": request.form.get("heritage_item", ""),
            "province": request.form.get("province", ""),
            "city": request.form.get("city", ""),
            "description": request.form.get("description", ""),
            "phone": request.form.get("phone", ""),
        }
        result = InheritorService.update_inheritor(inheritor_id, data)
        if result:
            flash("传承人信息更新成功", "success")
            return redirect(url_for("inheritors.detail", inheritor_id=inheritor_id))
        flash("更新失败", "danger")
    return render_template("inheritors/edit.html", inheritor=inheritor)
