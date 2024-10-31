def find_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_even_numbers(numbers_list))
