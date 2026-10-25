from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Повертає список колег, яких потрібно привітати протягом найближчих 7 днів
    (включно з поточним днем).

    users: список словників з ключами name та birthday ('рік.місяць.дата').
    Якщо день народження випадає на вихідний, привітання переноситься
    на наступний понеділок.
    Повертає список словників з ключами name та congratulation_date
    ('рік.місяць.дата').
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження в цьому році; якщо вже минув, беремо наступний рік
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year
            # weekday(): субота = 5, неділя = 6, переносимо на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays


users = [
    {"name": "Марія", "birthday": "1985.10.29"},
    {"name": "Олексій", "birthday": "1990.10.31"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
