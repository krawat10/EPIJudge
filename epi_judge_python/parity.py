from test_framework import generic_test


# 26, 4.1

# Brute Force
# def parity(x: int) -> int:
#     result = 0
#     while x:  # O(n)
#         result ^= x & 1 # ^= is XOR and flips odd numbers
#         x >>= 1
#     return result

# x & (x - 1) equal x without lowest bit (1011 -> 1010)
# def parity(x: int) -> int:
#     result = 0
#     while x:  # O(n)
#         result ^= 1  # flip to get odd/even
#         x &= x - 1  # removes LSB every time (1110 -> 1100 -> 1000 -> 0000 -> stop)
#     return result

# log(n) approach
# parity of 1101'0111 is the same as parity 1101 XOR 0111 = 1010
# parity of 10'10 is the same as parity 10 XOR 10 = 00
# parity of 0'0 is the same as parity 0 XOR 0 = 0
def parity(x: int) -> int:
    x ^= x >> 32  # 1101'0111 XOR 0000'1101 -> 1101'1010
    x ^= x >> 16  # 110110'10 XOR 001101'10 -> ...
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1  # we check LSB


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
