"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.


"""

import string

def rot13(message):
    first_part = string.ascii_lowercase[:13]
    #print first_part
    second_part = string.ascii_lowercase[13:]
    #print second_part
    first_part_c = string.ascii_uppercase[:13]
    #print first_part_c
    second_part_c = string.ascii_uppercase[13:]
    #print second_part_c
    crypto_msg = ""
    for i in message:
        if i in first_part:
            crypto_msg += second_part[first_part.index(i)]
        elif i in second_part:
            crypto_msg += first_part[second_part.index(i)]
        elif i in first_part_c:
            crypto_msg += second_part_c[first_part_c.index(i)]
        elif i in second_part_c:
            crypto_msg += first_part_c[second_part_c.index(i)]
        else:
            crypto_msg += i
    return crypto_msg

#print(rot13("HE1LLO"))
