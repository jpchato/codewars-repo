
'''
Write a program that can read in a list of words and convert each word into an integer, and a separate program that convert integers into words. The program should work with words up to 10 characters in length. It should generate integers in the range 0 to N^10, where N is the number of characters in the alphabet you are using. If N=26, then your maximum value would be 26^10 = 141167095653376.
'''
# 65-90
my_dict = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5,
  'f': 6,
  'g': 7,
  'h': 8,
  'i': 9,
  'j': 10,
  'k': 11,
  'l': 12,
  'm': 13,
  'n': 14,
  'o': 15,
  'p': 16,
  'q': 17,
  'r': 18,
  's': 19,
  't': 20,
  'u': 21,
  'v': 22,
  'w': 23,
  'x': 24,
  'y': 25,
  'z': 26,
}

def integerizer(word_list):
    integerized_array = []
    for word in word_list:
        word_value = 0
        for letter in word:
            # print(ord(letter))

            # integerized_array.append(ord(letter))
            word_value += ord(letter)
        integerized_array.append(word_value)
        word_value = 0
    print(integerized_array)
    return integerized_array
      
def worderizer(integerized_array):
    for number in integerized_array:
        # print(round((number/26) + 65))
        # print(chr(round((number/26) + 65)))
        print(chr(number))


if __name__ == '__main__':
    # integerizer(['dab', 'one', 'time'])
    worderizer(integerizer(['dab', 'one', 'time']))
