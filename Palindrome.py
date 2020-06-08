#Objectif : plus grand palindrome de la multipication de deux nombres à trois chiffres


#Données
a = 999
b = 999
c = a*b

#Algo
nombre = str(c)     #On place le résultat dans un tableau
compteur=0                 #Définition du compteur

while not( (nombre[0]==nombre[5]) and (nombre[1]==nombre[4]) and (nombre[2]==nombre[3])):   #Test si le résultats est un palindrome
#for i in range(80):
    compteur = compteur + 1                                                                      
    c = a*b
    print(compteur, a, b, c)
    nombre = str(c)
    if (compteur < 100 ):
        b=b-1
    else:
        if (compteur==100):
            a=a-1
            b=a
            compteur=0
