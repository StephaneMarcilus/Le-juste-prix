juste_prix = 500
prix = int(input("Veuillez entrer un prix : "))

while prix != juste_prix:

    if prix < juste_prix:
        print("C'est plus !")
        prix = int(input("Veuillez entrer un prix : "))

    else:
        print("C'est moins !")
        prix = int(input("Veuillez entrer un prix : "))

print("C'est le juste prix !")
        