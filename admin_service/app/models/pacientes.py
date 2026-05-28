from app.extensions import db
class Pacientes (db.Model):
    __tablename__ = "pacientes"
    
    id_pacientes = db.Column(db.Integer, primary_key= True)
    nombre= db.Column(db.String(90), nullable=False)
    telefono= db.Column(db.String(20))
    estado = db.Column(db.String(20),default= "ACTIVO")
    
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id_usuario"))
        