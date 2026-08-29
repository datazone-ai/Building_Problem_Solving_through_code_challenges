def convert_add(numbers):
    
    integers = [int(number) for number in numbers]
    return sum(integers)

result = convert_add(["1", "3", "5"])
print(result)