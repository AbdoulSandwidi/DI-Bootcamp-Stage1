
matrice=[["7", "i", "3"],
        ["T", "s", "i"],
        ["h"," %", "x"],
        ["i", " ","#" ],
        ["s", "M", " "],
        [" $", "a", " "],
        ["#", "t", "%"],
        ["^", "r", "!"]]


def affich_matrice(matrice):
    liste=[]
    for i in range(3):
        for ligne in matrice:
            liste.append(ligne[i])
    print(liste)
    for elem in liste:
        if not(elem.isalpha()) :
            i= liste.index(elem)
            j=i+1
            if not(liste[j].isalpha()):
                while j in range(len(liste)) and not(str(liste[j]).isalpha()):
                    #print(i,j)
                    j+=1
                if i != j:
                    liste[i:j] = " "
            else:
                liste.remove(elem)
    print(liste)
    return liste


liste = affich_matrice(matrice)

def formation_du_mot(liste):
    mot = ""
    mot = mot.join(liste)
    return mot

mot = formation_du_mot(liste)


print("Le texte contenu dans la matrice:\n\t", mot)
