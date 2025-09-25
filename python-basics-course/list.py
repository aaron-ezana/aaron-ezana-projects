friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends[0])
print(friends[-1]) # prints last item
print(friends[1:4]) # prints from index 1 to 3
friends[1] = "Mike" # change item at index 1
friends.extend(["Creed", "Kelly"]) # add multiple items to end of list
friends.append("Pam") # add single item to end of list
friends.insert(1, "Kelly") # add item at specific index
friends.remove("Kevin") # removes first occurrence of Karen
friends.pop() # removes last item
print(friends.index("Jim")) # returns index of first occurrence of Jim
print(friends.count("Jim")) # counts how many times Jim appears in list
friends.sort() # sorts list in alphabetical order
friends.reverse() # reverses order of list
friends2 = friends.copy() # makes a copy of friends list
print(len(friends)) # prints length of list
print(friends.clear()) # clears the list