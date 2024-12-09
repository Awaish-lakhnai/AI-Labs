#Draw a Square with Asterisks
def draw_square(side_length):
    for _ in range(side_length):
        print('* ' * side_length)
side = int(input("Enter the side length of the square: "))
draw_square(side)

#Sum of Even Numbers in a List
def sum_of_evens(numbers):
    return sum(num for num in numbers if num % 2 == 0)
nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(f"The sum of even numbers is: {sum_of_evens(nums)}")

#Countdown to Zero
def countdown(number):
    while number >= 0:
        print(number)
        number -= 1
num = int(input("Enter a number to count down from: "))
countdown(num)
