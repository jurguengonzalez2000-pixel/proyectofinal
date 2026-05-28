from app.extensions import db

class Centro(db.Model):
    __tablename__ = "centro"
    
    id_centro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(90), nullable=False)
    direccion  = db.Column(db.String(245))
    