from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.services.craft_service import CraftService

crafts_bp = Blueprint("crafts", __name__)


@crafts_bp.route("/")
def list_crafts():
    collection_id = request.args.get("collection_id", 0, type=int)
    if collection_id:
        crafts = CraftService.get_craft_steps_by_collection(collection_id)
        collection = CraftService.get_collection(collection_id)
    else:
        crafts = CraftService.get_all_craft_steps()
        collection = None
    return render_template(
        "crafts/list.html", crafts=crafts, collection=collection, collection_id=collection_id
    )


@crafts_bp.route("/<int:craft_id>")
def detail(craft_id):
    craft = CraftService.get_craft_step(craft_id)
    if not craft:
        flash("工艺步骤不存在", "danger")
        return redirect(url_for("crafts.list_crafts"))
    return render_template("crafts/detail.html", craft=craft)


@crafts_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        data = {
            "collection_id": request.form.get("collection_id", 0),
            "step_number": request.form.get("step_number", 1),
            "title": request.form.get("title", ""),
            "description": request.form.get("description", ""),
            "duration": request.form.get("duration", ""),
        }
        result = CraftService.create_craft_step(data)
        if result:
            flash("工艺步骤添加成功", "success")
            return redirect(url_for("crafts.list_crafts", collection_id=data["collection_id"]))
        flash("添加失败", "danger")
    from app.services.collection_service import CollectionService
    collections = CollectionService.get_collections()
    pre_collection_id = request.args.get("collection_id", 0, type=int)
    return render_template("crafts/create.html", collections=collections, pre_collection_id=pre_collection_id)
