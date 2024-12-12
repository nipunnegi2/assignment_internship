def exchange_characters(string):
    if len(string)<2:
        return "String must have two characters"
    
    new_string = string[-1]+string[1:-1]+string[0]
    
    return new_string



input_string = input("Enter the string: ")

result =exchange_characters(input_string)

print("Modified String : ", result)
