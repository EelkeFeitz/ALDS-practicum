import random

"""""
create_lists(amount, length, lower_range, upper_range)
    creates a list with 'amount' of sub-lists that contain 'length' amount of elements
    with random generated int's withing the 'lower_range' and 'upper_range'

Parameters
----------
amount: int
    the amount of sub-list generated 

length: int
    the length of each sub-list

lower_range: int
    the lower range of the random generated numbers that fill the sub-lists

upper_range: int
    the upper range of the random generated numbers that fill the sub-lists
    

Returns
------
super_list:
    a lst filled with sub-list which contain random generated int's
"""""
def create_lists(amount, length, lower_range, upper_range):
    super_list = []
    for i in range(0, amount):
        sub_list = []
        for j in range(0, length):
            element = random.randint(lower_range, upper_range)
            sub_list.append(element)
        super_list.append(sub_list)
    return super_list


"""""
checkoverlay(lst)
    walks through a list and checks if there is overlay within the sub-lists

Parameters
----------
lst : lst
    a lst with sub-lists that contain int's

Returns
------
overlay:
    an int that indicates how many sub-lists have multiple of the same numbers
"""""
def check_overlay(lst):
    overlay = 0
    for i in range(0, len(lst)):
        if len(set(lst[i])) < len(lst[i]):
            overlay += 1
#        for j in range(0, len(lst[i])):
#            for k in range(j, len(lst[i])):
#                if lst[]
    return overlay

studenten = create_lists(100, 23, 1, 365)
overlay = check_overlay(studenten)
print("Het aantal lijsten met hetzelfde cijfer:",overlay)