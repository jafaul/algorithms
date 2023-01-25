def binary_search(lst, item):
    low_index = 0
    high_index = len(lst) - 1

    while low_index <= high_index:
        middle_index = (low_index + high_index) // 2
        guess = lst[middle_index]
        if guess == item:
            return middle_index
        elif guess > item:
            high_index = middle_index
        else:
            low_index = middle_index

lst = []
[lst.append(i + 20) for i in range(100)]
print(lst)
print(len(lst))
#len(lst) == 1000
# max(index(lst)) == 999
# min(index(lst)) == 0
print(binary_search(lst, 66))


