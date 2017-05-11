def search_replace(my_list, search, replace):
    new_list = []
    i = 0
    for ele in range(0, len(my_list)):  # this loop retrieves index of search
        if i == search - 1:
            i = i
            break
        i += 1
    for j in range(0, len(my_list)):  # this loop appends elements to new list
        new_list.append(my_list[j])
        if j == search - 1:
            new_list[i] = replace
    return(new_list)
