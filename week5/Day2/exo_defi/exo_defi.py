class Farm():
	"""docstring for Farm"""
	def __init__(self, Nom_fermier):
		self.Nom_fermier = Nom_fermier

macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
print(macdonald.get_info())