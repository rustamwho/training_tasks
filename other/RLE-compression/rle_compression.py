import string
import re
import random

import pytest
from hypothesis import given, example, strategies as st

CHARACTERS = string.ascii_lowercase + string.ascii_uppercase


def replacer_zip(match: re.Match) -> str:
    # Для полученной группы букв возвращает (число повторов + символ)
    return str(match.end() - match.start()) + match.group(1)


def replacer_unzip(match: re.Match) -> str:
    # Из полученной группы (число повторов+символ) возвращает группу букв
    return int(match.group(1)) * match.group(2)


def rle_zip(unzipped: str) -> str:
    return re.sub(r'(\w)\1*', replacer_zip, unzipped)


def rle_unzip(zipped: str) -> str:
    return re.sub(r'(\d+)(\D?)', replacer_unzip, zipped)


# Tests ================================================
@given(original=st.text(alphabet=CHARACTERS, max_size=10_000, ))
@example(original='qqwwwweeeee')
def test_back_and_forth(original: str):
    assert original == rle_unzip(rle_zip(original))


@pytest.mark.parametrize('original, expected', [
    ('qqwwweeee', '2q3w4e'),
    ('foobaar', 'f2ob2ar'),
])
def test_zip(original, expected):
    assert expected == rle_zip(original)


@pytest.mark.parametrize('original, expected', [
    ('2q3w4e', 'qqwwweeee'),
    ('f2ob2ar', 'foobaar'),
])
def test_zip(original, expected):
    assert expected == rle_unzip(original)


def generate_random_string(length: int):
    rand_string = ''
    length_rand_string = 0
    while length_rand_string < length:
        rand_number = random.randint(1, length - length_rand_string)
        if rand_number > 260:
            rand_number //= 260
        rand_string += random.choice(CHARACTERS) * rand_number
        length_rand_string += rand_number
    return rand_string


for _ in range(1000):
    random_string = generate_random_string(1000)
    zipped = rle_zip(random_string)
    unzipped = rle_unzip(zipped)
    assert random_string == unzipped
