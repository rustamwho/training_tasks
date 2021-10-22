"""
What is an anagram? Well, two words are anagrams of each other if they both
contain the same letters. For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words. You should return
an array of all the anagrams or an empty array if there are none. For example:
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) =>
['carer', 'racer']
"""
from collections import Counter

import pytest


def anagrams(word, words):
    result = []
    counts_init = Counter(word)
    for input_word in words:
        if counts_init == Counter(input_word):
            result.append(input_word)
    return result


# best practice
def anagrams2(word, words):
    return [item for item in words if sorted(item) == sorted(word)]


@pytest.mark.parametrize('word, words, expected', [
    ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'],
     ['carer', 'racer']),
    ('abba', ['aabb', 'abcd', 'bbaa', 'dada'],
     ['aabb', 'bbaa'])

])
def tests(word, words, expected):
    assert expected == anagrams(word, words)
