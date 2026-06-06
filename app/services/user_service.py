from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User


class UserService:
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            return user
        return None

    @staticmethod
    def create_user(username, password, role="user"):
        if User.query.filter_by(username=username).first():
            return None
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            role=role,
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()
