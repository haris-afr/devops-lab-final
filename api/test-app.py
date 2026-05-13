import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client         
def test_health_check(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'

def test_get_courses(client):
    response = client.get('/api/courses')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_course_not_found(client):
    response = client.get('/api/courses/9999')
    assert response.status_code == 404

def test_add_course(client):
    response = client.post('/api/courses',
                           json={'instructor': 'Ali', 'title': 'Abc'})
    assert response.status_code == 200
