import re


def validate(s):
    result = re.match(r'\d+\.\d+\.\d+\.\d+', s)
    return result.group() == s if result else False


print(validate('192.168.1'))
