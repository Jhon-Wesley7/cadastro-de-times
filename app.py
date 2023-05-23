import time
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

times = []

@app.route('/')
def index():
    return render_template('index.html', times=time)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    time = request.form['time']
    jogadores = request.form['jogadores']
    resultado = request.form['resultado']

    time = {'time': time, 'jogadores': jogadores, 'resultado': resultado}
    time.append(times)

    return redirect('/')

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    time = None
    for t in times:
        if t['id'] == id:
            time = t
            break

    return render_template('edicao.html', time=time)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    time = request.form['time']
    jogadores = request.form['jogadores']
    resultado = request.form['resultado']

    for t in times:
        if t['id'] == id:
            t['nome'] == time
            t['jogadores'] == jogadores
            t['resultado'] == resultado
            break

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)