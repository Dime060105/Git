# numbers = range(5) # genera un range di numeri da 0 a 5 escluso 5
# numbers = range(5, 10) # genera un range di numeri da 5 a 10 escluso 10
numbers = range(5, 10, 2) # genera un range di numeri da 5 a 10 escluso 10 ogni 2 numeri partendo da 5
print(numbers)

for number in numbers: # per ogni numero in "numbers" esegui print, si può anche direttamente usare range al posto di "numbers" senza creare un elemento
    print(number)