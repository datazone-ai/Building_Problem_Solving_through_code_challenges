def biggest_odd(numbers):
    odd_numbers = [int(num) for num in numbers if int(num) % 2 != 0]
    return max(odd_numbers)

print(biggest_odd)
