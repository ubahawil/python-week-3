count = 1
total = 0

# BUG: Added a colon after the while condition.
while count <= 5:
    total = total + count

    # BUG: Changed count < 5 to count <= 5 so that 5 is included.
    count = count + 1

# BUG: Converted total to a string so it can be joined with the text.
print("Sum of 1 to 5 is: " + str(total))
