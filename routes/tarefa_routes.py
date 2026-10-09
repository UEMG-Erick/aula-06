from flask import Blueprint, redirect, render_template, request, url_for

from controllers.tarefa_controller import TarefaController

tarefa_routes = Blueprint('tarefa_routes', __name__)
controller = TarefaController()


@tarefa_routes.route('/')
def index():
    tarefas = controller.listar_tarefas()
    return render_template('index.html', tarefas=tarefas)


@tarefa_routes.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao', '').strip()
    if descricao:
        controller.adicionar_tarefa(descricao)
    return redirect(url_for('tarefa_routes.index'))


@tarefa_routes.route('/remover/<int:id>', methods=['POST'])
def remover(id):
    controller.remover_tarefa(id)
    return redirect(url_for('tarefa_routes.index'))


@tarefa_routes.route('/concluir/<int:id>', methods=['POST'])
def concluir(id):
    controller.concluir_tarefa(id)
    return redirect(url_for('tarefa_routes.index'))