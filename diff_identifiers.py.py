
user_age = 25

MAX_LOGIN_ATTEMPTS = 5

_internal_status = "Active"


def calculate_total():
    return 100

class UserAccount:
    pass

print("Variable (user_age):", user_age)
print("Constant (MAX_LOGIN_ATTEMPTS):", MAX_LOGIN_ATTEMPTS)
print("Underscore Name (_internal_status):", _internal_status)
print("Function Name (calculate_total):", calculate_total.__name__)
print("Class Name (UserAccount):", UserAccount.__name__)
