
############# EXO 1 #############

phrase= "Bonjour tout le monde."
n_phrase="Bonsoir"+" tout le monde."
print(phrase)
print(n_phrase)


############ EXO 2 ############

lettre_a_cherche="o"
phrase="Bonjour tout le monde"
resultat=phrase.count(lettre_a_cherche)
print(f"le nombre est:{resultat}!")

############ EXO 3 ############


lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
nombre=lorem.count(".")
print(f"Le nombre de phrase est: {nombre} !")




############ EXO 4 ############

chaine="Pierre, Julien, Anne, Marie, Lucien"
a=list(chaine.split(", "))
a.sort()
b=", ".join(list(a))
print(b)





