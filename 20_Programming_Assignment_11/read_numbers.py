# Paul Wade
# PA 11


# Open the file that was created in PA 11, Part 1 (write_numbers.py)

my_file = open('/users/paulwade/numbers.txt', 'r', encoding='utf-8')  # I'm using a mac, so no drive letter in path


# EXTRA CREDIT:
# Preload the count_tally dictionary with keys in order, each with zeroes.
# This will ensure sorting by key.

count_dict = {"0": "0", "1": "0", "2": "0", "3": "0", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0",
              "9": "0", "10": "0", "total": "0"}


while True:     # loop until EOF

    this_line = my_file.readline()      # Read in a line

    if this_line == '':                 # If EOF, break out of while loop

        break

    else:

        this_line = this_line.rstrip("\n")                                    # strip out the newline character

        count_dict[this_line] = int(count_dict[this_line]) + 1                # Increment number's count value

        count_dict["total"] = str(int(count_dict["total"]) + int(this_line))  # Increase running tally by number value


# After EOF, close the file

my_file.close()


# Iterate over all number values and output counts for each one

for i in range(1, 11):

    print("Number", str(i), "is in the list", count_dict[str(i)], "times.")


# Print the tally of all the numeric values in list

print("\nThe total of all the numbers in the list is:", count_dict["total"])
