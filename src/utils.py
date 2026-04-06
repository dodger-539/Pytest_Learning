def is_even(number):
    """Возвращает True, если число четное, иначе False."""
    return number % 2 == 0

# src/checker.py
def check_sign(number):
    if number > 0:
        return "positive"
    else:
        return "zero or negative"