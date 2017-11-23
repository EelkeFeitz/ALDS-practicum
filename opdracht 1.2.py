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
    assert len(s) != 0 #raises an error if s is an empty str
    number = 0
    numberList = []
    for e in s:
        if '0' <= e <= '9':
            number = number * 10 + int(e)
        else:
            if number != 0:
                numberList.append(number)
                number = 0
    if number != 0:
        #numberList.append(number)
        numberList += [number]
    return numberList


s = """ 22een123zin45 6met-63
2meerdere+7777getallen44"""
list = get_numbers(s)
print('Alle getallen:', list)