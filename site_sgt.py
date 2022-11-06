from flask import Flask, render_template
"""
- Flask: responsável pela conexão da aplicação com o servidor
- render_template: permite renderizar modelos, como, por exemplo, as páginas HTML
"""

app = Flask(__name__)  # Aplicativo Flask

@app.route('/')
def homepage():
    """
    Página inicial, nela será apresentado detalhes sobre o projeto e  sobre a equipe.
    :return: página principal
    """
    return render_template("homepage.html")

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
    :return: página 3
    """
    return render_template("midia.html")

@app.route('/entre_em_contato')
def entre_em_contato():  # Neste módulo será implementado um sistema de formulários
    pass

if __name__ == "__main__":  # Bloco de execusão do código principal. A função debug retornará eventuais erros
    app.run(debug=True)
