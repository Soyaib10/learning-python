friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
numbers = [1, 2, 3, 4]
print(friends[-1]) #prints last element
print(friends[1: 3]) #[index, desired], prints upto 3
friends.append("Creed") # add at end
friends.insert(1, "Kelly") #index_name, element
friends.remove("Jim")
friends.extend(numbers)
friends.pop()
print(friends)
print(friends.index("Oscar"))
print(friends.count("Oscar"))
print(numbers.sort())
print(friends)
print(numbers)
friends2 = friends.copy()
print(friends2)
