def creer_lg():
    liste_lg=[]
    for i in range(400,800,1):
        liste_lg.append(i)
    return liste_lg

def creer_target(liste_lg):
    liste_T1_target=[]
    liste_lg1=[]
    liste_T2_target=[]
    liste_lg2=[]
    liste_T3_target=[]
    liste_lg3=[]
    liste_T4_target=[]
    liste_lg4=[]

    for i in range(len(liste_lg)):
        if 400<=liste_lg[i]<=460:
            liste_T1_target.append(0)
            liste_lg1.append(liste_lg[i])
        if 480<=liste_lg[i]<=520:
            liste_T2_target.append(1)
            liste_lg2.append(liste_lg[i])
        if 540<=liste_lg[i]<=620:
            liste_T3_target.append(0)
            liste_lg3.append(liste_lg[i])
        if 640<=liste_lg[i]<=720:
            liste_T4_target.append(1)
            liste_lg4.append(liste_lg[i])

    return liste_T1_target,liste_lg1,liste_T2_target,liste_lg2,liste_T3_target,liste_lg3,liste_T4_target,liste_lg4

import matplotlib.pyplot as plt

liste_lg=creer_lg()
liste_T1_target,liste_lg1,liste_T2_target,liste_lg2,liste_T3_target,liste_lg3,liste_T4_target,liste_lg4=creer_target(liste_lg)

plt.plot(liste_lg1,liste_T1_target,'b.')
plt.plot(liste_lg2,liste_T2_target,'b.')
plt.plot(liste_lg3,liste_T3_target,'b.')
plt.plot(liste_lg4,liste_T4_target,'b.')

plt.xlabel('longueur d\'onde')
plt.ylabel('Transmission')
plt.title('Filtre cible en transmission')
plt.legend()
plt.show()