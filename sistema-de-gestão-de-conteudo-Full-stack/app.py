from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Configuração
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                                    'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# =======================================================
# 1. MODELO DO BANCO DE DADOS (O POST)
# =======================================================
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Post {self.titulo}>'

    def to_dict(self):
        """Converte o objeto Post para um dicionário JSON."""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'corpo': self.corpo,
            'data_criacao': self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')
        }


# Cria o banco de dados e as tabelas se não existirem
with app.app_context():
    db.create_all()


# =======================================================
# 2. ROTAS DE VISUALIZAÇÃO (Front-End)
# =======================================================

# Rota Inicial: Lista todos os posts (READ Público)
@app.route('/')
def index():
    # Ordena os posts pelo mais recente
    posts = Post.query.order_by(Post.data_criacao.desc()).all()
    return render_template('index.html', posts=posts)


# Rota de Post Individual (READ Público)
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


# Rota de Administração (Painel)
@app.route('/admin')
def admin():
    posts = Post.query.order_by(Post.data_criacao.desc()).all()
    # Para o painel, passamos os posts para edição
    return render_template('admin.html', posts=posts)


# =======================================================
# 3. ROTAS DA API (CRUD Admin Actions)
# =======================================================

# Rota CREATE
@app.route('/admin/create', methods=['POST'])
def create_post():
    # Usamos request.form porque a submissão vem de um formulário HTML simples
    titulo = request.form['titulo']
    corpo = request.form['corpo']

    if not titulo or not corpo:
        return "Erro: Título e corpo são obrigatórios", 400

    novo_post = Post(titulo=titulo, corpo=corpo)
    db.session.add(novo_post)
    db.session.commit()
    # Após a criação, redireciona de volta para o painel de administração
    return redirect(url_for('admin'))


# Rota UPDATE (Edição)
@app.route('/admin/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        post.titulo = request.form['titulo']
        post.corpo = request.form['corpo']
        db.session.commit()
        return redirect(url_for('admin'))

    # Se for GET, renderiza a página de edição (usaremos o admin.html como modelo)
    return render_template('admin.html', post_to_edit=post, posts=Post.query.all())


# Rota DELETE
@app.route('/admin/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)