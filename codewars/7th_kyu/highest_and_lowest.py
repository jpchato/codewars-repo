'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    number_list = numbers.split(' ')
    # print(number_list)
    highest = int(number_list[0])
    lowest = int(number_list[0])
    for number in number_list:
        # print((number))
        if int(number) >= highest:
            highest = int(number) 
        if int(number) <= lowest:
            lowest = int(number)   
    # print(highest, lowest)
    return (str(highest) + ' ' + str(lowest))

# high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")#, "542 -214"
high_and_low("1 1")#, "1 1")