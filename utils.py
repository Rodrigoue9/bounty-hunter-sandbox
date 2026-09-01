def calculate_discount(price: float, discount_percentage: float) -> float:
    """
    Calcula o preço final aplicando a porcentagem de desconto.
    """
    return price * (1.0 - (discount_percentage / 100.0))
