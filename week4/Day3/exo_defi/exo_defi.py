# Défi 1

mot = input("Entrer un mot:\t")
dico1 = {}
i = 0
while i < len(mot): #maman
	dico1.update({i: mot[i]})
	i += 1
print("dico1", dico1)
dico2 = {}
for x,y in dico1.items() :
	li = [x]
	for i,j in dico1.items():
		if x!=i and j == y :
			li.append(i)
			li = sorted(li)
			dico2.update({y: li})
	else:
		dico2.update({y: li})
print("dico2", dico2)


# Défi 2
items_purchase = {
				  "Water": 1,
				  "Bread": 3,
				  "TV": 1000,
				  "Fertilizer": 20
				}
wallet = int(input("Entrer le montant dont vous posseder:\t"))
print("\t\t\tProduit -->Prix en $")

my_keys = list(items_purchase.keys())
tri = my_keys
keys_sorted = [] 			# Une nouvelle liste contenant les meme element que my_keys
for x in my_keys:
	keys_sorted.append(x)
keys_sorted.sort()			#triage
print(keys_sorted)

items_purchase_sorted = {}

for k in keys_sorted:
	for x,y in items_purchase.items():
		if x == k:
			items_purchase_sorted[x] = y

print(items_purchase)
print("items_purchase_sorted:", items_purchase_sorted)

for x,y in items_purchase_sorted.items():
	if y <= wallet:
		print(f"\t\t\t{x}  ----->{y}")
n=0
for x,y in items_purchase_sorted.items():
	if y <= wallet:
		n = 1
	break

if not n:
	print("\n\t\tNothing!")