from flask import Flask
from .config import Config
from .extensions import db, ma, cors
from .routes.manager_routes import manager_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(manager_bp, url_prefix='/api/managers')

    return app
