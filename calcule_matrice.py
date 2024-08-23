import numpy as np
import time

# fonctions
# tous ces calculs sont effectuer sans backside
def liste_indice(formule, nH, nL, dH, dL):
    liste_n = []
    liste_d = []
    for lettre in formule:
        if lettre == "H":
            liste_n.append(nH)
            liste_d.append(dH)
        elif lettre == "L":
            liste_n.append(nL)
            liste_d.append(dL)
    return liste_n, liste_d


def phi(n, d, lamb):
    return (2 * np.pi / lamb) * n * d


def M(phi, n):
    return np.array(
        [[np.cos(phi), 1j * np.sin(phi) / n], [1j * n * np.sin(phi), np.cos(phi)]]
    )


def calcule_matrice(ns, liste_n, liste_d, phi, lambd):
    liste_Y = []
    for i in range(len(lambd)):
        M_tot = np.eye(2, dtype=complex)
        for j in range(len(liste_n)):
            phi_j = phi(liste_n[j], liste_d[j], lambd[i])
            M_j = M(phi_j, liste_n[j])
            M_tot = np.dot(M_j, M_tot)
        Y = (M_tot[1][0] + ns * M_tot[1][1]) / (M_tot[0][0] + ns * M_tot[0][1])
        liste_Y.append(Y)
    return liste_Y


def calcule_matrice_liste_ns(liste_ns, liste_n, liste_d,phi, lg_onde):

    liste_Y = []
    for j in range(len(lg_onde)):
        vec = np.array([1, liste_ns[j]])

        phi_j = phi(liste_n[j], liste_d[j], lg_onde[j])
        matrice = np.array([
            [np.cos(phi_j), 1j * np.sin(phi_j) / liste_n[j]],
            [1j * liste_n[j] * np.sin(phi_j), np.cos(phi_j)]
        ])
        M = np.dot(matrice, vec)
        B, C = M
        Y = C / B
        liste_Y.append(Y)
        
    return liste_Y

# def calcule_matrice_liste_polycouche(liste_ns, liste_nH,liste_nL,liste_d, phi, lg_onde,formule,liste_indice):

#     liste_Y = []
#     for j in range(len(lg_onde)):
#         vec = np.array([1,liste_ns[j]])
#         liste_n=liste_indice(formule,liste_nH[j],liste_nL[j],0,0)[0]
#         for k in range(len(liste_n)):
#             phi_j = phi(liste_n[k], liste_d[k], lg_onde[j])
#             matrice = np.array([
#                 [np.cos(phi_j), 1j * np.sin(phi_j) / liste_n[k]],
#                 [1j * liste_n[k] * np.sin(phi_j), np.cos(phi_j)]
#             ])
            
#             vec = np.dot(matrice, vec)
        
#         B, C = vec
#         Y = C / B
#         liste_Y.append(Y)
        
#     return liste_Y

def calcule_matrice_liste_multicouches(liste_ns, liste_nH, liste_nL, liste_d_H,liste_d_L, phi, lg_onde, formule, liste_indice):
   
    liste_Y = []
    for j in range(len(lg_onde)):
        vec = np.array([1, liste_ns[j]], dtype=complex)
        for m in range(len(liste_d_H)):
            liste_n, epaisseurs = liste_indice(formule, liste_nH[j], liste_nL[j], liste_d_H[m], liste_d_L[m])

        for k in range(len(liste_n)):
            phi_j = phi(liste_n[k], epaisseurs[k], lg_onde[j])
            matrice = np.array([
                [np.cos(phi_j), 1j * np.sin(phi_j) / liste_n[k]],
                [1j * liste_n[k] * np.sin(phi_j), np.cos(phi_j)]
            ], dtype=complex)

            vec = np.dot(matrice, vec)

        B, C = vec

        Y = C / B
        liste_Y.append(Y)

    return liste_Y

def calcule_R_matrice(liste_Y):
    liste_R = [
        (1 - np.real(Y)) ** 2 / (1 + np.real(Y)) ** 2 for Y in liste_Y
    ] 
    return liste_R


def calcule_T(liste_R):
    liste_T = [1 - R for R in liste_R]
    return liste_T


def calcule_R_ns(liste_ns):
    liste_R = []
    for ns in liste_ns:
        liste_R.append(((1 - ns) / (ns + 1)) ** 2)
    return liste_R
