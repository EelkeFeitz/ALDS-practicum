"""""
get_numbers(s)
    walks through a str and adds all the numbers in that str to a lst, then returns that lst

Parameters
----------
s : str
    a str with characters
    
Returns
------
numberList:
    a lst with all the numbers in str
"""""
def get_numbers(s):
    assert (len(s) != 0) #raises an error if s is an empty str
    number = 0
    numberList = []
    for i in range(0, len(s)):
        if (ord(s[i]) > 47 and ord(s[i]) < 58):
            number = number * 10 + int(s[i])
        else:
            if number != 0:
                numberList.append(number)
                number = 0
    if number != 0:
        numberList.append(number)
    return numberList


s = 'een123zin45 6met-632meerdere+7777getallen'
list = get_numbers(s)
print('Alle getallen:', list)