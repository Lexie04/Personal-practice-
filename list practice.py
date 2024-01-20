my_list = [1, "hello", 5]
print(my_list) #Output :[1, "hello", 5]


# Printng values
fruits = ["apple","banana","cherry"]
print(fruits[1]) # Output : "banana"

# Using in Strings (String Formatting)
fruits = ["apple","banana","cherry"]
message = "My favourite fruit is {}" .format(fruits[0])
print(message) # Output : "My favourite fruit is apple"

list_length = len(fruits)
print(list_length) # Output : 3

fruits .append("mango")
print(fruits)

fruits .insert(1, "kiwi")
print(fruits)

removed_fruit = fruits .pop(1)
print(removed_fruit)
print(fruits)