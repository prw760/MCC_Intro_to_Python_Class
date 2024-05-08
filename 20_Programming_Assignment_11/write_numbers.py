# Paul Wade
# PA 11

numbers = [5, 6, 8, 7, 8, 9, 2, 3, 2, 8, 6, 9, 9, 4, 5, 8, 9, 1, 8, 6, 10, 8, 8, 4, 5, 5, 3, 7, 5, 8, 1, 3, 1, 9, 5,
           9, 8, 5, 2, 1, 7, 10, 4, 1, 3, 6, 5, 5, 2, 3, 7, 4, 2, 3, 5, 8, 9, 8, 3, 3, 1, 5, 7, 3, 5, 3, 8, 6, 9, 10,
           9, 9, 2, 10, 2, 9, 2, 5, 6, 4, 10, 9, 5, 8, 3, 4, 2, 4, 7, 2, 3, 1, 9, 2, 7, 3, 3, 4, 6, 2]

# Open the file to write to with "create/overwrite" mode

my_file = open('/users/paulwade/numbers.txt', 'w', encoding='utf-8')    # I'm using a mac, so no drive letter in path


# iterate through each number in list and write to file with newline character

for list_number in numbers:

    my_file.write(str(list_number) + '\n')


# Output Status

print("The integer list has been written to the file", my_file.name)


# Close the still-open file

my_file.close()

