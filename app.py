from flask import Flask, render_template, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

"""
- Flask: responsável pela conexão da aplicação com o servidor
- render_template: permite renderizar modelos, como, por exemplo, as páginas HTML
- url_for(): permite a interação entre as páginas HTML com a página principal
"""

app = Flask(__name__)  # Aplicativo Flask

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_contatos.sqlite3'

db = SQLAlchemy(app)

# Banco de dados db_contato
class tb_contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    mensagem = db.Column(db.String(200))
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

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


with app.app_context():
    db.create_all()

if __name__ == "__main__":  # Bloco de execusão do código principal. A função debug retornará eventuais erros
    app.run(debug=True)
