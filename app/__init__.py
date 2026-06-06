from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.inheritors import inheritors_bp
    from app.routes.collections import collections_bp
    from app.routes.crafts import crafts_bp
    from app.routes.exhibitions import exhibitions_bp
    from app.routes.reservations import reservations_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(inheritors_bp, url_prefix="/inheritors")
    app.register_blueprint(collections_bp, url_prefix="/collections")
    app.register_blueprint(crafts_bp, url_prefix="/crafts")
    app.register_blueprint(exhibitions_bp, url_prefix="/exhibitions")
    app.register_blueprint(reservations_bp, url_prefix="/reservations")

    return app
