'''
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(input_str):
    my_dictionary = {
        'a' : 'a',
        'e' : 'e',
        'i' : 'i',
        'o' : 'o',
        'u' : 'u',
        
    }
    num_vowels = 0
    # your code here
    for item in input_str:
        if item in my_dictionary:
            num_vowels += 1
    print(num_vowels)
    return num_vowels

if __name__ == '__main__':
    get_count("abracadabra")
    # 5