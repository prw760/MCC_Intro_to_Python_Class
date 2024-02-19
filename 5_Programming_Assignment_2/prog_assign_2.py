# PA 2
# Paul Wade

word_1 = input("Enter word one that contains at least 4 letters: ")

word_2 = input("Enter word two that contains at least 4 letters: ")

word_3 = input("Enter word three that contains at least 4 letters: ")

combined = word_1[0:3] + word_2[len(word_2) - 2:] + word_3[0]

print(combined)

# SAMPLE OUTPUT:
#
# Enter word one that contains at least 4 letters: adobe
# Enter word two that contains at least 4 letters: fiver
# Enter word three that contains at least 4 letters: 12345
# adoer1
