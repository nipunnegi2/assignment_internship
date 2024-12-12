def get_unique_data(lst):
    return list(set(lst)) # convert list to set , then set to list 


input_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]

unique_list = get_unique_data(input_list)

print("Unique data from the list:", unique_list)