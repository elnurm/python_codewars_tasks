"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
and returns the same string with all even indexed characters in each word upper cased,
and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

even = cut
odd  = tek

"""

def to_weird_case(msg):
    import re
    weird_str = []
    msg_list = re.split(r'(\W+)', msg)
    for _ in msg_list:
        for i in range(len(_)):
            if i % 2 == 0:
                weird_str += _[i].upper()
            elif _[i] == ' ':
                weird_str += ' '
            else:
                weird_str += _[i].lower()
    return ''.join(weird_str)

print to_weird_case("WeIrD StRiNg CaSe")
