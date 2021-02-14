'''
abcd > dcba
'''

def reverse_string():
    reversed_string = ''
    string = 'abcd'
    counter = 0
    for i in range(len(string)):
        counter +=1 
        reversed_string += string[len(string) - counter]
    print(reversed_string)

if __name__ == "__main__":
    reverse_string()
