
# EXERCICE

mdp=input("Entrez le mot de pass:")
if mdp==" ":
    print("votre mot de passe de est trop court".upper())
elif len(mdp)<8:
    print("votre mot de passe est trop court".capitalize())
elif type(mdp)!=str():
    print("votre mot de passe ne contient que des nombre.")
else:
    print(" Inscription terminer !")
    
######################################  REPONSES AUX QUESTIONS ##########################################

# Pour verifier la validité du mot depasse on doit se basé sur le mot de passe entre par l'utilusateur en suite on le faire passé 
# dans la boucle conditionnel en analysant la taille et le type de chaine de caractere entré par l'utilusateur.
