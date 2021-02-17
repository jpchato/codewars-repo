'''
It's 9 time!

I want to count from 1 to n. How many times will I use a '9'?

9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc

Note: n will always be a positive integer.

count_nines(8) == 0
count_nines(9) == 1
count_nines(10) == 1
count_nines(98) == 18
count_nines(100) == 20
'''

def count_nines(n):
    counter = 0
    for i in range(n):
        if '9' in str(i+1):
            print ('nine is in', str(i+1))
            for item in str(i+1):
                if item == '9':
                    counter += 1
    print('counter', counter)
    return counter

if __name__ == "__main__":
    count_nines(9)
    count_nines(100)
    count_nines(200)