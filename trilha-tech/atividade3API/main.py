from flask import Flask, jsonify, request , Response # jsonify classe para formatação json
from db.tarefas import Tarefas
from functools import wraps
import secrets


users = {
    "simone":"simone123",
    "teste":"teste123"
}

def check_auth(username, password):
    return username in users and users[username] == password


def authenticate():
    return Response(
        'Acesso restrito. Faça seu login com usuário e senha!',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_basic_auth(f):
    @wraps(f) # decorator abraça as outras funções
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated



app = Flask(__name__) # nome default, vai utilizar o nome da nossa pasta do projeto

# Métodos GET - Todas as tarefas
@app.route("/tarefas", methods=["GET"])
@requires_basic_auth
def listar_tarefas():
    return jsonify(
        dados=Tarefas, 
        total_tarefas= len(Tarefas)
    )

# Método GET - Com filtro, realiza a busca por ID
@app.route("/tarefas/<string:id>", methods=["GET"])
def buscar_tarefa_por_id(id):
    for item in Tarefas:
        if item["id_tarefa"] == id:
            return jsonify(
                dados=item,
            ), 200
    return jsonify(
        mensagem="ID informado não foi encontrado :()",
    ), 401


# Método POST
@app.route("/tarefas", methods=["POST"])
#@requires_basic_auth
def criar_tarefa():
    nova_tarefa = request.json

    nova_tarefa["id_tarefa"] = secrets.token_hex(4)
    Tarefas.append(nova_tarefa)

    return jsonify(
        dados=nova_tarefa,
        mensagem="Nova tarefa criada com sucesso!"
    )

# Método PUT
@app.route('/tarefas/<string:id>', methods=["PUT"])
def atualizar_tarefa(id):
    nova_tarefa = request.json

    tarefa_encontrada = None

    for tarefa in Tarefas:
        if tarefa["id_tarefa"] == id:
            tarefa_encontrada = tarefa
    
    if not tarefa_encontrada:
        return jsonify(
            mensagem="Não foi encontrada a tarefa na base de dados."
        )
    
    tarefa_encontrada.update(nova_tarefa)
    return jsonify (
        dados=nova_tarefa,
        mensagem="Tarefa atualizada com sucesso!"
    )

# Método DELETE
@app.route("/tarefas/<string:id>", methods=["DELETE"])
#@requires_basic_auth
def apagar_tarefa(id):
    global Tarefas

    for tarefa in Tarefas:
        if tarefa['id_tarefa'] == id:
            Tarefas = [tarefa for tarefa in Tarefas if tarefa['id_tarefa'] != id]
            return jsonify(
                mensagem="Tarefa apagada com sucesso!")
    return jsonify(
        mensagem="ID da tarefa não encontrado na base de dados :("), 404
    
app.run()