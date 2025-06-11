from flask import Blueprint, jsonify, request
from db_config import db
from models import Tarefa

# Cria um Blueprint para agrupar rotas relacionadas a tarefas
tarefa_bp = Blueprint('tarefa_bp', __name__)

# Rota GET - Lista todas as tarefas
@tarefa_bp.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return jsonify([
        {
            'id': tarefa.id,
            'nome_tarefa': tarefa.nome_tarefa,
            'status_tarefa': tarefa.status_tarefa
        } for tarefa in tarefas
    ]), 200

# Rota GET - Buscar uma tarefa por ID
@tarefa_bp.route('/tarefas/<int:id>', methods=['GET'])
def buscar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if tarefa:
        return jsonify({
            'id': tarefa.id,
            'nome_tarefa': tarefa.nome_tarefa,
            'status_tarefa': tarefa.status_tarefa
        }), 200
    return jsonify({'mensagem': 'Tarefa não encontrada'}), 404

# Rota POST - Cria uma nova tarefa
@tarefa_bp.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.json
    nova_tarefa = Tarefa(
        nome_tarefa=dados['nome_tarefa'],
        status_tarefa=dados['status_tarefa']
    )
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify({
        'id': nova_tarefa.id,
        'nome_tarefa': nova_tarefa.nome_tarefa,
        'status_tarefa': nova_tarefa.status_tarefa
    }), 201

# Rota PUT - Atualizar uma tarefa existente
@tarefa_bp.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if tarefa:
        dados = request.json
        tarefa.nome_tarefa = dados.get('nome_tarefa', tarefa.nome_tarefa)
        tarefa.status_tarefa = dados.get('status_tarefa', tarefa.status_tarefa)
        db.session.commit()
        return jsonify({
            'id': tarefa.id,
            'nome_tarefa': tarefa.nome_tarefa,
            'status_tarefa': tarefa.status_tarefa
        }), 200
    return jsonify({'mensagem': 'Tarefa não encontrada'}), 404

# Rota DELETE - Excluir uma tarefa pelo ID
@tarefa_bp.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
        return '', 204
    return jsonify({'mensagem': 'Tarefa não encontrada'}), 404