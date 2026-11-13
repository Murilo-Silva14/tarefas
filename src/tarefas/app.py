from flask import Flask, abort, redirect, render_template, request, url_for
 
from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefas
 
app = Flask(__name__)
 
with app.app_context():
    init_db()
   
@app.route('/test')
def test():
    return 'Servidor online!'
 
@app.route('/', methods=['GET', 'POST'])
def home():
 
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # casa com o nome do input no form
        data_conclusao_form = request.form['dataConclusao'] #casa com o nome do input no form
 
        data_corrigida = data_conclusao_form or None
        # 'or' nesse caso é um operador de
 
        # Instnaciamos uma nova tarefa com os dados recebidos do form
        tarefas = Tarefas(titulo=titulo_form, data_conclusao=data_corrigida)
       
        # Salvamos a tarefa no banco
        tarefas.salvarTarefas()
 
        return redirect(url_for('home'))
 
    tarefas = Tarefas.listarTarefas()
 
    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
        tarefa_edicao=None
    )


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    tarefa = Tarefas.carregarTarefa(id)
    if tarefa is None:
        abort(404)

    if request.method == 'POST':
        titulo = request.form['tituloTarefa']
        data_conclusao = request.form['dataConclusao'] or None
        tarefa.atualizarTarefa(titulo, data_conclusao)
        return redirect(url_for('home'))

    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=Tarefas.listarTarefas(),
        tarefa_edicao=tarefa
    )

 
# Crie uma nova funcionalidade para apagar casa uma das tarefas cadastradas
@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
    Tarefas.apagarTarefas(id)
    return redirect(url_for('home'))
 
if __name__ == '__main__':
    app.run()