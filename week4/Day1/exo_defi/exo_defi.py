import random

chaine = input("Entrer une chaine de caratere:\t")
if len(chaine) < 10:
	print("chaine pas assez longue")
elif len(chaine) > 10:
	print("chaine trop longue")

print(f"Le premier caractere de {chaine} est '{chaine[0]}' et le dernier est '{chaine[-1]}'")

liste=list(chaine)
a=""
for i in liste:
	a = a+i
	print(a)

print("\nChaine melangee:\n")
random.shuffle(liste)
new_chaine = "".join(liste)
print(new_chaine, "\n\n")