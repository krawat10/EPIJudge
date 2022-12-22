import sys

from test_framework import generic_test


def reverse_bits(x: int) -> int:
    i = 0
    j = 64 - 1

    result = 0
    while i < j:
        result |= ((x >> i & 1) << j) | (x >> j & 1) << i

        i += 1
        j -= 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
