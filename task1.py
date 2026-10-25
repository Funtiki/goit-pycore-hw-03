from datetime import datetime


def get_days_from_today(date):
    """
    Повертає кількість днів від заданої дати до поточної.

    Параметр date: рядок у форматі 'РРРР-ММ-ДД'.
    Якщо дата в минулому, результат додатний, якщо в майбутньому, від'ємний.
    Якщо формат дати неправильний, повертає повідомлення про помилку.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Невірний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД."
    # toordinal() дає номер дня, тому час (години, хвилини) ігнорується
    today = datetime.today()
    difference = today.toordinal() - given_date.toordinal()
    return difference


print(get_days_from_today("2014-08-01"))
print(get_days_from_today("2034-08-01"))
print(get_days_from_today("2014.08.01"))
