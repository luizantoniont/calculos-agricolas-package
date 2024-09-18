def prod_agri(colheita_total, area):
    """
    Calcula a produtividade agrícola, que é a quantidade de produto colhido 
    por hectare.
    Args:
        colheita_total (float): Quantidade total de colheita em quilogramas 
        (kg).
        area (float): Área cultivada em hectares (ha).
    Returns:
        float: A produtividade agrícola em kg/hectare.
    Raises:
        ValueError: Se `colheita_total` ou `area` forem menores ou iguais a 
        zero.
    """
    try:
        colheita_total = float(colheita_total)
        area = float(area)
    except ValueError:
        raise TypeError("A colheita total e a área devem ser números.")
    
    if colheita_total <= 0 or area <= 0:
        raise ValueError(
            "A colheita total e a área deve ser um valor positivo."
            )
    return colheita_total/area
