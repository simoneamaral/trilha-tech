from db_config import db

class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    nome_tarefa = db.Column(db.String(100), nullable=False)
    status_tarefa = db.Column(db.String(100), nullable=False)
