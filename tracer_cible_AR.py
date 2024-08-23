import numpy as np
def creer_lg():
    liste_lg=[]
    for i in range(400,800,1):
        liste_lg.append(i)
    return liste_lg
def creer_cible_AR(liste_lg):
    liste_R1_target=[]
    liste_lg1=[]
    liste_R2_target=[]
    liste_lg2=[]

    for i in range(len(liste_lg)):
        if 400<=liste_lg[i]<=480:
            liste_R1_target.append(1)
            liste_lg1.append(liste_lg[i])
        if 640<=liste_lg[i]<=720:
            liste_R2_target.append(0)
            liste_lg2.append(liste_lg[i])
        

    return liste_R1_target,liste_lg1,liste_R2_target,liste_lg2


import matplotlib.pyplot as plt

liste_lg=creer_lg()
liste_T1_target,liste_lg1,liste_T2_target,liste_lg2=creer_cible_AR(liste_lg)

plt.plot(liste_lg1,liste_T1_target,'b.')
plt.plot(liste_lg2,liste_T2_target,'b.')


plt.xlabel('longueur d\'onde')
plt.ylabel('Réflexion')
plt.title('Filtre cible en Réflexion')
plt.legend()
plt.show()
