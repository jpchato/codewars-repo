def is_square(n):    
    '''
    A square of squares
    You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

    However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

    Task
    Given an integral number, determine if it's a square number:

    In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

    The tests will always use some integral number, so don't worry about that in dynamic typed languages.

    Examples
    -1  =>  false
    0  =>  true
    3  =>  false
    4  =>  true
    25  =>  true
    26  =>  false
    '''
    # print(n ** .5)
    if n < 0:
        # print(False)
        return False
    elif n == 0:
        # print(True)
        return True
    elif (n ** 0.5).is_integer():
        # .is_integer() can check if a float is an int
        # print(True)
        return True
    else:
        # print(False)
        return False

# is_square(25)#, True, "25 is a square number (5 * 5)"
# is_square( 0)#, True, "0 is a square number (0 * 0)")
# is_square( 3)#, False, "3 is not a square number"
is_square( 4)#, True, "4 is a square number (2 * 2)"  #asdf