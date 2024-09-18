def dens_agri(numero_plantas, area):
    """
    Calcula a densidade de plantio, que é o número de plantas por hectare.
    Args:
        numero_plantas (int): O número total de plantas.
        area (float): Área cultivada em hectares (ha).
    Returns:
        float: A densidade de plantio em plantas/hectare.
    Raises:
        ValueError: Se `numero_plantas` for menor ou igual a zero, ou `area` 
        for menor ou igual a zero.
    """
    try:
        numero_plantas = int(numero_plantas)
        area = float(area)
    except ValueError:
        raise TypeError("O numero_plantas e a área devem ser números.")
    
    if numero_plantas <= 0 or area <= 0:
        raise ValueError(
            "O número de plantas e a area deve ser maior que zero."
            )
    return numero_plantas/area