from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Configuração
app = Flask(__name__)
# Configura o banco de dados SQLite no caminho absoluto do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                                    'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# =======================================================
# 1. MODELO DO BANCO DE DADOS (A TAREFA)
# =======================================================
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    concluida = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Converte o objeto Tarefa para um dicionário JSON."""
        return {
            'id': self.id,
            'descricao': self.descricao,
            'concluida': self.concluida
        }


# Cria o banco de dados e as tabelas se não existirem
with app.app_context():
    db.create_all()


# =======================================================
# 2. ROTAS DA API (Endpoints) - O CRUD
# =======================================================

# Rota READ (Listar todas as tarefas)
@app.route('/api/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = Tarefa.query.all()
    # Converte a lista de objetos Tarefa para uma lista de dicionários JSON
    return jsonify([t.to_dict() for t in tarefas])


# Rota CREATE (Criar uma nova tarefa)
@app.route('/api/tarefas', methods=['POST'])
def criar_tarefa():
    data = request.get_json()
    if not data or 'descricao' not in data:
        return jsonify({'erro': 'Descrição é obrigatória'}), 400

    nova_tarefa = Tarefa(descricao=data['descricao'])
    db.session.add(nova_tarefa)
    db.session.commit()
    return jsonify(nova_tarefa.to_dict()), 201  # 201: Criado


# Rota UPDATE (Marcar como concluída)
@app.route('/api/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    data = request.get_json()

    if 'concluida' in data:
        tarefa.concluida = data['concluida']

    db.session.commit()
    return jsonify(tarefa.to_dict())


# Rota DELETE (Excluir uma tarefa)
@app.route('/api/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'mensagem': 'Tarefa deletada com sucesso'}), 204  # 204: Sem Conteúdo


# =======================================================
# 3. ROTA FRON-END (Servir o HTML)
# =======================================================

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Adicione debug=True apenas para ambiente de desenvolvimento
    app.run(debug=True)