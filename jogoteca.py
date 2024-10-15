from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('GoW', 'Rack n Slash', 'PS2')
jogo3 = Jogo('MK', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]
        
        
app = Flask(__name__)
@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html',titulo='Jogos', jogos=lista)
app.run()
