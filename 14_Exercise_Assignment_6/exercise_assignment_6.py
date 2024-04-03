# EA 6
# Paul Wade

# CHAPTER 9

# 1. Create a tuple named integer_tuple that contains the even integer values between -20 and -10.
# The tuple should start with -20 and end with -10 (3 pts.).

integer_tuple = (-20, -18, -16, -14, -12, -10)


# 2. Use indexing to print the value -12 (1 pt.).

print(integer_tuple[4])


# 3. Use slicing to print (-14, -12, -10) (2 pts.).

print(integer_tuple[3:])


# 4. Iterate over the integer_tuple using a for in loop to display each integer in the tuple
# on a separate line (2 pts.).

for item in range(len(integer_tuple)):
	print(integer_tuple[item])


# 5. Create a list named fruit_list that contains Strawberry and Banana, print the list (2 pts).

fruit_list = ["Strawberry", "Banana"]
print(fruit_list)


# 6. Add Grapes to the list using the append function, print the list (2 pts.).

fruit_list.append('Grapes')
print(fruit_list)


# 7. Insert Watermelon into the list at index 2 ( 1 pt.).
fruit_list.insert(2, "Watermelon")
print(fruit_list)


# 8. Write an if statement using the keyword in to determine if Apple is in the list.  If Apple is in the list,
# print out: Apple is in the list. If Apple is not in the list print out: Apple is not in the list (2 pts.).

if "Apple" in fruit_list:
	print("Apple is in the list")
else:
	print("Apple is not in the list")


# 9. Use a for in loop to print the fruits in the list, each fruit should be printed on the same line with a space
# after each fruit (2 pts.).

for fruit in fruit_list:
	print(fruit, end=" ")


# 10. Use the extended function to add Orange, Kiwi and Mango to the list, print the list (2 pts.).
print()  # Do not delete this line

fruit_list.append("Orange")
fruit_list.append("Kiwi")
fruit_list.append("Mango")
print(fruit_list)


# 11. Replace Banana with Plantain in the list using indexing (1 pt.).

fruit_list[fruit_list.index("Banana")] = "Plantain"


# 12. Remove Grapes from the list using the pop function, print the list (2 pts.).
fruit_list.pop(fruit_list.index("Grapes"))

print(fruit_list)

# 13. Use slicing to print the names Plantain, Watermelon, Orange (1 pt.).
print(fruit_list[1:4])


# 14. Create a list named integer_list that contains the odd integers values -25 through -11 using
# a list comprehension and the step value in the range.  The list should start with -25
# and end with -11. Print the list (2 pts.).

integer_list = [*range(-25, -9, 2)]      # I could have used stop value of -10 here, but less readable
print(integer_list)
