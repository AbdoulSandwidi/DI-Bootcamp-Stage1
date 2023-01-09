print("=======================Exercise 1: Set=========================")
#1.Créez un ensemble
print("\nMes numeros favoris:")
my_fav_numbers = {72403073,75169304,67123939}
print(f"{my_fav_numbers}\n\n")

# 2. Ajoutez deux nouveaux numéros
print("Ajoutez deux nouveaux numéros")
my_fav_numbers.add(52633939)
my_fav_numbers.add(53633939)
print(f"{my_fav_numbers}\n\n")

# Supprimer le dernier numero
print("L'ensemble après suppression du dernier numero:")
my_fav_numbers.pop()
print(f"{my_fav_numbers}\n\n")

# 4.Les numeros favoris de mon ami
print("Les numeros favoris de mon ami:")
friend_fav_numbers={78458698,70010101,76707070}
print(friend_fav_numbers,"\n\n")

# 5.Concatenation
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(f"our_fav_numbers: {our_fav_numbers}\n\n")

print("=======================Exercise 2: Tuple=========================")
# Non! on peut ajouter dans le tuple. Les tuples sont immuables.
print("\nNon! on peut ajouter dans le tuple. Les tuples sont immuables.\n\n")


print("=======================Exercice 3 : Liste=========================")

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1.Retirez « Banana » de la liste.
basket.remove("Banana")

# 2.Retirez « Blueberries » de la liste.
basket.remove("Blueberries")

# 3.Ajoutez « Kiwi » à la fin de la liste
basket.append("Kiwi")

# 4.Ajoutez « Apples » au début de la liste.
basket.append("Apples")

# 5.Comptez combien de pommes sont dans le panier
basket.count("Apples")

# 6.Videz le basket
basket.clear()

# 7.Imprimer(basket)
print(basket)


"""
Exercice 4 : Flotteurs
1. Un float est un type de données fondamental intégré au compilateur
	qui est utilisé pour définir des valeurs numériques avec des virgules
	décimales flottantes;
	int les entiers peuvent être décrits comme des nombres entiers, ce qui
	signifie qu’ils n’ont pas de parties fractionnaires, tandis que float
	décrit un nombre qui ne peut être écrit que dans un système de nombres décimaux.


2. Oui! une autre façon de generer un flottant est le fait de convertir un chaine avec
une precision absolue et à supprimer le nombre de caracteres souhaité  
"""

# 3. Create a list
liste = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

# Exercice 5 : Pour La Boucle
print("=======================Exercice 5=========================")

# Question 1
for x in range(1,21):
	print(x)

# Question 2
liste1 = []
for x in range(1,21):
	liste1.append(x)

for indice in range(0,len(liste1)):
	if indice%2 == 0:
		print(liste1[indice])

# Exercice 6 : En Boucle
print("=======================Exercice 6=========================")

User_name = "SANDWIDI"
User= ""
while User != User_name:
	User= input("Veuiller entrer votre nom d'utilisateur:\t")

#Exercice 7
print("=======================Exercice 7=========================")
# Question 1)
fruits = input("Ecrivez ici vos fruits preferes separes par des espaces\n\tExemple: 'mangues karite banane'\t")

# Question 2)
Liste = []
Liste = fruits.split()

# Question 3)
fruit = input("\nEnter le nom de n'importe quel fruit:\t")
if fruit in liste:
	print("Vous avez choisi l'un de fruits preferes! Profitez-en\n")
else:
	print("Vous avez choisi un nouveau fruit. J'espere que vous apprecierez!\n")


# Exercice 8
print("=======================Exercice 8=========================")
# Question 1)

choix = ""
ListeP = []
while choix != "QUITTER":
	choix= input("Entrer les garniture PIZZA de votre choix:\t")
	choix = choix.upper()
	if choix == "QUITTER":
		break

# Question 2)	
	else:
		print("\nNous ajouterons cela a vos garnitures.\t")
		ListeP.append(choix)

# Question 3)
prix = 10
print("\nListe des garnitures:")
for i in ListeP:
	print(f"\t==>{i}")
	prix += 2.5
print(f"Le montant total:\t{prix} $")

# Exercice 9
print("=======================Exercice 9=========================")
# Question 1)
cout = 0
cout1 = 10
cout2 = 15
age = int(input("Entrer votre age :\t"))
if 3 <= age and age <= 12 :
	cout = cout1

if age > 12:
	cout = cout2
print(f"Facture: {cout}$")

# Question 2)
enfant = int(input("Entrer le nombre d'enfant de 3 à 12 ans:\t"))
grand_enfant = int(input("Entrer le nombre de personnes de plus 12 ans\t"))

# Question 3)
print(f"Cout total: {enfant * cout1 + grand_enfant * cout2}")

# Question 4)
list_admissibl = [["Clement", 18], ["Roland", 12],
			["lamine", 25], ["Richard", 15]]

print("\nListe des prospects:\n", list_admissibl)
for x in list_admissibl:
	print(f"\t==>{x[0]} ==> {x[1]}")

for x in list_admissibl:
 	if x[1] not in range(16,22):
 		list_admissibl.remove(x)
 
print("\nListe des client de cette seance:", list_admissibl)
for x in list_admissibl:
 	print(f"\t==>{x[0]} ==> {x[1]}")


# Exercice 10
print("=======================Exercice 10=========================")

# Question 1)
sandwich_orders = ["Tuna sandwich", "Avocado sandwich",
					"Egg sandwich", "Sabih sandwich",
					"Pastrami sandwich"]

# Question 2)
finished_sandwiches = []

# Question 3)
p=1
while p==1:
	print("\tQuel sandwich est pret?")
	for m in range(0, len(sandwich_orders)):
		print(f"\n\t\t{m+1}- {sandwich_orders[m]}")

	x = int(input("\t\tEntrer votre choix:\t"))
	pret = sandwich_orders[x-1]
	finished_sandwiches.append(sandwich_orders[x-1])
	sandwich_orders.remove(sandwich_orders[x-1])
# Question 4)
	
	print(f"I made your {pret}\n")
	p = int(input("\tTaper 1 s'il y a des sandwich prepares:\t"))