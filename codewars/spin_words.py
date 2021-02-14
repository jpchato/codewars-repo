'''
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(sentence):
    sentence = "Hey fellow warriors"
    sentence_array = sentence.split()
    new_array = []
    for word in sentence_array:
        if len(word) >=  5:
            word = word[::-1]
            new_array.append(word)
        else:
            new_array.append(word)
    print(new_array)
    new_sentence = ' '.join(new_array)
    print(new_sentence)
    return new_sentence
    
if __name__ == "__main__":
    spin_words("welcome")
    