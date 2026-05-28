import csv
import requests

BASE_URL = 'http://localhost:5000'

login = requests.post(
    f'{BASE_URL}/auth/login',
    json={
        'username': 'admin',
        'password': '1234'
    }
)

TOKEN = login.json()['token']

headers = {
    'Authorization': f'Bearer {TOKEN}'
}

with open('datos.csv', newline='', encoding='utf-8') as archivo:

    lector = csv.DictReader(archivo)

    for fila in lector:

        if fila['tipo'] == 'centro':

            requests.post(
                f'{BASE_URL}/admin/centros',
                json={
                    'nombre': fila['nombre'],
                    'direccion': fila['extra1']
                },
                headers=headers
            )

        elif fila['tipo'] == 'doctor':

            requests.post(
                f'{BASE_URL}/admin/doctores',
                json={
                    'nombre': fila['nombre'],
                    'especialidad': fila['extra1']
                },
                headers=headers
            )

        elif fila['tipo'] == 'paciente':

            requests.post(
                f'{BASE_URL}/admin/pacientes',
                json={
                    'nombre': fila['nombre'],
                    'telefono': fila['extra1'],
                    'estado': fila['extra2']
                },
                headers=headers
            )

respuesta = requests.post(
    'http://localhost:5001/citas',
    json={
        'fecha': '2026-05-30 10:00',
        'motivo': 'Limpieza dental',
        'id_paciente': 1,
        'id_doctor': 1,
        'id_centro': 1,
        'id_usuario_registra': 1
    },
    headers=headers
)

print(respuesta.json())