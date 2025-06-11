from db_config import app, db
from routes import tarefa_bp

# Registra o blueprint das rotas de tarefas
app.register_blueprint(tarefa_bp)

# Cria as tabelas do banco de dados (se ainda não existirem)
with app.app_context():
    db.create_all()

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
