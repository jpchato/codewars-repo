'''
Substitute two equal letters by the next letter of the alphabet (two letters convert to one):

"aa" => "b", "bb" => "c", .. "zz" => "a".
The equal letters do not have to be adjacent.
Repeat this operation until there are no possible substitutions left.
Return a string.

Example:

let str = "zzzab"
    str = "azab"
    str = "bzb"
    str = "cz"
return "cz"
Notes
The order of letters in the result is not important.
The letters "zz" transform into "a".
There will only be lowercase letters.
If you like this kata, check out another one: Last Survivor Ep.3
'''

def last_survivors(string):
    new_string = string
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == string[j]:
                new_string = string.replace(string[i],'')
                new_string = string.replace(string[j],'')
    print(new_string)

if __name__ == '__main__':
    last_survivors("zzzab")#cz
