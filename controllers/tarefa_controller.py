from models.tarefa import Tarefa


class TarefaController:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, descricao):
        nova_tarefa = Tarefa(self.proximo_id, descricao)
        self.tarefas.append(nova_tarefa)
        self.proximo_id += 1
        return nova_tarefa

    def listar_tarefas(self):
        return self.tarefas

    def remover_tarefa(self, id):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.id != id]

    def concluir_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                tarefa.concluir()
                return tarefa
        return None