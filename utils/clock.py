from datetime import datetime


HOUR = 12


def get_date() -> str:
    date = datetime.now()
    return f"{date.day:02d}/{date.month:02d}/{date.year}"


def get_time() -> str:
    current_datetime = datetime.now()
    is_pm = current_datetime.hour >= 12
    formatted_hour = 12 if current_datetime.hour == 12 else current_datetime.hour % HOUR
    formatted_current_time = current_datetime.strftime(f"{formatted_hour}:%M:%S {'PM' if is_pm else 'AM'}")
    return formatted_current_time

