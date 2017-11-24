def my_bin(n):
    assert n >= 0
    if n == 0:
        return ''
    return my_bin(n//2) + str(n % 2)


a = 1
b = my_bin(a)
print("Binairy sting van:", a,"is:", b)
