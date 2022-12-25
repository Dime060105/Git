temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink watewr")
elif temperature > 20:       # se questo viene eseguito vuol dire che temp <= 30 e > 20
    print("Is a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("Is cold")          # questo viene eseguito solo se nessuno degli statement sopra di lui sono stati soddisfatti