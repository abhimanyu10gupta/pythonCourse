friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.append("Mikey")
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

friends2= friends.copy()
print(friends2)

friends.sort()
print(friends)

friends.extend(lucky_numbers)
friends.insert(2, "Neo")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kevin"))

print(friends.count("Neo"))

friends.clear()
print(friends)


