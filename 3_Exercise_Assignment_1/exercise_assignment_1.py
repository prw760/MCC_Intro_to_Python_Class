# EA 1
# Paul Wade

# CHAPTER 4

mcc_string = "Mesa Community College Thunderbirds" # DO NOT DELETE THIS LINE OF CODE

# 1. Print the length of mcc_string (1 pt.).

print(len(mcc_string))

# 2. Use slicing on mcc_string to print out the substring:ege Thunder (1 pt.).

print(mcc_string[19:30])

# 3. Use negative slicing on mcc_string to print out the substring:nity Coll (1 pt.).

print(mcc_string[-25:-16])

# 4. Write a statement that uses the find function to find College in mcc_string. Print the value returned by the function (2 pts.).

print(mcc_string.find("College"))

# 5. Write a statement that removes the whitespace at the end of num_string and assigns the updated string 
# to a variable called updated_num_string.  Print updated_num_string (2 pts.).
num_string = '098-76-54321     ' # DO NOT DELETE THIS LINE OF CODE

updated_num_string = num_string.rstrip()
print(updated_num_string)

# 6. Write a print statement using a f-string that prints out the following using the variables defined below.
# The variables must be used to calculate 7.5 in the print statement (1 pt.).
# 30 / 4 = 7.5
var_1 = 4 # DO NOT DELETE THIS LINE OF CODE
var_2 = 30 # DO NOT DELETE THIS LINE OF CODE

print(f"{var_2} / {var_1} = {var_2 / var_1}")


# 7. Write a statement that replaces Spring 2023 with Fall 2022 in string_one and assigns it to string_two.  Print string_two (2 pts.).
string_one = "The student is registered in CIS256DA for Spring 2023 semester." # DO NOT DELETE THIS LINE OF CODE

string_two = string_one.replace("Spring 2023", "Fall 2022")
print(string_two)


# 8. Convert the string stored in num1 to a float and assign it to num2 (1pt.).
num1 = "32.3" # DO NOT DELETE OR MODIFY THIS LINE OF CODE
num2 = float(num1)

# 9. Convert the string stored in num3 to an int and assign it to num4 (1pt.).
num3 = "20" # DO NOT DELETE OR MODIFY THIS LINE OF CODE
num4 = int(num3)

#10. Print out the product of num2 * num4 (1 pt.).
print(num2 * num4)

# 11. Using CONCATENATION, print out the following sentence: 12 inches equals 30.48 centimeters.
# You must use the variables listed below in the sentence (2 pts.)
inches = 12 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
centimeters = 30.48 # DO NOT DELETE OR MODIFY THIS LINE OF CODE

print(str(inches) + " inches equals " + str(centimeters) + " centimeters.")
