# Objectif : somme des multiples de 3 et de 5 en dessous de 1000

# Déclaration des variables

max_number = 1000          # Limite supérieure 
a = 0.0                   # Nombre testé
somme = 0.0               # Somme

# Aglo

for a in range(max_number-1):
    a = a + 1.0       # incrémentation du nombre testé
    b=a/3              
    c=a/5

    if (b.is_integer()==True or c.is_integer()==True):  # si a est un multiple de 3 (b.is_integer()==True) ou de 5 (c.is_integer()==True)
       somme = somme + a    # On ajoute a à la somme totale des multiples
       

print(somme)    # Affichage du résultat