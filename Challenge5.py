number = int(input("Write a number"))
lista = range(1, number+1)
divisor_list = []

for elem in lista:
    if number % elem == 0:
        divisor_list.append(elem)

print(divisor_list)

