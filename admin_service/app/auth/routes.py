from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models.usuario import Usuario

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    usuario = Usuario.query.filter_by(
        username=username
    ).first()

    if not usuario:
        return jsonify({
            "error": "Usuario no existe"
        }), 401

    if usuario.password != password:
        return jsonify({
            "error": "Contraseña incorrecta"
        }), 401

    token = create_access_token(
        identity=str(usuario.id_usuario),
        additional_claims={
            "rol": usuario.rol
        }
    )

    return jsonify({
        "access_token": token,
        "rol": usuario.rol
    }), 200