import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50))
    subtipo = db.Column(db.String(50))
    subitem = db.Column(db.String(50))
    tom_estilo = db.Column(db.String(50))
    persona = db.Column(db.String(50))
    objetivos = db.Column(db.Text)
    regras = db.Column(db.Text)
    contexto = db.Column(db.Text)
    restricoes = db.Column(db.Text)
    exemplos = db.Column(db.Text)
    framework = db.Column(db.String(50))
    frontend = db.Column(db.String(50))
    backend = db.Column(db.String(50))
    main_language = db.Column(db.String(50))
    ferramentas_externas = db.Column(db.Text)  # JSON string
    nivel_detalhe = db.Column(db.String(20))
    publico_alvo = db.Column(db.String(50))
    formato_saida = db.Column(db.String(50))
    prioridade = db.Column(db.String(50))
    metodo_raciocinio = db.Column(db.String(50))
    idioma = db.Column(db.String(20))
    metricas = db.Column(db.Text)  # JSON string
    integracao_multimodal = db.Column(db.Text)  # JSON string
    historico = db.Column(db.Boolean, default=False)
    modo_iterativo = db.Column(db.Boolean, default=False)
    nivel_criatividade = db.Column(db.Integer, default=50)
    dependencias = db.Column(db.Text)
    ambiente_deploy = db.Column(db.String(50))
    testes = db.Column(db.Text)  # JSON string
    versionamento = db.Column(db.String(50))
    estrutura_projeto = db.Column(db.Text)
    padroes_codigo = db.Column(db.String(50))
    integracao_ci_cd = db.Column(db.Text)  # JSON string
    estilo_saida = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class SavedPrompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=False)  # JSON string
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

def init_db(app):
    with app.app_context():
        db.create_all()