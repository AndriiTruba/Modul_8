
from datetime import datetime, timedelta

users = [{'Andrii': '2022-08-01'},
         {'Bob': '2022-07-30'},
         {'Artem': '2022-07-29'},
         {'Kim': '2022-07-27'},
         {'Ivan': '2022-08-06'},
         {'Ira': '2022-08-04'},
         {'Petro': '2022-08-03'},
         {'Bill': '2022-08-03'}]

DAYS_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday', 'Monday']

def period_birthdays_per_week(data):
    
    date_mondey = datetime.strptime(data, '%Y-%m-%d')
    if date_mondey.weekday() != 0:
        print('Введена дата не є понеділком введіть коректну дату!')

    start = date_mondey.date() - timedelta(days=2)
    finish = date_mondey.date() + timedelta(days=4)
    return start,  finish


def get_birthdays_per_week(users):
    new_dict = {}
    start, finish = period_birthdays_per_week(input(f'Введіть дату понеділка потрібного тижня в форматі РРРР-ММ-ДД: '))
    if start.weekday() != 5:
        return None
    for birthday_boy in users:
        for name, birthday in birthday_boy.items():
            birthday = datetime.strptime(birthday, '%Y-%m-%d')
            if start <= birthday.date() <= finish:
                day_birthday = DAYS_WEEK[birthday.weekday()]
                if day_birthday not in new_dict:
                    new_dict[day_birthday] = []
                new_dict[day_birthday].append(name)

    for day, name in new_dict.items():
        print(f"{day}: {(', '.join(name))}")

if __name__ == '__main__':
    get_birthdays_per_week(users)