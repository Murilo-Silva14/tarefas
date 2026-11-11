from flask import Flask, render_template, request, redirect, url_for
 
from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa
 
app = Flask(__name__)
 
with app.app_context():
    init_db()
 
@app.route('/test')
def test():
    return 'Servidor online!'
 
@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # casa com o nome do inputno form
        data_conclusao_form = request.form['dataConclusao'] # casa com onome do imput no form

        data_corrigida = data_conclusao_form if data_conclusao_form != '' else None

        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()

        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
 
    return render_template(
        'base.html',
        titulo_da_pagina = 'Minha lista de tarefas',
        tarefas_da_pagina = tarefas
        )
 
if __name__ == '__main__':
    app.run()