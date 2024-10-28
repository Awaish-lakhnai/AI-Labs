# (Integer)
# Program 1: Adding two integers
a = 5
b = 10
print(f"{a+b}")

# Program 2: Multiplying two integers
a = 7
b = 8
print(f"{a*b}")


#(Float)
# Program 1: Adding two float numbers
a = 5.5
b = 10.2
print(f"{a+b}")

# Program 2: Dividing two float numbers
a = 9.8
b = 2.0
print(f"{a/b}")


#(Complex)
# Program 1: Adding two complex numbers
a = 3 + 5j
b = 2 + 4j
print(f"{a+b}")

# Program 2: Multiplying two complex numbers
a = 1 + 2j
b = 3 + 4j
print(f"{a-b}")

#(Boolean)
# Program 1: Boolean comparison
is_greater = 10 > 5
print("Is 10 greater than 5?", is_greater)

# Program 2: Boolean comparison
is_greater = 15 > 10
print("Is 15 greater than 10?", is_greater)


#(Set)
# Program 1: Adding elements to a set
a = {1, 2, 3}
a.add(4)
print("Updated Set:", a)

# Program: Subtracting (removing) an element from a set
a = {1, 2, 3, 4}
a.remove(4)
print("Updated Set after Subtracting 4:", a)


#(Dict)
# Program 1: Adding key-value pairs
student = {'name': 'Soojal', 'age': 18}
student['course'] = 'IT'
print("Student Dictionary:", student)

# Program 2: Accessing dictionary values
a = {'name': 'Sara', 'course': 'IT'}
print("course:", a['course'])

#(String)
# Program 1: Concatenating strings
a = "soojal"
b = "Lakhani"
result = a + " " + b
print("Concatenated String:", result)

# Program 2: Finding string length
text = "Python Programming"
print("Length of text:", len(text))


#(List)
# Program 1: Adding elements to a list
list = [1, 2, 3]
list.append(4)
print("Updated List:", list)

# Program 2: Accessing elements in a list
fruits = ["apple", "banana", "cherry"]
print("First Fruit:", fruits[0])


#(Tuple)
# Program 1: Accessing elements in a tuple
coordinates = (10, 20)
print("X coordinate:", coordinates[0])

# Program 2: Tuple concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print("Concatenated Tuple:", result)
