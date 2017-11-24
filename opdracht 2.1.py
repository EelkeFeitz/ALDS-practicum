"""""
machtv3(a, n)
    calculates and returns the exponent of a^n

Parameters
----------
a : int
    the ground number

n : int
    the exponential

Returns
------
m: int
    the exponent of a^n
"""""
def machtv3(a, n):
    assert n > 0
    m = 1
    while n > 0:
        if n%2 == 0:
            a *= a
            n /= 2
        else:
            n -= 1
            m *= a
    return m

a = machtv3(2,11)
print(a)
