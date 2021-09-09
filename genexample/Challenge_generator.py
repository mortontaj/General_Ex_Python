def odd_only(CC):
    """
    Odd numbers below the entered number

    :param CC: The largest non included int

    :return: All odd numbers up to but including
        the entered number
    """
    if CC % 2 == 0 & CC > 0:
        CC -= 1
    if CC < 0:
        CC = 0
    while CC % 2 == 1:
        yield CC
        CC -= 2
        if CC == -1:
            break


def oddnumber():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = oddnumber()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()

# Approximates the value of pi as the range increases
for x in range(100000):
    print(next(approx_pi))

for x in range(10):
    print(next(oddnumber))

for x in range(10):
    print(next(odd_only(x)))
