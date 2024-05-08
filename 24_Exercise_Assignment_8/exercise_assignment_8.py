# EA 8
# Paul Wade

# CHAPTER 17

import numpy as np

# Use numpy functions to answer the questions, unless otherwise stated.

# 1. Create a 4x4 array named four_by_four containing 13,14,15,16 in row 1; 9,10,11,12  in row 2;  5, 6,
# 7,8 in row 3 and 1,2,3,4 in row 4 (2 pts.).
# Do NOT use the arrange() or reshape() functions to create the array

four_by_four = np.array([
							[13, 14,  15, 16],
							[9, 10, 11, 12],
							[5, 6, 7, 8],
							[1, 2, 3, 4]
						])


# 2. Print the shape of  four_by_four (1 pt.).

print(four_by_four.shape)


# 3. Print four_by_four (1 pt.).

print(four_by_four)


# 4. Calculate and print the sum of four_by_four (2 pts.).

print(np.sum(four_by_four))


# 5. Calculate and print the maximum entry in four_by_four (2 pts.).

print(np.max(four_by_four))


# 6. Calculate and print the minimum entry in four_by_four (2 pts.).

print(np.min(four_by_four))


# 7. Get and print an array of diagonal entries from four_by_four (2 pts.).
print(np.diagonal(four_by_four))


# 8. Use the arange() function to create a 1-D array named one_dim containing the even int values 100 through 122
# (2 pts.).

one_dim = np.arange(100, 122 + 1, 2)


# 9. Print one_dim (1 pt.).

print(one_dim)


# 10. Use the reshape function to reshape one_dim into a 2-D array named two_dim with 3 rows and 4 columns (2 pts.).

two_dim = one_dim.reshape(4, 3)


# 11. Print two_dim (1 pt.).

print(two_dim)

# 12. Cube every entry in two_dim using the ** operator and save the results in cubed_two_dim (1 pt.).

cubed_two_dim = two_dim**2


# 13. Print cubed_two_dim (1 pt.).

print(cubed_two_dim)
