# Exercice 1
print("=======================Exercice 1=========================")

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))

print(dictionary)

print("=======================Exercice 2=========================")

# Exercise 2
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
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cout_famille = 0
print("\nCout individuel des membres de la famille")
for nom,age in family.items():
	if 3 <= age and age <= 12 :
		cout = cout1

	elif age > 12:
		cout = cout2
	cout_famille += cout

# Question 3)
	print(f"\t\t===> {nom}: {cout}$")

# Question 4)
print(f"\n\tTotal:\t{cout_famille}$")

# Question 5)
family1 = {}
i = 1
while i == 1:
	nom1 = input("\tEntrer le nom du membre:\t")
	age1 = int(input("\tEntrer son age:\t"))
	family1.update({nom1: age1})
	i = int(input("Taper 1 pour ajouter un membre:"))
print(family1)

print("=======================Exercice 3=========================")

brand = {"name": "Zara",
		"creation_date": 1975,
		"creator_name": "Amancio Ortega Gaona",
		"type_of_clothes": ["men", "women", "children", "home"],
		"international_competitors": ["Gap", "H&M", "Benetton"],
		"number_stores": 7000,
		"major_color":
		    {"France": "blue", 
		    "Spain": "red", 
		    "US": ["pink", "green"]}
		}

brand.update({"number_stores": 2 })
brand.update({"country_creation": "Spain"})
print(brand["international_competitors"])

# Question 6)
for i,j in brand.items():
 	if i == "international_competitors":
 		j = j.append("Desigual")

print(f"\nListe apres ajout de 'Desigual':\n{brand}")

# Question 7)
brand.pop("creation_date")
print(f"\nListe apres suppression de 'creation_date':\n{brand}")

# Question 8)
competitors = brand["international_competitors"]
last_competitor = competitors[-1]
print(f"\nThe last international competitor:\t {last_competitor} ")

# Question 9)
US_colors = brand["major_color"]["US"]
print(US_colors)
print("Les principales couleurs de vetements aux Etats-Unis")
for color in US_colors:
	print("\t\t\t\t\t", color)

# Question 10)
taille = len(brand)
print("Le nombre de paires cle-valeur:\t", taille)

# Question 11)
print("Liste des cle:")
for i,j in brand.items():
	print("\t\t\t\t\t", i)

# Question 12)
more_on_zara = {
				"creation_date": 1975,
				"number_stores": 10000
				}
# Question 13)
brand.update(more_on_zara)

# Question 14)
print(f"\nLe nombre actuel de magazins: \t{brand['number_stores']}")
# constat : Le nombre de magazin a ete mise a jour
print("\nConstat : Le nombre de magazin a ete mise a jour")


# Exercice 4
print("=======================Exercice 4=========================")

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Question 1)
dico1 = {}
for i in users:
	dico1[i] = users.index(i) 
print("\nDictionnaire 1:\n\t",dico1)

# Question 2)
dico2 = {}
for i in users:
	dico2[users.index(i)] = i
print("\nDictionnaire 2 :\n\t",dico2)

# Question 3)
dico3 = {}
users.sort()
for i in users:
	dico3[i] = users.index(i)
print("\nDictionnaire 3:\n\t",dico3)

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Question 4-1)
dico4 = {}
for elem in users:
	if "i" in elem:
		dico4[elem] = users.index(elem)
print("\nDictionnaire 4:\n\t", dico4)

# Question 4-1)
dico5 = {}
for elem in users:
	if elem[0] == "M"or elem[0] == "P":
		dico4[elem] = users.index(elem)
print("\nDictionnaire 5:\n\t", dico4)