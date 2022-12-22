from test_framework import generic_test


def swap_bits(x, i, j):
    if (x >> i & 1) != (x >> j & 1):  # check if bits differ (1 and 0 or 0 and 1)
        bit_mask = (1 << i) | (1 << j)  # 011101 (i is 0, j is 5) -> 1xxxx1 -> 100001
        x ^= bit_mask  # 011101 XOR 100001 -> 111100

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
