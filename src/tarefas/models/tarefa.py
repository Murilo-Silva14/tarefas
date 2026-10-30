from datetime import datetime

from tarefas.models.database import Database


class Tarefa:
    """Provê mmétodos para armazenar, recuperar e processar os dados das terefas
    criadas a partir do formulário principal.
    """

    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salva a tarefa no banco de dados"""

        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao)
        
        with Database() as db:
            db.executar(sql, params)


#Teste
tarefa = Tarefa('Minhanova tarefa')
tarefa.salvarTarefa()