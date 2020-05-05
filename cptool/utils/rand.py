from random import randint

RAND_MAX = 10 ** 5


def _rand():
    return randint(0, RAND_MAX)


def random(min_range=0, max_range=RAND_MAX):
    """Return a random integer in [min_range, max_range]."""
    return (
        _rand() * (RAND_MAX + 1) * (RAND_MAX + 1) * (RAND_MAX + 1)
        + _rand() * (RAND_MAX + 1) * (RAND_MAX + 1)
        + _rand() * (RAND_MAX + 1)
        + _rand()
    ) % (max_range - min_range + 1) + min_range
