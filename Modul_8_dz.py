
from datetime import datetime

users = [{'Andrii': '2022-08-01'},
         {'Ivan': '2022-08-06'},
         {'Ira': '2022-08-04'},
         {'Petro': '2022-08-03'},
         {'Bill': '2022-08-03'}]
DAYS_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday', 'Monday']

def get_birthdays_per_week(users):

    new_dict = {}

    for birthday_boy in users:
        for name, birthday in birthday_boy.items():
            birthday = datetime.strptime(birthday, '%Y-%m-%d')
            day_birthday = DAYS_WEEK[birthday.weekday()]
            if day_birthday not in new_dict:
                new_dict[day_birthday] = []
            new_dict[day_birthday].append(name)

    for day, name in new_dict.items():
        print(f"{day}: {(', '.join(name))}")

if __name__ == '__main__':
    get_birthdays_per_week(users)