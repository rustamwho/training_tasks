"""
Given an array (arr) as an argument complete the function countSmileys that
should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes.
Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for
a nose are - or ~
Every smiling face must have a smiling mouth that should be marked
with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Example

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
"""
import re


def count_smileys(arr):
    res_count = sum(
        1 if re.match(r'[:;][-~]?[)D]', x) else 0 for x in arr)
    return res_count


def tests():
    assert count_smileys([':)', ':(', ':D', ':O', ':;']) == 2


tests()
