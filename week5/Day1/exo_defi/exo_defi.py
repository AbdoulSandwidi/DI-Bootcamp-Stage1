class Farm():
	"""docstring for Farm"""
	def __init__(self, nom):
		self.nom = nom
		self.dico = {}

	def add_animal(self, name, nombre_animaux = 1):
		if name in self.dico :
			self.dico[name] += nombre_animaux
		else :
			self.dico[name] = nombre_animaux

	def get_info(self):
		print(f"{self.nom}'s Farm\n")
		for animal, nb_animal in self.dico.items() :
			print(f"{animal} : {nb_animal}")
		return "\n\tE-I-E-I-0!"

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())