from flask import Flask, render_template
from livereload import Server


app = Flask(__name__)

@app.route('/inicio')


def ola():
    lista = ['Tetris', 'Skyrim', 'Crash']
    return render_template('lista.html', titulo='Jogos', jogos = lista)   

if __name__ == '__main__':
    #live render loader every f5
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(port=5555)
