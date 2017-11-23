"""""
next_las_seq(x)
    takes a list with numbers, creates a list with the next
    'look-and-say' sequence. Returns that list

Parameters
----------
x : lst
    a list with int numbers

Returns
------
next_seq : lst
    returns a list with the next 'look-and-say' sequence
"""""
def next_las_seq(x):
    next_seq = []
    for i in range(len(x)):
        curr_num = x[i]
        if i == 0:
            prev_num = x[i] - 1
        if curr_num != prev_num:
            num_count = 1
            prev_num = curr_num
            for j in range(i+1, len(x)):
                if x[j] == curr_num:
                    num_count += 1
                else:
                    next_seq.append(num_count)
                    next_seq.append(curr_num)
                    break
    next_seq.append(num_count)
    next_seq.append(curr_num)
    return next_seq


x = [3, 3, 4, 1, 1, 6, 6, 6, 6, 1]
y = next_las_seq(x)
print("Current LAS sequence: ", x)
print("The next LAS sequence:", y)