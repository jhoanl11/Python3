def string_or_int(number):
    if type(number) == int:
        raise RuntimeError("This is not a string")
    else:
        print("Thank you for your string")


def check_positive(number2):
    if number2 < 0:
        raise RuntimeError("Number must be valid")
    else:
        print("This number is positive")

string_or_int("hola")

check_positive(2)
