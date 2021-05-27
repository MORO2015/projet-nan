
# Affichage des fonctions du programme

print("######## Veillez entrez un nombre de 1 à 5 pour une operation! #########")
print("(1): Ajouter un élément à votre liste de courses")
print("(2): Retirer un élément de votre liste de courses")
print("(3): Afficher les éléments de votre liste de courses")
print("(4): Vider votre liste de courses")
print("(5): Quitter le programme")
liste=[]
# La boucle d'iteration
while (nbre>=1 or nbre<=5):
    nbre=int(input("Quelle operation voulez vous faire:"))
    if nbre==1:
        elnt_A=str(input("Ajouter un élément de votre liste:"))
        liste.append(elnt_A)
        print("Element ajouté avec succes!")
    elif nbre==2:
        elnt_R=str(input("Retirer un élément de votre liste:"))
        liste.remove(elnt_R)
        print("Element retirer avec succes!")
    elif nbre==3:
        print(f"les element ajoutés sont les suivants:{liste}")
    elif nbre==4:
        liste.clear()
        print("Votre liste de courses a été vider!")
    elif nbre==5:
        print("Au revoir!")
        break
