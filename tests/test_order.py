import pytest
from app.db.connection import create_app, db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_order(client):
    response = client.post('/api/orders', json={
        'product_name': 'Test Product',
        'quantity': 10,
        'price': 99.99
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Order created'

def test_get_orders(client):
    response = client.get('/api/orders')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_order(client):
    client.post('/api/orders', json={
        'product_name': 'Test Product',
        'quantity': 10,
        'price': 99.99
    })
    
    response = client.get('/api/orders/1')
    assert response.status_code == 200
    assert response.json['product_name'] == 'Test Product'

def test_update_order(client):
    client.post('/api/orders', json={
        'product_name': 'Test Product',
        'quantity': 10,
        'price': 99.99
    })
    
    response = client.put('/api/orders/1', json={'status': 'Shipped'})
    assert response.status_code == 200
    assert response.json['message'] == 'Order updated'

def test_delete_order(client):
    client.post('/api/orders', json={
        'product_name': 'Test Product',
        'quantity': 10,
        'price': 99.99
    })
    
    response = client.delete('/api/orders/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Order deleted'
