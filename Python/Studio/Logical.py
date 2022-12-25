price = 31
print(price > 10 and price < 30) # se entrambe le bolean sono true il risultato dell'espressione sarà true, se una dlle due o tutte e duo sono falsa allora il risultato sarà false
print(price > 10 or price < 30) # il check è lineare, prima controlla se il valore è maggiore di 10 poi se è minore di 30, se un risultato dei due è true allora il risultato dell'espressione sarà true
print(not price > 10) # il risultato sarà true se la il prezzo non sarà maggiore di 10 e false se lo sarà, inverte il risultato