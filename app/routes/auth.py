from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.services.user_service import UserService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = UserService.authenticate(username, password)
        if user:
            login_user(user)
            flash("登录成功", "success")
            next_page = request.args.get("next", url_for("main.index"))
            return redirect(next_page)
        flash("用户名或密码错误", "danger")
    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        if password != confirm_password:
            flash("两次密码输入不一致", "danger")
            return render_template("auth/register.html")
        result = UserService.create_user(username, password)
        if result:
            flash("注册成功，请登录", "success")
            return redirect(url_for("auth.login"))
        flash("用户名已存在", "danger")
    return render_template("auth/register.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("已退出登录", "info")
    return redirect(url_for("main.index"))
