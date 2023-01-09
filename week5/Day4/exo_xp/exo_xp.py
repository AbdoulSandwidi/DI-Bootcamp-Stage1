# Exercice 1

def ce_q_j_apprend():
	print("Salut! Je suis en train d'apprendre les fonctions en python\n")

ce_q_j_apprend()


# Exercice 2

def favorite_book(title):
	print(f"Un de mes livres préférés est '{title}'\n")

title = "Candide"
favorite_book(title)

# Exercice 3

def describe_city(ville = "Ouagadougou", pays="Burkina Faso"):
	print(f"'{ville}' est au '{pays}'")

describe_city()

# Exercice 5

def make_shirt(taille = "Grande", message = "J’aime Python"):
	print(f"La taille de votre chemise est '{taille}' et le texte est '{message}'\n")

taille = "Moyenne"
sms = "HEUREUX MENAGE"
make_shirt(taille, sms)

make_shirt()

make_shirt("Grande",)

make_shirt("Moyenne",)

make_shirt(taille = "de votre choix", message = "conforme a vos souhaits")


# Exercice 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
	for magician_name in magician_names:
		print(f"\t\t\t{magician_name}")

def make_great(magician_names):
	for magician_name in magician_names:
		indice = magician_names.index(magician_name)
		magician_names[indice]= "the Great " + magician_name

make_great(magician_names)
show_magicians(magician_names)


# Exercice 7
import random
def get_random_temp(saison):
	temp = random.randint(-10, 40)
	if saison == "hiver":
		temp = random.randint(-10, 16)
	elif saison == "ete":
		temp = random.randint(16, 23)
	elif saison == "automne":	
		temp = random.randint(23, 32)
	elif saison == "printemps":
		temp = random.randint(32, 40)
	temp = random.uniform(temp, temp+1)
	return temp

# get_random_temp(saison)

def main():
	saison = input("Entrer la saison (Ex: ete, automne, hiver ou printemps) :")
	temperature = get_random_temp(saison)

	print(f"La température actuelle est de {temperature} degrés Celsius.")
	if temperature < 0 :
		print("Brrr, c’est glacial! Portez des couches supplémentaires aujourd’hui")
	elif temperature < 16:
		print("Assez froid! N’oublie pas ton manteau")
	elif temperature < 23:
		print("Ah! Comme le temps est beau!")
	elif temperature < 32:
		print("Detendez-vous! La temperature est ambiante.")
	else:
		print("Asbtenez-vous de sortir sous le soleil car il fait assez chaux.")

main()