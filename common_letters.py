"""
Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
The letters in the returned list should be unique. For example

common_letters("banana","cream")
common_letters("elnur","ilgar") == > ['l']
should return ['a']

"""
#/usr/bin/env python

def common_letters(string1,string2):
    unique_letters = []
    for letter in string1:
        if letter in string2:
            unique_letters += letter
    return unique_letters
    if unique_letters == []:
        return "There is no unique letter"


print common_letters("elnur","ilgar")
