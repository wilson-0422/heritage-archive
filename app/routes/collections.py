from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.collection_service import CollectionService

collections_bp = Blueprint("collections", __name__)


@collections_bp.route("/")
def list_collections():
    category = request.args.get("category", "")
    collections = CollectionService.get_collections(category=category)
    categories = CollectionService.get_categories()
    return render_template(
        "collections/list.html",
        collections=collections,
        categories=categories,
        current_category=category,
    )


@collections_bp.route("/<int:collection_id>")
def detail(collection_id):
    collection = CollectionService.get_collection(collection_id)
    if not collection:
        flash("藏品不存在", "danger")
        return redirect(url_for("collections.list_collections"))
    return render_template("collections/detail.html", collection=collection)


@collections_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        data = {
            "name": request.form.get("name", ""),
            "category": request.form.get("category", ""),
            "inheritor_id": request.form.get("inheritor_id", 0),
            "year": request.form.get("year", 0),
            "material": request.form.get("material", ""),
            "size": request.form.get("size", ""),
            "description": request.form.get("description", ""),
        }
        result = CollectionService.create_collection(data)
        if result:
            flash("藏品添加成功", "success")
            return redirect(url_for("collections.detail", collection_id=result.id))
        flash("添加失败", "danger")
    from app.services.inheritor_service import InheritorService
    inheritors = InheritorService.get_inheritors()
    return render_template("collections/create.html", inheritors=inheritors)
