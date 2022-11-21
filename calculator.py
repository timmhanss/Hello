print("Welcome to Hansen's first Calculator! Made on 9 Nov 2022")

# Get two numbers from the user
x = input("Insert your first number: ")
y = input("Insert your second number: ")

# Calculate and print x and y
result = float(x) + float(y)

# Print the result with a comma separator, split the print between two lines to make it clear.
print ("The answer is: ", end='') # No new line
print (f"{result:,}")