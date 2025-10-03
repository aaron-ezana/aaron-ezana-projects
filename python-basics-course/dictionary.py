dictionary = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer",
    "hobby": "Photography",
    "is_student": False
}

print(dictionary["name"])
print(dictionary.get("abc", "Not Found")) # Default value printed because key doesn't exist
print(dictionary.get("is_student")) # Default value is None because key exists