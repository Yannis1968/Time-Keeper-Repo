
numbers= input("Δώσε μου μια σειρα αριθμών χωρισμένων με κομα: ")
list_of_numbers = numbers.split(',')
list_of_every_second_number = []

for x in list_of_numbers:
    if list_of_numbers.index(x)%2 == 1:
       list_of_every_second_number.append(int(x))

    else:
        pass

print (sum(list_of_every_second_number))

