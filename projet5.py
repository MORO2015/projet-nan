
# EXERCICE: BOUCLE FOR 

for num in range(2,101):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num, end="-")
        
        
        # EXERCICE: BOUCLE WHILE

def premier (nb):
     
    if nb == 0 or nb == 1 :
        return False
    else :
        racine = nb**0.5
        diviseur = 2
        while diviseur <= racine :
            if nb % diviseur == 0 :
                return False
            
            diviseur = diviseur + 1

        return True
    ### Debut programme ###
nombre = 0
nombre2 = 0
 
while nombre != 100 :
    nombre2 = nombre2 + 1
    for nombre in range(1, 101):
        if premier(nombre):
            print(nombre, end = ", ")
