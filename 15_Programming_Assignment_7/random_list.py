# Paul Wade
# PA 7

import random
import statistics


# Initialize empty list, then populate it with 20 random numbers between 1 and 100
my_list = []

for i in range(20):
	my_list.append(random.randint(1,100))


# Output various metrics about the list (values, min, max, sum, average)

print("The list contains:", my_list)
print("The lowest random number was:", min(my_list))
print("The highest random number was:", max(my_list))
print("The total of the random numbers was:", sum(my_list))
print("The average of the random numbers was:", statistics.mean(my_list))


# Output a same-line list of the list's integer elements that are greater than 50

print("\nRandom numbers > 50")

for i in range(20):
	if my_list[i] > 50:
		print(my_list[i], end=" ")
