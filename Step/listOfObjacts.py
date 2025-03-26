names = ["John", "Bob", "Mosh","Sam", "Mary"]
print(names)
print(names[-2])
names[0]= "Jon"
print(names[0])
print(names[0:3])

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)


numbers2 = [1, 2, 3, 4, 5]
print(1 in numbers2) # true 1 is exist
print(len(numbers2))
