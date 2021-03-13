'''
https://www.codewars.com/kata/520446778469526ec0000001/train/python
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''
def same_structure_as(original,other):
    len_original = len(original)
    print(len_original)
    len_other = len(other)
    if len_original != len_other:
        print(False)
        return False
    
    for item in original:
        print(item)
    for item in other:
        print(other)
    pass

if __name__ == '__main__':
    # same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
    # true
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ) 
    # false