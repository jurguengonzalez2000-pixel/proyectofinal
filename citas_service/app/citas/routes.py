from flask import Blueprint,request, jsonify
from app.extensions import db 
from app.models.cita import Cita
from flask_jwt_extended import jwt_required

citas_bp =Blueprint ("citas_bp", __name__)

@citas_bp.route("",methods=["POST"])
@jwt_required()
def crear_cita():
    data=request.get_json()
    
    existente = Cita.query.filter_by(
        fecha=data["fecha"],
        id_doctor=data["id_doctor"]
    ).first()
    
    if existente:
        return jsonify({"mensaje": "no hay disponibilidad"}),401
    
    cita = Cita(
        fecha=data["fecha"],
        motivo=data["motivo"],
        estado = "activa",
        id_paciente=data["id_paciente"],
        id_doctor=data["id_doctor"],
        id_centro=data["id_centro"],
        id_usuario_registro=data["id_usuario_registro"]
    )
    
    db.session.add(cita)
    db.session.commit()
    
    return jsonify ({
        "mensaje":"cita creada"
    }),201
      
      



@citas_bp.route('', methods=['GET'])
def listar_citas():

    citas = Cita.query.all()

    resultado = []

    for cita in citas:

        resultado.append({
            'id_cita': cita.id_cita,
            'fecha': cita.fecha,
            'motivo': cita.motivo,
            'estado': cita.estado
        })

    return jsonify(resultado)


@citas_bp.route('/<int:id_cita>', methods=['PUT'])
@jwt_required()
def cancelar_cita(id_cita):

    cita = Cita.query.get(id_cita)

    if not cita:
        return jsonify({
            'error': 'Cita no existe'
        }), 404

    if cita.estado == 'CANCELADA':
        return jsonify({
            'error': 'Cita ya cancelada'
        }), 400

    cita.estado = 'CANCELADA'

    db.session.commit()

    return jsonify({
        'mensaje': 'Cita cancelada'
    })