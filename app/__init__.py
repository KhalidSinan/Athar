from flask import Flask
from .config import Config
from .extensions import db, ma, cors
from .routes.manager_routes import manager_bp
from .routes.member_routes import member_bp
from .routes.skill_routes import skill_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(manager_bp, url_prefix='/api/managers')
    app.register_blueprint(member_bp, url_prefix='/api/members')
    app.register_blueprint(skill_bp, url_prefix='/api/skills')

    return app
