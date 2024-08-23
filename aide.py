import numpy as np


def convertir_pourcent(liste):
    modif_liste = []
    for elmt in liste:
        modif_liste.append(elmt / 100)
    return modif_liste

def convertir_fois_100(liste):
    modif_liste=[]
    for elmt in liste:
        modif_liste.append(elmt*100)
    return modif_liste


def enleve_longueur_onde_absorbant(lg_onde, T, R):
    liste_T = []
    liste_R = []
    liste_lg_onde = []
    for i in range(len(T)):
        if T[i] + R[i] >= 0.98:
            liste_T.append(T[i])
            liste_R.append(R[i])
            liste_lg_onde.append(lg_onde[i])
    return liste_lg_onde, liste_T, liste_R


def enlever_au_dela_1500(liste_lg, liste_R, liste_T):
    liste_r = []
    liste_t = []
    liste_lg_onde = []
    for i in range(len(liste_lg)):
        if liste_lg[i] <= 1500:
            liste_lg_onde.append(liste_lg[i])
            liste_r.append(liste_R[i])
            liste_t.append(liste_T[i])
    return liste_lg_onde, liste_r, liste_t


def enlever_au_dela_1000(liste_lg, liste_R, liste_T):
    liste_r = []
    liste_t = []
    liste_lg_onde = []
    for i in range(len(liste_lg)):
        if liste_lg[i] <= 1000:
            liste_lg_onde.append(liste_lg[i])
            liste_r.append(liste_R[i])
            liste_t.append(liste_T[i])
    return liste_lg_onde, liste_r, liste_t


def enlever_R_abs(liste_R_m, lg_onde, lg_onde_m):
    liste_R = []
    liste_lg = []
    for i in range(len(lg_onde)):
        for k in range(len(lg_onde_m)):
            if lg_onde[i] == lg_onde_m[k]:
                liste_lg.append(lg_onde_m[k])
                liste_R.append(liste_R_m[i])
    return liste_lg, liste_R


def enlever_R_abs_cond(liste_R_m, lg_onde, lg_onde_m):
    liste_R = []
    liste_lg = []

    for i in range(len(lg_onde)):
        if lg_onde[i] in lg_onde_m:
            liste_lg.append(lg_onde[i])
            liste_R.append(liste_R_m[i])

    return liste_lg, liste_R


def garder_meme_val(liste1, liste2):
    liste = []
    for x in liste1:
        for y in liste2:
            if x == y:
                liste.append(x)
    return liste


def liste_1_sur_carre(liste_lg_max):
    liste_div_lg_max = []
    for elmt in liste_lg_max:
        liste_div_lg_max.append(1 / elmt**2)
    return liste_div_lg_max


def arrondir(liste):
    new_liste = []
    for elmt in liste:
        new_liste.append(np.around(elmt, decimals=0))
    return new_liste

def incertitude_n(liste_n_par_R,liste_n_par_T):
    moy_n_par_R=0
    moy_n_par_T=0
    for x in liste_n_par_R:
        moy_n_par_R+=x
    moy_n_par_R=moy_n_par_R/len(liste_n_par_R)
    for y in liste_n_par_T:
        moy_n_par_T+=y
    moy_n_par_T=moy_n_par_T/len(liste_n_par_T)
    delta_n=50*np.abs((moy_n_par_R-moy_n_par_T)/(moy_n_par_R+moy_n_par_T))
    return delta_n



