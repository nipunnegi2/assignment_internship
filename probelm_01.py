input_numbers= input("Enter the numbers separated by spaces: ")


try:
    numbers  = map(int , input_numbers.split())
    total = sum(numbers)
    print(f"Sum of numbers is : {total}")
except ValueError:
    print("Enter valid integres.")

    
