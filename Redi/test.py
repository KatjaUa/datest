print("Hello VS Code")

# ex1
birth_year = input("enter your birth age: ")
age = 2025 - int(birth_year)
print(age)

# ex 2 plus numbers float
first = input("First: ")  #  alternativ -- first = float(input("First: "))
second = input("Second: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))


#ex 3
course = "Python for Beginners"
# print(course.upper())
print(course.find('y')) # return index if dont exist will be -1
print(course.replace('x', '4')) # replace if find
print('Python' in course) # bollean shows if it can find it


#ex 4
x = 10
x = x +3
# x +=3  the same as previpus line


y = 3 >= 2 # True
print(y) 

#ex 5 boolean expression 
price = 5
print(not price > 10)
print(price > 10 or price < 30)
print(price > 10 and price < 30)




