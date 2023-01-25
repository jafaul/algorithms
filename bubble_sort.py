lst = [5, 7, 4, 6, 9, 2]
print(lst)
n = len(lst)

count = 0

for run in range(n - 1):
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            count += 1
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(count)
print(lst)

# or other way by book:
def find_smallest(lst):
    smallest = lst[0]
    # smallest = 5
    # smallest = 3; smallest = lst[2], smallest_index = 2 instead 0
    smallest_index = 0
    for index_item in range(1, len(lst)):
        # index_item = 1 - don't suit
        # index_item = 2
        if lst[index_item] < smallest:
            smallest = lst[index_item]
            smallest_index = index_item
    return smallest_index


def selection_sort(lst):
    new_arr = []
    for index_item in range(len(lst)):
        smallest = find_smallest(lst)
        new_arr.append(lst.pop(smallest))
    return new_arr


print(selection_sort([5, 6, 3, 2, 10]))
