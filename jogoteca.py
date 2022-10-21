from flask import Flask, render_template, request, redirect, session, flash, url_for
from livereload import Server
from classes import Usuario, Jogo


usuario_1 = Usuario('User1', 'user1', 'user1')
usuario_2 = Usuario('User2', 'user2', 'user2')
usuario_3 = Usuario('User3', 'user3', 'user3')

usuarios = {
    usuario_1.nickname : usuario_1,
    usuario_2.nickname : usuario_2,
    usuario_3.nickname : usuario_3
}
jogo_1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_2 = Jogo('God of War', 'War', 'Foda-se')
jogo_3 = Jogo('Mortal Kombat', 'luta', 'Xbox')

lista = [jogo_1, jogo_2, jogo_3]

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('novo-jogo') == 'novo-jogo':
            return redirect('/novo')
    if request.method == 'POST':
        if request.form.get('logout') == 'logout':
            return redirect('/logout')

    return render_template \
        ('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session \
        or session['usuario_logado'] == None:
            return redirect('/login?proxima=novo')
    return render_template \
        ('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    server = Server(app.wsgi_app)
    server.serve(port = 5555)
