#Défi 1
# Question 1)
number = int(input("Entrer un entier pour obtenir ses multiples:\t"))
length = int(input("Entrer le nombre de multiples desires:\t"))

# Question 2)
i=1

liste = []
while i <= length :
	liste.append(number*i)
	i += 1
print(liste)


#Défi 2
# Question 2)
chaine = input("Entrer une chaine:")
chaine = chaine.lower()
reduit = chaine
for i in chaine:
	reduit = reduit.replace(i+i,i)
print(reduit)