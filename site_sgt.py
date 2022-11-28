from flask import Flask, render_template, url_for

"""
- Flask: responsável pela conexão da aplicação com o servidor
- render_template: permite renderizar modelos, como, por exemplo, as páginas HTML
- url_for(): permite a interação entre as páginas HTML com a página principal
"""

app = Flask(__name__)  # Aplicativo Flask

@app.route('/sobre')
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

@app.route('/contato')
def contato():  # Neste módulo será implementado um sistema de formulários
    return render_template("contato.html")

if __name__ == "__main__":  # Bloco de execusão do código principal. A função debug retornará eventuais erros
    app.run(debug=True)
