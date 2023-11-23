from datetime import datetime, timedelta

def find_next_weekday(weekday_name):
    weekdays = {'Понедельник': 0, 'Вторник': 1, 'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5, 'Воскресенье': 6}

    current_date = datetime.now()

    current_weekday = current_date.weekday()

    target_weekday = weekdays.get(weekday_name)

    days_until_target = (target_weekday - current_weekday) % 7

    if days_until_target == 0:
        days_until_target = 7

    delta = timedelta(days=days_until_target)

    next_weekday = current_date + delta

    return next_weekday

weekday_name = 'Пятница'
next_weekday_date = find_next_weekday(weekday_name)
print(f'Следующая {weekday_name} будет {next_weekday_date.strftime("%Y-%m-%d")}')