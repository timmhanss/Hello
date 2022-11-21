# Converter imperial to metric by Hansen 10 Nov 2022
import math

# Say hello to the user
def hello(name):
    print("Hello", name, "!")

# Convert height into feet"inch
def heightconvert(height): 
    feet = math.floor(int(height) / 30) # Divide the height by 30, round down
    inch = ((int(height) - 30 * feet)) % 12 # Subtract the height with feet() multiplied by 30, then find the remainder as inches
    print("Your height in feet/inches is ", feet, '"',inch, sep='') # Combine both then print, no separators.

# Convert weight into pounds
def weightconvert(weight):
    pounds = (float(weight) * 2.2)
    print("Your weight in pounds is", pounds)


# Ask the user it's name, height in cm, and weight in kg
def main():
    name = input("Hello! What's your name? ")
    height = input("How tall are you in centimeters? ")
    weight = input("How heavy are you in kilograms? ")
    hello(name)
    heightconvert(height)
    weightconvert(weight)

main()