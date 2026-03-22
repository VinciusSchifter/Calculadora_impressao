import pytest
from src.calculator import calcular_preco


def test_preco_couche():
    assert calcular_preco(10, 20, 2, "couche") > 0


def test_preco_offset():
    assert calcular_preco(10, 20, 2, "offset") > 0


def test_papel_invalido():
    with pytest.raises(ValueError):
        calcular_preco(10, 20, 2, "papel_inexistente")
