friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends.append("Rohit") # list are mituable and strings are immutable
print(friends)

l1 = [1, 34,62, 2, 6, 11] # [1, 2, 6, 11, 34, 62]
l1.sort()
print(l1)

l1 = [1, 34,62, 2, 6, 11] # [11, 6, 2, 62, 34, 1]
l1.reverse()
print(l1)

l1 = [1, 34,62, 2, 6, 11] 
# l1.insert(3, 333333) # insert 333333 such that its index in the list is 3
# value = l1.pop(3)
l1.remove(62) # remove methods 
print(l1)

