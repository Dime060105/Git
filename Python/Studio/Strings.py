course = 'Python for Beginners' # stringa = immutabile, tutte le funziani non modificano la stringa ma forniscono un output modificato di quella stringa
print(course.upper()) # converte tutto il testo in maiusc
print(course.lower()) # converte tutto il testo in minus
print(course.find('t')) # trova in che posizioni si trova la lettera "t"
print(course.find('T')) # sensibile a maiusc e minusc, se output = -1 non esiste
print(course.find('for')) # trova in che posizioni si trova la parola "for"
print(course.replace('for', '4')) # rimpiazza un elemento con un altro
print(course.replace('x', '4')) # se non esiste l'elemento non cambia nulla dell'elemento iniziale
print('Python' in course) # l'"in operator" è un carattere speciale di py, output = bolean