str_list = ['sonam', 'pooja', 'apple', 'papa']
i = 0
while i < len(str_list):
    j = 0
    while j < len(str_list)-1:
        if str_list[j] > str_list[j + 1]:
            str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
        j = j+1
    i = i+1
print(str_list)
