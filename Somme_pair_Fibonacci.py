# Objectif : somme des termes paires de la suite de Fibonacci

# Déclaration des variables

a = 1.0
b = 2.0
c = 3.0
somme = 2.0
max_number = 4000000

while c < max_number : 
    if (c/2).is_integer()==True:    # détermine si le dernier terme de la suite est paire.
        somme = somme + c           # S'il est pair, on le compte dans la somme

    a = b                           # Il est important de calculer le dernier terme de la suite 
    b = c                           # en fin de boucle pour que la valeur testée par la condition 
    c = a + b                       # while soit la dernière valeur obtenue.

print (somme)
