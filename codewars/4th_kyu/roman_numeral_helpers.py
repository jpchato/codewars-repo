'''
Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
'''



class py_solution:
    def roman_to_int(self, s):
        rom_val = {
        'I':	1,
        'V':	5,
        'X':	10,
        'L':	50,
        'C':	100,
        'D':	500,
        'M':	1000,

        }
        int_val = 0
        for i in range(len(s)):
            # print(s[i])
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                # print(int_val)
            else:
                int_val += rom_val[s[i]]
                # print(int_val)
        return int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))