from app.extensions import db
class Usuario(db.Model):
    __tablename__= "usuario"
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(245), nullable=False)
    rol = db.Column(db.String(20), nullable=True)
    