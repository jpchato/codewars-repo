'''
You are given three strings, “kasjfhhi” “yyjknaalkjs” “anewunnsii”. Using your favorite language, write a function called repeatedChar which returns the first letter of each string that occurs twice in a row in a new string.
Example #1: 
Input : “kasjfhhi”
Output : h
Example #2: 
Input : “yyjknaalkjs”
Output : y
Example #3: 
Input:  “anewunnsii”
Output : n

'''

def repeatedChar(string1):
    solutions_string = ''

    for i in range(len(string1) - 1):
        if string1[i] == string1[i+1]:
            solutions_string += string1[i]
            break
        continue

    print(solutions_string)
    return solutions_string

if __name__ == '__main__':
    # repeatedChar('acahyshn', 'yyjknaalkjs', 'anewunnsii')
    repeatedChar('acahyshn')
    repeatedChar('yyjknaalkjs')
    repeatedChar('anewunnsii')