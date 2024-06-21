import time

# 61efficacite.py

# complexite : 
# RLE = O(n) car boucle for
# RLErec = O(nk) car RLE O(n) * nb iteration
# unRLE = O(9n/2) soit n car limit de la 2eme boucle à 9 / 2 car parcours 2 en 2
# unRLErec = O(nk)

# test10() aucun détail
# test30() +=650ms
# test40() +=0.8s
# test60() infini

def RLE(texte):
    # si le texte est vide on renvoie une chaine vide
    if not texte:
        return ""

    resultat = []

    # initialise le compteur et le caractère
    compteur = 1
    caractere = texte[0]

    # on parcours le texte a partir du deuxième caractère
    for i in range(1, len(texte)):
        # si le caractère actuel est le même que le précédent et que le compteur est inférieur à 9
        if texte[i] == caractere and compteur < 9:
            compteur += 1
        else:
            # sinon on ajoute le compteur et le caractère au résultat
            resultat.extend([str(compteur), caractere])
            # on remets les variables a jour
            compteur = 1
            caractere = texte[i]

    # on ajoute ce qu'il reste au resultat
    resultat.extend([str(compteur), caractere])

    # on mets la liste sous foeme de chaine et on la renvoie
    return "".join(resultat)


def RLE_recursif(chaine, nombre):
    resultat = chaine
    for _ in range(nombre):
        resultat = RLE(resultat)
    return resultat


def unRLE(chaine):
    result = ""
    for i in range(0, len(chaine), 2):
        nombre = int(chaine[i])
        caractere = chaine[i+1]
        result += caractere * nombre
    return result

def unRLE_recursif(chaine, nombre):
    resultat = chaine
    for i in range(nombre):
        resultat = unRLE(resultat)
    return resultat

startRLE = time.time()
print(RLE("abc"))
print(RLE("abbccc"))
print(RLE("aaabaa"))
print(RLE("aAa"))
print(RLE("WWWWWWWWWWWWW"))
print(RLE("WWWWWWWWWBWWWWWWWWBBBWWWBWWWWWWW"))
print("temps rle : ", time.time() - startRLE)

startRLErec = time.time()
print(RLE_recursif("abc", 1))
print(RLE_recursif("abbccc", 1))
print(RLE_recursif("aaabaa", 1))
print(RLE_recursif("aAa", 1))
print(RLE_recursif("abc", 2))
print(RLE_recursif("abc", 3))
print("temps rle_rec : ", time.time() - startRLErec)

startunRLErec = time.time()
print(RLE("abc"))
print(RLE("abbccc"))
print(RLE("aaabaa"))
print(RLE("aAa"))
print(RLE("WWWWWWWWWWWWW"))
print(RLE("WWWWWWWWWBWWWWWWWWBBBWWWBWWWWWWW"))
print("temps rle_rec : ", time.time() - startunRLErec)

start10 = time.time()
print(unRLE_recursif(RLE_recursif("SAE", 10), 10))
print("temps rle_rec : ", time.time() - start10)
start20 = time.time()
print(unRLE_recursif(RLE_recursif("SAE", 20), 20))
print("temps rle_rec : ", time.time() - start20)
start30 = time.time()
print(unRLE_recursif(RLE_recursif("SAE", 30), 30))
print("temps rle_rec : ", time.time() - start30)
start40 = time.time()
print(unRLE_recursif(RLE_recursif("SAE", 40), 40))
print("temps rle_rec : ", time.time() - start40)
start60 = time.time()
print(unRLE_recursif(RLE_recursif("SAE", 60), 60))
print("temps rle_rec : ", time.time() - start60)
start100 = time.time()
print(unRLE_recursif(RLE_recursif("SAE", 100), 100))
print("temps rle_rec : ", time.time() - start100)