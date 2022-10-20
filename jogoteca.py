from flask import Flask, render_template, request
from livereload import Server


class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo_1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_2 = Jogo('God of War', 'War', 'Foda-se')
jogo_3 = Jogo('Mortal Kombat', 'luta', 'Xbox')
lista = [jogo_1, jogo_2, jogo_3]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template \
        ('lista.html', titulo = 'Jogos', jogos = lista)   

@app.route('/novo')
def novo():
    return render_template \
        ('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template \
        ('lista.html', titulo='Jogos', jogos=lista)


if __name__ == '__main__':
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(port = 5555)
