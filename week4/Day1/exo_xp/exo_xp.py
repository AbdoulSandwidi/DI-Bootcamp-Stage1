#Exercice 1
print(4*"Hello world\n")

#Exercice 2 (Calcul de 99 à la puissance de 3 fois 8)

resultat= (99**3) * 8
print("resultat:",resultat,"\n\n")

#Exercice 3
# Sortie des extraits de codes suivants:

#>>> 5 < 3
print("False")

#>>> 3 == 3
print("True")

#>>> 3 == "3"
print("False")

#>>> "3" > 3
print("Il y'aura un TypeError")

#>>> "Hello" == "hello"
print("False\n\n")

# Exercice 4 : La Marque De Votre Ordinateur

computer_brand= "HP"
print(f"I have a <{computer_brand}> computer\n\n")

# Exercice 5 : Vos Informations

name= "SANDWIDI"
age= 25
shoe_size=41
info = f"Mr {name} a {age} ans et la pointure de sa chaussure est {shoe_size}"
print(info,"\n\n")
# L'execution a ete faite

# Exercice 6 : A & B
A = 12
B = 8
if A > B :
	print("Hello World\n A > B\n\n")

# Exercice 7 : Impair Ou Pair
nombre= int(input("Entrer un nombre pour verifier sa  parite:\t "))
if not(nombre%2):
	print(f"{nombre} est un nombre pair\n\n")
else:
	print(f"{nombre} est un nombre impair\n\n")

# Exercice 8 : Comment T’appelles-Tu ?
nom= input("Comment t'appelles-tu?\t")
nom= nom.upper()
if nom == "SANDWIDI":
	print("Ahh! Nous avons donc le meme nom!\n\n")
else:
	print("Nous avons des noms differents\n\n")

# Exercice 9 : Assez Grand Pour Monter Sur Des Montagnes Russes
pouce = float(input("Entrez votre pouce:\t"))
if 2.54*pouce > 145:
	print("Vous etes assez grand pour rouler!\n\n")
else:
	print("Vous devez grandir un peu plus!\n\n")