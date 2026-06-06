from app.routes.main import main_bp
from app.routes.auth import auth_bp
from app.routes.inheritors import inheritors_bp
from app.routes.collections import collections_bp
from app.routes.crafts import crafts_bp
from app.routes.exhibitions import exhibitions_bp
from app.routes.reservations import reservations_bp

__all__ = [
    "main_bp",
    "auth_bp",
    "inheritors_bp",
    "collections_bp",
    "crafts_bp",
    "exhibitions_bp",
    "reservations_bp",
]
