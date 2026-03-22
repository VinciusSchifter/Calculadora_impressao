def calcular_preco(largura_cm, altura_cm, quantidade, tipo_papel="couche"):
    area = largura_cm * altura_cm
    base_preco = 0.05

    if tipo_papel == "couche":
        fator = 1.2
    elif tipo_papel == "offset":
        fator = 1.0
    elif tipo_papel == "reciclado":
        fator = 0.9
    else:
        raise ValueError("Tipo de papel inválido.")

    return round(area * base_preco * fator * quantidade, 2)
