from app.extensions import db

class Doctor(db.Model):
    __tablename__ = "doctor"
    

    id_doctor = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(90), nullable=False)
    especialidad = db.Column(db.String(90))
    
    id_usuario= db.Column(db.Integer, db.ForeignKey("usuario.id_usuario"))
    
    