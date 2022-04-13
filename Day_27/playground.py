def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
#
#
# add(3, 5, 6)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)