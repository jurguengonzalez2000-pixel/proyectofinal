from flask import Flask
from app.extensions import db, jwt

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)
    jwt.init_app(app)

    from app.citas.routes import citas_bp

    app.register_blueprint(citas_bp, url_prefix='/citas')

    with app.app_context():
        db.create_all()

    return app