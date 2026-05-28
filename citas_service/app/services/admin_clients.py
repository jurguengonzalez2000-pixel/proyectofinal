import requests
ADMIN_URL = 'http://admin_service:5000'

def obtener_doctores(token):

    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(
        f'{ADMIN_URL}/admin/doctores',
        headers=headers
    )
    return response.json()