def sym(list_one, list_two):
    new_list = []
    
    for item in list_one:
        if item not in list_two and item not in new_list:
            new_list.append(item)
    for item in list_two:
        if item not in list_one and item not in new_list:
            new_list.append(item)
    print(new_list)
    new_list
    return new_list
if __name__ == '__main__':
    sym([1, 2, 3], [5, 2, 1, 4])
    # [3,4,5]
    sym([1, 2, 3, 3], [5, 2, 1, 4])
    # [3, 4, 5]