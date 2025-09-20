import pytest
from app import app, db, init_db
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            init_db(app)
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Gerar Prompt' in response.data

def test_gerar_prompt(client):
    data = {
        'titulo': 'Test Prompt',
        'tipo': 'Geração de Conteúdo',
        'nivel_detalhe': 'Resumido'
    }
    response = client.post('/gerar_prompt', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    result = json.loads(response.data)
    assert 'titulo' in result
    assert result['titulo'] == 'Test Prompt'