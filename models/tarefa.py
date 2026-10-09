class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def atualizar_descricao(self, descricao):
        self.descricao = descricao