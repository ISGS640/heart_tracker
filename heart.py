
from datetime import datetime

MESSAGE_NORMAL = 'Нормальная активность! Продолжайте движения.'
MESSAGE_WARNING = 'Осторожно успокойтесь!'
MESSAGE_DANGER = 'Осторожно что-то не так! Обратитесь к врачу.'
MESSAGE_LOW = 'Главное — быть активным!'
storage_data = {}
last_time = None
def check_correct_data(package):
    global last_time
    if len(package) != 2:
        return False
    if not all(package):
        return False
    time_str, heart_rate = package
    try:
        time_obj = datetime.strptime(time_str, '%H:%M:%S')
    except ValueError:
        return False
    if last_time and time_obj <= last_time:
        return False
    last_time = time_obj
    return True
def accept_package(package):
    if not check_correct_data(package):
        return storage_data
    time_str, heart_rate = package
    storage_data[time_str] = heart_rate
    print(f"\nВремя: {time_str}.")
    print(f"Частота сердечных сокращений за сегодня: {heart_rate} уд/мин.")
    if heart_rate >= 100:
        print(MESSAGE_DANGER)
    elif heart_rate >= 80:
        print(MESSAGE_WARNING)
    elif heart_rate >= 60:
        print(MESSAGE_NORMAL)
    else:
        print(MESSAGE_LOW)
    print("")
    return storage_data