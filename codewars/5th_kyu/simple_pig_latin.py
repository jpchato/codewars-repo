'''
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''
def pig_it(text):
    new_array = []
    for word in text.split():
        if word != '?' and word != '.' and word != '!':
            new_array.append(word[1::] + word[0] + 'ay' )
        else:
            new_array.append(word)
    new_string = ' '.join(new_array)
    # print (new_string)
    return new_string

if __name__ == '__main__':
    # pig_it('Pig latin is cool')
    # pig_it('This is my string')
    pig_it('Quis custodiet ipsos custodes ?')