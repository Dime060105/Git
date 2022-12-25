unità = input("Kg (K) o Masse Solari (O)? ")

if unità.upper() == "O":
    masse = input("Quante Masse? ")
    convertito = float(masse) * 1.989E+30
    raggio = (1.48E-27 * convertito) / 1000
    print("Il Raggio di Swarchild misura " + str(raggio) + "Km")
elif unità.upper() == "K":
    chili = input("Quanti Chili? ")
    raggio = (1.48E-27 * float(chili)) / 1000
    print("Il RAggio di Swarchild misura " + str(raggio) + "Km")
else:
    print("Il Formato Ultilizzato non è Valido, Riprovare...")