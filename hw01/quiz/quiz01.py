def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    n = 1
    while True:
        if n % a == 0 and n % b == 0:
            return n
        n += 1

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    c = 0
    for x in range(0, 10):
        if has_digit(n, x):
            c += 1
    return c
        

def has_digit(n, k):
    while n > 0:
        if n % 10 == k:
            return True
        n //= 10
    return False
