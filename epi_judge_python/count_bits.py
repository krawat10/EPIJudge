from test_framework import generic_test


def count_bits(x: int) -> int:
    result = 0
    while x:
        result += 1
        x &= x - 1 # removes LSB bit ( 0010 &= 0001 -> 0000 )
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
