"""
Algoritme de compression de chaîne 
"""
def RLE(chaine : str) :
    #Initialisation d'une chaine et d'un indice
    chaineCompress = ""
    i = 0

    while i < len(chaine) :
        #Compteur à 1 pour le caractère courant
        cptChar = 1

        #Si le suivant est égale au courant et qu'il existe dans la chaine, et que le compteur ne dépasse pas 9...
        while i+1 < len(chaine) and chaine[i] == chaine[i+1] and cptChar < 9:
            #...on incrémente le compteur et l'indice
            cptChar += 1
            i += 1

        #On ajoute à la chaine compressée le compteur et le caractére
        chaineCompress += str(cptChar) + chaine[i]
        #On passe au prochain caractère
        i += 1

    return chaineCompress

def RLE(chaine : str, iteration : int) :
    if iteration == 0 :
        return ""
    else :
        return     
    return chaineCompress

print(RLE("aaabccd"))
print(RLE("abc"))

print(RLE("abbccc"))

print(RLE("aaabaa"))
print(RLE("aAa"))
print(RLE("WWWWWWWWWWWWW"))
print(RLE("WWWWWWWWWBWWWWWWWWBBBWWWBWWWWWWW"))
