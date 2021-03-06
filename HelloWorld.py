a = int

print("\nMicro-calculadora\n")

print("2 + 2 = " + str(2 + 2))
print("2 / 2 = " + str(2 / 2))
print("2 * 2 = " + str(4 * 2))

a = int(input("\nEntre o valor de 'A': "))

if a == 2:
    print("\nA é igual há 2.")
elif a == 1:
    print("\nA é igual a 1.")
elif a == 0:
    print("\nA é igual a 0.")
else:
    print("\n'A' não é igual há 2, 1 nem 0. 'A' tem valor de " + str(a) + ".")