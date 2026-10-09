from flask import Flask

from routes.tarefa_routes import tarefa_routes

app = Flask(__name__)
app.register_blueprint(tarefa_routes)


if __name__ == '__main__':
    app.run(debug=True)