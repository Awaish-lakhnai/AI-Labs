#Write a Python function that takes a number as input and returns the sum of its digits.
def sum_of_digits(number):
    number = abs(number)
    digits = str(number)
    return sum(int(digit) for digit in digits)
num = 12345
print(f"The sum of the digits of {num} is {sum_of_digits(num)}.")


#Write a Python function that takes a sentence as input and returns the number of words in it?
def count_words(sentence):
    words = sentence.split()
    return len(words)
sentence = input("Enter a sentence: ")
print("The number of words in the sentence is:", count_words(sentence))


#Write a Python function that takes an integer and returns whether the number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter an integer: "))
print("The number is:", check_even_odd(number))