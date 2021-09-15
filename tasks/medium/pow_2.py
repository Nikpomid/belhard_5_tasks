"""
Проверить, является ли число степенью двойки.
Вернуть True или False

is_pow_2(1) -> True
is_pow_2(2) -> True
is_pow_2(16) -> True
is_pow_2(256) -> True
is_pow_2(1024) -> True
is_pow_2(13) -> False
is_pow_2(17) -> False
"""
from math import log


def is_pow_2(number) -> bool:
    x = log(number, 2)
    if x == int(x):
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_pow_2(4)
    assert is_pow_2(16)
    assert is_pow_2(256)
    assert not is_pow_2(123)
    print("Решено")
