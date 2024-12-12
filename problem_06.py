def shift_zeroes_to_beginning(list):
    zeroes = list.count(0) 
   
    list = [x for x in list if x != 0]
   
    return [0] * zeroes + list

# Example usage
list = [0, 0, 6, 7, 9, 0, 6, 4, 3, 0]
result = shift_zeroes_to_beginning(list)
print(result)