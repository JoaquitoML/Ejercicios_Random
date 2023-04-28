

for numero in range(0,101):
    
    if numero % 3 == 0:
        print("fizz")
    
    elif numero % 5 == 0:
        print("buzz")
    
    if numero % 15 == 0:
        print("fizzbuzz")
    
    else:
        print(numero)