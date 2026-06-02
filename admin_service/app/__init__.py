
from flask import Flask
from app.extensions import db, jwt
from datetime import timedelta 
from app.models.usuario import Usuario 

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    
    db.init_app(app)
    jwt.init_app(app)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .admin.routes import admin_bp
    app.register_blueprint(admin_bp, url_prefix="/admin")
    with app.app_context():
        db.create_all()
        
        admin = Usuario.query.filter_by(username="admin").first()
        if not admin:
            admin = Usuario(
                username="admin",
                password="1234",
                rol="admin"
            )
            db.session.add(admin)
            db.session.commit()
    return app 

