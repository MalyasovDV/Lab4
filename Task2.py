from gettext import find


def find_simple_multipliers(number):
    multiplier = []
    while (number > 1):
        for i in range (2, int(number + 1)):
            if (number % i == 0):
                multiplier.append(i)
                number /= i
                break
    return multiplier

number = 20
print(number, find_simple_multipliers(number))