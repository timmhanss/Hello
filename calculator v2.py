print("Welcome to Hansen's second Calculator! Made on 9 Nov 2022")    

# Calculate all numbers
def calc(x,y): # This takes two numbers, set calc to accept two variables
    num = float(x) + float(y) # Both variables are added here
    print("The total of both numbers are: ", num) # Print the result
    
# Ask the user for two numbers
def main():
    x = input("Insert your first number: ") 
    y = input("Insert your second number: ")
    calc(x,y) # This will send both variables to the calc() function

main()