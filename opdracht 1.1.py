"""""
my_max(a)
    walks through a list and returns the highest number

Parameters
----------
a : lst
    a list with int's

------
highest: int
    returns the highest int in the list
"""""
def my_max(a):
    assert len(a) != 0  # raises an error if a is an empty lst
    highest = a[0]
    for i in a:
        assert type(i) == int or type(i) == float
        if i > highest:
            highest = i
    return highest


a = [1, 2, 3, 4, 5.0]
b = my_max(a)
print('opdracht 1: the highest number in a =', b)
