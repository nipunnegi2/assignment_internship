def frequency_calculation(input_list):
    frequency_dict={}

    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] +=1
        else:
            frequency_dict[item] = 1
    
    return frequency_dict
input_list =[1,2,2,3,3,2,3,2,1,5,6]
frequency_dict=frequency_calculation(input_list)

print("Frequencies of elements in the list: ")
print(frequency_dict)