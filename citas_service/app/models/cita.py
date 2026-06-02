from app.extensions import db

class Cita(db.Model):

    __tablename__ = 'citas'

    id_cita = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.String(50))
    motivo = db.Column(db.String(255))
    estado = db.Column(db.String(30))

    id_paciente = db.Column(db.Integer)
    id_doctor = db.Column(db.Integer)
    id_centro = db.Column(db.Integer)

    id_usuario_registro = db.Column(db.Integer)