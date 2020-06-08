# Objectif : plus grand facteur premier d'un nombre n


# Données
n =  600851475143 # 13195.0  

# Fonction nombre premier


def fun_prime_nb(a):
    sortie=False
    for k in range(a):
        if ((i+1)/(k+1)).is_integer() == True and (k+1)!=1 and (k+1)!=(i+1): #Si le diviseur de n n'est pas un nb 1er
            sortie = True
            break                                                          # On sors de la boucle
    return sortie
        

# Algo

product_factor=1
for i in range(int(n)):
    if (n/(i+1)).is_integer() == True:  # Determination des diviseurs de n
        if fun_prime_nb(i+1) == False:
                prime_factor = i+1
                print(prime_factor)    # Affiche chaque nombre premier
        product_factor = product_factor * prime_factor
        if product_factor == n:
            quit()                      # S'arrête lorsque la décomposition est complète
print(prime_factor)                     # Affiche le dernier nombre premier

