
my_list = [13, 666, -666]
sorted_list1 = sorted(my_list)

# Implementing custom sorting function (using Bubble Sort for simplicity)
def custom_sort(input_list):
    list_copy = input_list[:]
    n = len(list_copy)

    # Bubble Sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_copy[j] > list_copy[j + 1]:
                # Swap if the element found is greater than the next element
                list_copy[j], list_copy[j + 1] = list_copy[j + 1], list_copy[j]

    return list_copy

sorted_list2 = custom_sort(my_list)

# Printing the sorted lists
print("sorted_list1:", sorted_list1)
print("sorted_list2:", sorted_list2)
