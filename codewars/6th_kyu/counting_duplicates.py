'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    text = text.lower()
    tracker = {
        
    }
    counter = 0
    for item in text:
        if item not in tracker:
            tracker[item] = 0
        if item in tracker:
            tracker[item] += 1
    for item in tracker:
        if tracker[item] > 1:
            counter += 1
    # print(tracker)
    # print(counter) 
    return counter
if __name__ == '__main__':
    # duplicate_count("") # 0
    # duplicate_count("abcdeaa")# 1
    duplicate_count("abcdeaB") # 2