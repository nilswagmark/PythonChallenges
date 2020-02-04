
import random

list_of_numbers = []
for i in range(20):
    list_of_numbers.append(random.randint(0,10))

for number in list_of_numbers:
    if number < 5:
        print(number)
    else:
        continue