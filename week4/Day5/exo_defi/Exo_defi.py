sequence = input("Entrer une sequence de mots separes par des virgules:\n\t")

liste = sequence.rsplit(",")
# Autre methode : liste.sort(reverse = False)

print(f"La liste correspondant à votre sequence est:\n\t{sorted(liste)}")