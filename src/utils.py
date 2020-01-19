from random import randint

RAND_MAX = 1000000


def _rand():
    return randint(0, 32767)


def random():
    return (
        _rand() * (RAND_MAX + 1) * (RAND_MAX + 1) * (RAND_MAX + 1)
        + _rand() * (RAND_MAX + 1) * (RAND_MAX + 1)
        + _rand() * (RAND_MAX + 1)
        + _rand()
    )
