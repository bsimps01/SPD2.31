# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace nested conditional with guard clases.
ADJ_FACTOR = 0.7

def get_result(income, duration):
    return (income / duration) * ADJ_FACTOR

def get_adjusted_capital(capital, rate, duration, income):
    if (capital > 0):
        get_result(income, duration)
    if (rate > 0 and duration > 0):
        get_result(income, duration)
    
    return get_result(income, duration)

adjusted_capital = get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital)