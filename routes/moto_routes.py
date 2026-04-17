from flask import Blueprint, request, jsonify
from models.moto import Moto

moto_bp = Blueprint('moto_bp', __name__)

# 📌 Obtener todas
@moto_bp.route('/motos', methods=['GET'])
def get_motos():
    data = Moto.get_all()
    return jsonify(data)

# 📌 Obtener una por ID
@moto_bp.route('/motos/<int:id>', methods=['GET'])
def get_moto(id):
    data = Moto.get_by_id(id)
    return jsonify(data)

# 📌 Crear moto
@moto_bp.route('/motos', methods=['POST'])
def create_moto():
    data = request.json

    Moto.create(
        data['marca'],
        data['modelo'],
        data['cilindraje'],
        data['anio'],
        data['precio'],
        data['id_proveedor']
    )

    return jsonify({"message": "Moto creada correctamente"})

# 📌 Actualizar
@moto_bp.route('/motos/<int:id>', methods=['PUT'])
def update_moto(id):
    data = request.json

    Moto.update(
        id,
        data['marca'],
        data['modelo'],
        data['cilindraje'],
        data['anio'],
        data['precio'],
        data['id_proveedor']
    )

    return jsonify({"message": "Moto actualizada"})

# 📌 Eliminar
@moto_bp.route('/motos/<int:id>', methods=['DELETE'])
def delete_moto(id):
    Moto.delete(id)
    return jsonify({"message": "Moto eliminada"})