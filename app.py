from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)  # Aplicativo Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_contatos.sqlite3'
# Configuração da chave secreta
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

# chave para o 'secret key' da função 'flash'
app.secret_key = "super secret key"

# Configuração para a autenticação de usuário
login_manager = LoginManager()
login_manager.init_app(app)
# Criação da tabela User
@login_manager.user_loader  # usado para recarregar o id do usuário autenticado
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


# Tabela para o banco de dados
class tb_contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    mensagem = db.Column(db.String(200))

    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

# Configurações para o Banco de dados e criação dda tabela User
class User(db.Model, UserMixin):
    __tablename__ = "Usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    user = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)  # Verifica se o funcionário está habilitado

    def __init__(self, name, user, password, status):
        self.name = name
        self.user = user
        self.password = generate_password_hash(password)
        self.status = status

with app.app_context():
    db.create_all()

    # Comando para adicionar um usuário padrão ao criar o banco de dados
    if User.query.filter_by(user='administrador').count() < 1:
        user = User(name='Administrador', user='administrador', password='FisicaQuantica*', status=1)
        db.session.add(user)
        db.session.commit()


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form["senha"]
        user = User.query.filter_by(user=usuario).first()
        if not user or not check_password_hash(user.password, senha):  # Verificação de usuário e senha na db
            flash("Usuário ou senha inválido!")
        elif user.status == 1:
            login_user(user)
            return redirect(url_for('pagina_inicial'))
        else:
            flash("Usuário inválido")
    return render_template('login.html')


# Caso o usuário não esteja autenticado ele será redirecionado para a página de login
@login_manager.unauthorized_handler
def unauthorized_callback():
    flash("Faça o login!")
    return redirect(url_for('login'))


# Tela de logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('sobre'))


# Página inicial
@app.route("/pagina_inicial")
@login_required
def pagina_inicial():
    """
    Página inicial, nela será apresentada a tela de opções
    :return: Tela inicial
    """
    return render_template("pagina_inicial.html", contatos=tb_contato.query.all())


@app.route('/')
def sobre():
    """
    Página inicial, nela será apresentado detalhes sobre o projeto e  sobre a equipe.
    :return: página principal
    """
    return render_template("sobre.html")

@app.route('/pem')
def pem():
    """
    Página 2, nela será apresentado os detalhes sobre a missão PEM, sobre o funcionamento do satélite e sobre as fases
    da olimpiada de satélites.
    :return: página 2
    """
    return render_template("pem.html")

@app.route('/midia')
def midia():
    """
    Página 3, nela será apresentada as mídias da equipe.
    OBS: Colocar um campo de inserção de mídia.
    OBS: Colocar um campo de inserção de mídia.
    :return: página 3
    """
    return render_template("midia.html")

@app.route('/contato', methods=["GET", "POST"])
def contato():  # Neste módulo será implementado um sistema de formulários
    nome = request.form.get('nome')
    email = request.form.get('email')
    mensagem = request.form.get('mensagem')

    if request.method == 'POST':
        contato = tb_contato(nome, email, mensagem)
        db.session.add(contato)
        db.session.commit()
    return render_template("contato.html")


if __name__ == "__main__":  # Bloco de execusão do código principal. A função debug retornará eventuais erros
    app.run(debug=True)
