#TASK 01:

class Car:
    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Car Info:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage} miles")

    def drive(self, miles):
        self.mileage += miles

car = Car("Toyota", "Corolla", 2020, 15000)
car.display_info()

miles_to_drive = int(input("Enter miles to drive: "))

car.drive(miles_to_drive)

car.display_info()


#TASK 02:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def average_marks(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Average Marks: {self.average_marks():.2f}")
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))

student = Student(name, age)

marks = list(map(int, input("Enter the student's marks (separated by spaces): ").split()))
student.add_marks(marks)

student.display_info()

#TASK 03:
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")

account = BankAccount("Awaish", 1000)

account.display_info()

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)

account.display_info()