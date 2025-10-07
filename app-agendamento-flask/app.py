from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Configuração
app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma_chave_secreta_forte'  # Necessário para usar 'flash'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                                    'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# =======================================================
# 1. MODELOS DE DADOS
# =======================================================

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Relacionamento com Consultas
    consultas = db.relationship('Consulta', backref='paciente', lazy=True)


class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default='Agendada')  # Opções: Agendada, Cancelada, Concluída

    # Chave Estrangeira: liga a consulta a um paciente
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)


# Cria o banco de dados e as tabelas se não existirem
with app.app_context():
    db.create_all()


# =======================================================
# 2. ROTAS
# =======================================================

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Tenta agendar a consulta
        nome = request.form.get('nome')
        email = request.form.get('email')
        data_str = request.form.get('data')
        hora_str = request.form.get('hora')
        motivo = request.form.get('motivo')

        # --- VALIDAÇÃO DE DADOS ---
        if not all([nome, email, data_str, hora_str, motivo]):
            flash('Todos os campos são obrigatórios!', 'error')
            return redirect(url_for('index'))

        try:
            # 1. Combina Data e Hora em um único objeto datetime
            data_hora_agendada = datetime.strptime(f'{data_str} {hora_str}', '%Y-%m-%d %H:%M')
        except ValueError:
            flash('Formato de Data ou Hora inválido.', 'error')
            return redirect(url_for('index'))

        # 2. Verifica se o horário está no futuro
        if data_hora_agendada <= datetime.now():
            flash('Não é possível agendar consultas no passado ou no momento atual.', 'error')
            return redirect(url_for('index'))

        # 3. VERIFICAÇÃO DE CONFLITO SIMPLES (Sobrecarga de Horário)
        # Verifica se já existe uma consulta agendada para o mesmo minuto
        conflito = Consulta.query.filter_by(data_hora=data_hora_agendada, status='Agendada').first()
        if conflito:
            flash('Desculpe, este horário já está reservado. Escolha outro.', 'error')
            return redirect(url_for('index'))

        # --- CRIAÇÃO DOS REGISTROS ---
        try:
            # 1. Encontra ou Cria o Paciente
            paciente = Paciente.query.filter_by(email=email).first()
            if not paciente:
                paciente = Paciente(nome=nome, email=email)
                db.session.add(paciente)
                db.session.commit()

            # 2. Cria a Consulta
            nova_consulta = Consulta(
                data_hora=data_hora_agendada,
                motivo=motivo,
                paciente_id=paciente.id
            )
            db.session.add(nova_consulta)
            db.session.commit()

            flash('Consulta agendada com sucesso!', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            db.session.rollback()
            flash(f'Erro interno ao agendar: {e}', 'error')
            return redirect(url_for('index'))

    # Rota GET: Exibir Formulário e Lista de Consultas

    # Puxa todas as consultas agendadas e ordena pela data/hora
    consultas = Consulta.query.order_by(Consulta.data_hora.asc()).all()

    return render_template('index.html', consultas=consultas)


@app.route('/cancelar/<int:consulta_id>', methods=['POST'])
def cancelar_consulta(consulta_id):
    consulta = Consulta.query.get_or_404(consulta_id)

    if consulta.status == 'Agendada':
        consulta.status = 'Cancelada'
        db.session.commit()
        flash(f'Consulta ID {consulta_id} cancelada.', 'success')
    else:
        flash(f'Consulta ID {consulta_id} não pode ser cancelada (Status: {consulta.status}).', 'error')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)