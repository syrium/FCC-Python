def quick_sort(integer_list):
    if len(integer_list) < 1:
        return []

    sorted_list = []

    pivot = integer_list[0]
    less_list = []
    equal_list = []
    greater_list = []

    #while len(integer_list) >= 1:
    for value in integer_list:
        if value < pivot:
            less_list.append(value)
            if len(less_list) > 1:
                less_list = quick_sort(less_list)   
        elif value > pivot:
            greater_list.append(value)
            if len(greater_list) > 1:
                greater_list = quick_sort(greater_list)
        else:
            equal_list.append(value)

    sorted_list.extend(less_list)
    sorted_list.extend(equal_list)
    sorted_list.extend(greater_list)

    print(sorted_list)
    return sorted_list

quick_sort([20, 3, 14, 1, 5])
quick_sort([83, 4, 24, 2])
quick_sort([4, 42, 16, 23, 15, 8])
quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])