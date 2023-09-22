#!/usr/bin/env python3

import re

# ukol za 2 body
def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd 
       numbers.

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    >>> first_odd_or_even([1,1,1,1,6,3])
    6
    >>> first_odd_or_even([2])
    0
    >>> first_odd_or_even([333,14,29,15])
    14
    """
    
    count_odd = 0
    count_even = 0
    for x in numbers:
        if x % 2:
            if count_odd == 0:
                first_odd = x
            count_odd+=1
        else:
            if count_even == 0:
                first_even = x
            count_even+=1
    if count_odd == 0 or count_even == 0 or count_even == count_odd:
        return 0
    elif count_even < count_odd:
        return first_even
    else:
        return first_odd


# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
    word = list(word.upper())
    pilot_alpha_list = [i for char in word for i in pilot_alpha if i.startswith(char)]
    

    return pilot_alpha_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
