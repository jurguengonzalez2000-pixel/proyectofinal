from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth_bp',__name__)


@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == '1234':

        token = create_access_token(
            identity=username,
            additional_claims={"rol": "admin"}

        )

        return jsonify({
            'access_token': token
        }), 200

    return jsonify({
        'error': 'Credenciales incorrectas'
    }), 401
    