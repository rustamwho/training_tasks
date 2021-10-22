"""
The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned. Valid
decimal values for RGB are 0 - 255. Any values that fall out of that range
must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3
will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r, g, b):
    result = ''
    for x in (r, g, b):
        if x < 0:
            x = 0
        if x > 255:
            x = 255
        hex_x = str(hex(x)).split('x')[1].upper()
        hex_x = '0' + hex_x if len(hex_x) < 2 else hex_x
        result += hex_x
    return result


# best practice
def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


def tests():
    assert rgb(255, 255, 255) == 'FFFFFF'


tests()
