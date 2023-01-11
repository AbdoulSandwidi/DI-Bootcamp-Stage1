print("\n======================== Exercice 1 ========================\n")
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#Question 1)
chat1 = Cat("Milou", 2)
chat2 = Cat("chamss", 3)
chat3 = Cat("Milou", 4)

liste = [chat1, chat2, chat3]
def chat_age(liste_chat):
	liste_age = [chat.age for chat in liste_chat]
	print("liste age = ",liste_age)
	for chat in liste_chat:
		if chat.age == max(liste_age):
			return chat

vieux_chat = chat_age(liste)
print(f"Le chat le plus âgé est {vieux_chat.name} et a {vieux_chat.age} années.")

# Exercice 2 : Chiens
print("\n======================== Exercice 2 ========================\n")

class Dog:
	"""docstring for Dog"""
	def __init__(self, name, height):
		self.name = name
		self.height = height

	def bark(self):
		print(f"\t\t{self.name} goes woof!")

	def jump(self):
		print(f"\t\t{self.name} saute {2*self.height} cm de haut!")

davids_dog = Dog("Rex", 50)

print(f"\t\tNom du chien de David:\t{davids_dog.name}\n\t\tHauteur du chien:\t{davids_dog.height}cm")
print("\n			************		\n")

davids_dog.bark()
davids_dog.jump()

print("\n			************		\n")

sarahs_dog = Dog("Teacup ", 20)
print(f"\t\tNom du chien de David:\t{sarahs_dog.name}\n\t\tHauteur du chien:\t{sarahs_dog.height}cm")
print("\n			************		\n")
sarahs_dog.bark()
sarahs_dog.jump()

print("\n			************			\n")

if davids_dog.height > sarahs_dog.height :
	print(f"\t\t{davids_dog.name} est le plus grand chien")
else :
	print(f"\t\t{sarahs_dog.name} est le plus grand chien")

#Exercice 3 : Qui Est Le Producteur De La Chanson ?
print("\n======================== Exercice 3 ========================\n")
class Song():
	"""docstring for Song"""
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for element in self.lyrics :
			print("\t\t",element)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()