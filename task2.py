import random


def get_numbers_ticket(min, max, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел для лотереї.

    min: мінімальне число (не менше 1).
    max: максимальне число (не більше 1000).
    quantity: скільки чисел вибрати (від 1 до кількості чисел у діапазоні).
    Якщо параметри некоректні, повертає порожній список.
    """
    # min і max мають бути в межах 1..1000, і min не може бути більшим за max
    if not (1 <= min <= max <= 1000):
        return []

    # quantity не може бути менше 1 або більше, ніж чисел у діапазоні
    if not (1 <= quantity <= max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
