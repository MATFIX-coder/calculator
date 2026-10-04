def add_numbers(a: float, b: float) -> float:
    """Складывает два числа и возвращает результат суммы"""
    return a + b

def divide(a, b):
    if b == 0:
        return "На ноль делить нельзя"
    return a / b

print(add_numbers(1, 2))
print(divide(4, 2))
print(divide(4, 0))