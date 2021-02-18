'''
https://www.codewars.com/kata/5772da22b89313a4d50012f7/train/python
Personalized greeting
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'
'''

def greet(name, owner):
    if name == owner:
        print ('Hello boss')
        return 'Hello boss'
    if name != owner:
        print ('Hello guest')
        return 'Hello guest'

if __name__ == '__main__':
    greet('Daniel', 'Daniel')
    greet('Greg', 'Daniel')