# Asks user for their name
name = input("What's your name?")

# Removes extra spaces and adds capitalization in the name input
# .strip and .title parameters are used
name = name.strip().title() 

# Prints the name variable
print("Hello,", name)