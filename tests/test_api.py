import pytest
from src.api import app


@pytest.fixture
def client():
    return app.test_client()


def test_calculo_endpoint(client):
    response = client.get(
        "/calcular?largura=10&altura=20&quantidade=2&papel=couche"
    )
    assert response.status_code == 200
    assert "preco" in response.json
