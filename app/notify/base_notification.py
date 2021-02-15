import re

notifications = list()

def add_notification(message):
    this.notifications.append({'message': message})

def is_true(value, message):
    if value:
        this.notifications.append({'message': message})

def is_required(value, message):
    if not value or len(value) <= 0:
        this.notifications.append({'message': message})

def has_min_len(value, min, message):
    if not value or len(value) < min:
        this.notifications.append({'message': message})

def has_max_len(value, max, message):
    if not value or len(value) > max:
        this.notifications.append({'message': message})

def is_fixed_len(value, bigger, message):
    if len(value) != bigger:
        this.notifications.append({'message': message})

def is_email(value, message):
    reg_exp = re.compile(r"/^\w + ([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/");
    if not reg_exp.findall(value):
        this.notifications.append({'message': message})

def get_all_notifications():
    return this.notifications

def valid():
    return this.notifications.length == 0