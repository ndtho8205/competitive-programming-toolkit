from typing import Callable

# MIN_N = 1
# MAX_N = 1000000


def generate(f_rand: Callable[[int, int], int]):
    # f_rand(min_range, max_range) is a function
    # that return a pesudo-random integer
    # in [min_range, max_range]
    # print(f_rand(min_range=MIN_N, max_range=MAX_N))
    raise NotImplementedError


if __name__ == "__main__":
    generate(f_rand=lambda x, y: 3)
