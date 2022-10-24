from gettext import find


def find_simple_multipliers(number):
    multiplier = []
    while (number > 1):
        for i in range (2, number):
            if (number % i == 0):
                multiplier.append(i)
                number /= i
    return multiplier

print(find_simple_multipliers(20))