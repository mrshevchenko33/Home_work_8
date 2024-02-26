my_list = [0, 1, 7, 2, 4, 8]

my_num = 0

if my_list:
    for i in my_list[::2]:
        my_num += i
        result = my_num * my_list[-1]
else:
    result = 0
print(result)