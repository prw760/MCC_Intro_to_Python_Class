# EA 2
# Paul Wade

from itertools import groupby

# CHAPTER 5

# 1. Create a variable named num_1 and assign 14 to it (1 pt.).
num_1 = 14


# 2. Create a variable named num_2 and assign 79 to it (1 pt.).
num_2 = 79


# 3. Add num_1 to num_2 and store it in ans_one, print ans_one (2 pts.).
ans_one = num_1 + num_2
print(ans_one)


# 4. Subtract num_1 from num_2 and store it in ans_two, print ans_two (2 pts.).
ans_two = num_2 - num_1
print(ans_two)

# 5. Multiply num_1 by num_2 and store it in ans_three, print ans_three (2 pts.).
ans_three = num_1 * num_2
print(ans_three)


# 6. Divide num_2 by num_1 and store it in ans_four, print ans_four (2 pts.).
ans_four = num_2 / num_1
print(ans_four)


# 7. Use the integer division operator to divide num_2 by num_1 and store it in ans_five, print ans_five (2 pts.).
ans_five = num_2 // num_1
print(ans_five)


# 8. Return the remainder of num_2 divided by num_1 and store it in ans_six, print ans_six (2 pts.).
ans_six = num_2 % num_1
print(ans_six)


# 9. Use the is_integer method to check if num is an integer and print the value returned by the method (2 pts.).
num = 15.6 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
print(num.is_integer())


# 10. Use the pow function to print out 5 raised to the power of -3 (1 pt.).
print(pow(5, -3))


# 11. Print num_3 so that 3 decimal places are displayed and it is grouped by thousands (1 pt.).
num_3 = 987654321.123456789 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
print(round(num_3, 3))


# 12. Write a print statement using an f-string that prints out the following sentence using the variables defined below.
# In 2017, New Zealand had a population of 4,793,700 and a life expectancy of 71.61 years. The round function
# should not be used (2 pts.).
year = 2017 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
population = 4793700 # DO NOT DELETE OR MODIFY THIS LINE OF CODE
expectancy = 71.6143 # DO NOT DELETE OR MODIFY THIS LINE OF CODE

print("In {0}, New Zealand had a population of {1:,} and a life expectancy of {2:.2f} years.".format( year, population, expectancy))

