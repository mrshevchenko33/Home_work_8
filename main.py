my_list = [1, 2, 3, 4, 5]


mid = len(my_list) // 2


if len(my_list) % 2 == 0:
    first_list = my_list[:mid]
    second_list = my_list[mid:]
else:
    first_list = my_list[:mid + 1]
    second_list = my_list[mid + 1:]


new_list = [first_list, second_list]

print(new_list)
