from datetime import datetime
 
from tarefas.models.database import Database
 
 
class Tarefas:
    """Provê métodos para armazenar, recuperar e processar os dados das
    tarefas criadas a partir do formulário principal.
    """
 
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
 
    def salvarTarefas(self):
        """Salva a tarefa no banco de dados."""
 
        sql = 'INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao) # protege contra SQL Injection
 
        # Gerenciador de contexto (with)
        # Acessa os métodos __enter__e__exit__ da classe
        with Database() as db:
            db.executar(sql, params)
 
 
    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""
 
        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao
        FROM tarefas LIMIT 100; '''
 
        with Database() as db:
            tarefas_banco = db.executar(sql)
 
        return tarefas_banco if tarefas_banco else []
 
   
    @staticmethod
    def apagarTarefas(id_tarefa):
 
        sql = """DELETE FROM tarefas WHERE id_tarefa = %s;"""
        params = (id_tarefa,)
        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def carregarTarefa(id_tarefa) -> "Tarefas | None":
        sql = """
        SELECT id_tarefa, titulo_tarefa, data_conclusao
        FROM tarefas
        WHERE id_tarefa = %s
        """

        with Database() as db:
            resultado = db.executar(sql, (id_tarefa,))

        if not resultado:
            return None

        dados = resultado[0]
        return Tarefas(
            titulo=dados['titulo_tarefa'],
            id=dados['id_tarefa'],
            data_conclusao=dados['data_conclusao']
        )

    def atualizarTarefa(self, titulo, data_conclusao):
        sql = """UPDATE tarefas
             SET titulo_tarefa = %s, data_conclusao = %s
             WHERE id_tarefa = %s"""

        params = (titulo, data_conclusao, self.id)

        with Database() as db:
            db.executar(sql, params)

 
# Área 51 (testes)
#tarefa = Tarefa('Minha nova tarefa')
#tarefa.salvarTarefas()