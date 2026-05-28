from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt


def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()

            claims = get_jwt()

            if claims.get('rol') not in roles:
                return jsonify({
                    'error': 'No autorizado'
                }), 403

            return fn(*args, **kwargs)

        return wrapper

    return decorator