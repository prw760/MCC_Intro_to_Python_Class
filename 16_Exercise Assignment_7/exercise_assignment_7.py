# EA 7
# Paul Wade

# CHAPTER 9 and Sets

# 1. Create a dictionary called users, that includes the user name as the key and password as the value.
# Both the user name and password should be strings (3 pts.).
# The dictionary should contain: tatkinson - !2054570Athu, jcarter - 2#064636Cjas, hcheloa - 66$90154Chan,
# kmcphee - 206@2113Mkar, npeterson - 2052&833Pnic

users = {"tatkinson": "!2054570Athu",          # one entry per line for PEP 8 readability
         "jcarter": "2#064636Cjas",
         "hcheloa": "66$90154Chan",
         "kmcphee": "206@2113Mkar",
         "npeterson": "2052&833Pnic"}


# 2. Print the dictionary (1 pt.).
print(users)


# 3. Write a for in loop that prints the keys in the dictionary (2 pts.).

for key in users.keys():
	print(key)


# 4. Write a for in loop that prints the values in the dictionary (2 pts.).
for value in users.values():
	print(value)


# 5. Write a for in loop that assigns the keys and values to seperate variables and prints the following
# line for each user in the dictionary: "User user name has a password of  password."
# eg. User tatkinson has a password of !2054570Athu. (3 pts.)
for key, value in users.items():
	print("User", key, "has a password of", value)


# 6. Write an if statement using the keywords not in to determine if user name pwheeler is in the dictionary.
# If pwheeler is not in the dictionary, print out "User pwheeler is not in the dictionary.",
# else print out "User pwheeler is in the dictionary." (2 pts.).

user_name_for_search = "pwheeler"  # Using variable because it Seemed weird to hard-code
                                   # the username in the print statements

if user_name_for_search in users:
	print (user_name_for_search, "is in the dictionary")
else:
	print(user_name_for_search, "is not in the dictionary")


# 7. User kmcphee has updated their password to 2100606^Wpat. Update kmchphee's entry in the dictionary
# to reflect the password change (1 pt.).

users.update({"kmcphee": "2100606^Wpat"})


# 8. Add User asaris with a password of 20178*07Saly to the dictionary and add mkholay
# with a password of 204736?5Kmal to the dictionary (2 pts.).

users["asaris"] = "204736?5Kmal"


# 9. User tatkinson has retired, remove their entry from the dictionary.  Print the dictionary (2 pts.).
users.pop("tatkinson")
print(users)


# 10. Write code to create a set named set_a with the following floats: 1.50, 36.32, 60.00, 72.68, 84.79 (2 pts.).
set_a = {1.50, 36.32, 60.00, 72.68, 84.79}


# 11. Write code to create a set named set_b with the following floats: 12.50, 24.75, 36.32, 48.84, 60.00 (2 pts.).
set_b = {12.50, 24.75, 36.32, 48.84, 60.00}


# 12. Write code that creates another set containing only the elements that are found in both set_A and set_b,
# and assigns the resulting set to the variable set_c.  Print set_c (2 pts.).
set_c = set_a.intersection(set_b)
print(set_c)

# 13. Write code that creates another set containing all the elements of set_a and set_b, and assigns the
# resulting set to the variable set_d. Print set_d (2 pts.).
set_d = set_a.union(set_b)
print(set_d)


# 14. Write code that creates another set containing the elements that appear in set_a but not in set_b,
# and assigns the resulting set to the variable set_e. Print set_e (2 pts.).
set_e = set_a.difference(set_b)
print(set_e)


# 14. Write code that creates another set containing the elements that are not shared by set_a and set_b,
# and assigns the resulting set to the variable set_f. Print set_f (2 pts.).
set_f = set_b.difference(set_a)
print(set_f)
