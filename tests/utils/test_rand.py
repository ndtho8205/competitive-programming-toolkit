from cptool.utils import rand

SMALL_RANGE = (10, 50)


def test_random_with_small_range():
    attempt = 10 ** 5
    generated_int = {}

    for i in range(SMALL_RANGE[0], SMALL_RANGE[1] + 1):
        generated_int[i] = 0

    for i in range(attempt):
        ans = rand.random(SMALL_RANGE[0], SMALL_RANGE[1])
        generated_int[ans] += 1

    got_min_freq = min(generated_int.values()) / attempt
    got_max_freq = max(generated_int.values()) / attempt
    expected_freq = 1.0 / (SMALL_RANGE[1] - SMALL_RANGE[0] + 1)
    tolerance = 0.001
    assert (got_max_freq - expected_freq) - (expected_freq - got_min_freq) < tolerance
