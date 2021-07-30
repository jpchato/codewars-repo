'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
Note for Go
For Go: Empty string slice is expected when there are no anagrams found.
'''

def anagrams(word, words):
    #your code here
    sanitized_list = []
    return_list = []
    for i in range(len(words)):
        # print(words[i])
        if len(word) == len(words[i]):
            # print(word, words[i])
            sanitized_list.append(words[i])
    # print(sanitized_list)
    for item in sanitized_list:
        if sorted(item) == sorted(word):
            return_list.append(item)
    print(return_list)
    return return_list

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])#, ['aabb', 'bbaa'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])#, ['carer', 'racer'])