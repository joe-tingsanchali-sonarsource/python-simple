def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    return average

my_list = [] # The bug is triggered here
result = calculate_average(my_list)
print(f"The average is: {result}")
