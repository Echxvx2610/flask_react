from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde otros orígenes (como Netlify)

@app.route('/api/usuarios')
def get_users():
    usuarios = [
        {"id": 1, "nombre": "Ana", "email": "ana@example.com"},
        {"id": 2, "nombre": "Luis", "email": "luis@example.com"},
        {"id": 3, "nombre": "Carlos", "email": "carlos@example.com"}
    ]
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run()
