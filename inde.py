from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

pokemons = {
    1: {"id": 1, "nombre": "Bulbasaur", "tipo": ["Planta", "Veneno"], "habilidad": "Espesura"},
    2: {"id": 2, "nombre": "Charmander", "tipo": ["Fuego"], "habilidad": "Brasas"}
}

users = {
    "admin": "password"
}

#  Authentication
@auth.verify_token
def verify_token(token):
    if token:
        username = auth.decode_token(token)
        if username in users: 
            return username
        else:
            return None

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username') 
    password = request.json.get('password')
    if username in users and users[username] == password:
        token = auth.encode_token(username)
        return jsonify({'token': token})
    else:
        abort(401, description='Credenciales invalidas')  

# Routes 
@app.route('/pokemons', methods=['GET'])
@auth.login_required
def get_pokemons():
    return jsonify(list(pokemons.values()))

@app.route('/pokemons/<int:pokemon_id>', methods=['GET'])
@auth.login_required
def get_pokemon(pokemon_id):
    if pokemon_id in pokemons:
        return jsonify(pokemons[pokemon_id])
    else:
        abort(404, description='Pokemon no encontrado')

@app.route('/pokemons', methods=['POST'])
@auth.login_required
def create_pokemon():
    new_pokemon = request.get_json()
    if not new_pokemon or not all(key in new_pokemon for key in ('nombre', 'tipo', 'habilidad')):
        abort(400, description='Data incompleta')

    new_pokemon_id = max(pokemons.keys()) + 1
    pokemons[new_pokemon_id] = {
        "id": new_pokemon_id,
        "nombre": new_pokemon['nombre'],
        "tipo": new_pokemon['tipo'],
        "habilidad": new_pokemon['habilidad']
    }
    return jsonify({'message': 'Pokemon creado exitosamente'})
   
@app.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
@auth.login_required
def update_pokemon(pokemon_id):
    if pokemon_id not in pokemons:
        abort(404, description='Pokemon no encontrado')

    updated_pokemon = request.get_json()
    if not updated_pokemon or not all(key in updated_pokemon for key in ('nombre', 'tipo', 'habilidad')):
        abort(400, description='Data incompleta')

    pokemons[pokemon_id] = {
        "id": pokemon_id,
        "nombre": updated_pokemon['nombre'],
        "tipo": updated_pokemon['tipo'],
        "habilidad": updated_pokemon['habilidad']
    }
    return jsonify({'message': 'Pokemon actualizado exitosamente'})

@app.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
@auth.login_required
def delete_pokemon(pokemon_id):
    if pokemon_id in pokemons:
        del pokemons[pokemon_id]
        return jsonify({'message': 'Pokemon eliminado con exito'})
    else:
        abort(404, description='Pokemon no encontrado')

