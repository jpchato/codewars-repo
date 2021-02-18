'''
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python
Introduction
The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

Task :
Given a year, return the century it is in.

Input , Output Examples ::
centuryFromYear(1705)  returns (18)
centuryFromYear(1900)  returns (19)
centuryFromYear(1601)  returns (17)
centuryFromYear(2000)  returns (20)
Hope you enjoy it .. Awaiting for Best Practice Codes

Enjoy Learning !!!
'''
import math
def century(year):
    answer = math.ceil(year/100)
    print(answer)
    return answer


if __name__ == "__main__":
    century(1705)
    century(1900)
    century(1601)
    century(2000)
    century(356)
    century(89)