from flask import Blueprint, request, jsonify
from app.extensions import db 
from app.models.doctor import Doctor
from app.models.pacientes import Pacientes 
from app.models.usuario import Usuario
from app.models.centro import Centro 
from app.utils.decorador import role_required

admin_bp = Blueprint("admin_bp", __name__)

@admin_bp.route("/usuario", methods=["POST"])
@role_required(["admin"])
def crear_usuario():
    data = request.get_json()
    
    usuario = Usuario(
        username=data["username"],
        password=data["password"],
        rol=data["rol"])
    
    db.session.add(usuario)
    db.session.commit()
    
    return jsonify({"mensaje": "usuario creado"}), 201

@admin_bp.route("/doctores", methods=["POST"])
@role_required(["admin"])
def doctor():
    data = request.get_json()
    
    doctor = Doctor (
        nombre=data["nombre"],
        especialidad=data["especialidad"],
        id_usuario=data.get("id_usuario")
        
        
    )
    
    db.session.add(doctor)
    db.session.commit()
    
    return jsonify({"mensaje":"doctor creado"}),201

@admin_bp.route("/pacientes", methods=["POST"])
@role_required(["admin"])
def crear_paciente ():
    data = request.get_json()
    
    paciente = Pacientes(
        nombre=data["nombre"],
        telefono=data["telefono"],
        estado=data["estado"],
        id_usuario=data["id_usuario"]
    )
    
    db.session.add(paciente)
    db.session.commit()
    
    return jsonify({"mensaje": "paciente creado"}), 201

@admin_bp.route("/centros", methods=["POST"])
@role_required(["admin"])
def crearcentro():
    data= request.get_json()
    
    centro = Centro(
        nombre=data["nombre"],
        direccion=data["direccion"]
    )
    
    db.session.add(centro)
    db.session.commit()
    
    return jsonify({"mensaje":"centro creado correctamente"}), 201

    
@admin_bp.route("/doctores", methods=["GET"])
def lista_doctores():
    
    doctores = Doctor.query.all()
    
    resultado= []
    for doctor in doctores:
        resultado.append({
            "id_doctor":doctor.id_doctor,
            "nombre": doctor.nombre,
            "especialidad":doctor.especialidad
        })
    return jsonify(resultado)

@admin_bp.route("/pacientes", methods=["GET"])
def lista_paciente():
    
    pacientes  = Pacientes.query.all()
    
    resultado = []
    
    for p in pacientes :
        resultado.append({
            "id_pacientes": p.id_pacientes,
            "nombre": p.nombre,
            "telefono": p.telefono,
            "estado": p.estado
        })
        
    return jsonify(resultado)

@admin_bp.route("/centros", methods=["GET"])
def lista_centro():
    centros = Centro.query.all()
    
    resultado = []
    
    for centro in centros:
        
        resultado.append({
            "id_centro":centro.id_centro,
            "nombre": centro.nombre,
            "direccion": centro.direccion
        })       
    return jsonify(resultado)

@admin_bp.route("/doctores/<int:id_doctor>", methods=["GET"])
def obtener_doctor(id_doctor):

    doctor = Doctor.query.get(id_doctor)

    if not doctor:
        return jsonify({
            "error": "Doctor no existe"
        }), 404

    return jsonify({
        "id_doctor": doctor.id_doctor,
        "nombre": doctor.nombre,
        "especialidad": doctor.especialidad
    })


@admin_bp.route("/pacientes/<int:id_paciente>", methods=["GET"])
def obtener_paciente(id_paciente):

    paciente = Pacientes.query.get(id_paciente)

    if not paciente:
        return jsonify({
            "error": "Paciente no existe"
        }), 404

    return jsonify({
        "id_pacientes": paciente.id_pacientes,
        "nombre": paciente.nombre,
        "telefono": paciente.telefono,
        "estado": paciente.estado
    })
    
@admin_bp.route("/centros/<int:id_centro>", methods=["GET"])
def obtener_centro(id_centro):

    centro = Centro.query.get(id_centro)

    if not centro:
        return jsonify({
            "error": "Centro no existe"
        }), 404

    return jsonify({
        "id_centro": centro.id_centro,
        "nombre": centro.nombre,
        "direccion": centro.direccion
    })