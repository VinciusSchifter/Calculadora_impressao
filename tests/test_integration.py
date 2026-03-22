from src.calculator import calcular_preco


def test_fluxo_completo():
    preco_unitario = calcular_preco(10, 20, 1, "offset")
    preco_total = calcular_preco(10, 20, 10, "offset")
    assert preco_total == preco_unitario * 10
