"""""
zeef_van_eratosthens(lst)
    walks through a lst and adds all the prime numbers in that list to anohter list, and returns that list.

Parameters
----------
lst : lst
    a lst with int numbers

Returns
------
returnList:
    a lst with all the prime numbers out of lst
"""""
def zeef_van_eratosthenes(lst):
    check_list = [True for i in range(0, len(lst))]
    return_list = []
    for i in range(0, len(lst)):
        if check_list[i]:
            for j in range(2, lst[i]+1):
                if j == lst[i]:
                    return_list.append(lst[i])
                    break
                if int(lst[i] / j) * j == lst[i]:
                    check_list[i] = False
                    break
    return return_list


longList = [i for i in range(2, 1002)]
primeList = zeef_van_eratosthenes(longList)
print('Opdracht 3: De priemgetallen tussen 2 en 1000 zijn:', primeList)
