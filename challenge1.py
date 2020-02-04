

name = input("What is your name? ")
age = int(input("How old are you? "))
number = int(input("Please write a number between 0 and 10 "))

years_left = 100-age
year = 2020+years_left

for i in range(number):
    print("Hi " + name + " , you will turn 100 in the year of " + str(year))