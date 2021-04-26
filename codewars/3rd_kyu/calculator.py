'''
Create a simple calculator that given a string of operators (), +, -, *, / and numbers separated by spaces returns the value of that expression

Example:

Calculator().evaluate("2 / 2 + 3 * 4 - 6") # => 7
Remember about the order of operations! Multiplications and divisions have a higher priority and should be performed left-to-right. Additions and subtractions have a lower priority and should also be performed left-to-right.
'''
# PEMDAS
class Calculator(object):
    def evaluate(self, string):
        total = 0
        math_array = []
        string = string.replace(' ', '')
        for item in string:
            if item.isdigit():
                item = int(item)
                math_array.append(item)
            else:
                math_array.append(item)
        print(math_array)
        for i in range(len(math_array)):
            pass
if __name__ == '__main__':
    Calculator().evaluate( "2 / 2 + 3 * 4 - 6")#, 7)