
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print stars in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
