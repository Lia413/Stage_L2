from val import (
    chemin_dossier,
    chemin_new_dossier,
    chemin_YF3_A,
    chemin_YF3_B,
    chemin_fichier_A_ZnS,
    chemin_fichier_B_ZnS,
    chemin_fichier_nu,
    chemin_fichier_A,
    chemin_fichier_B,
    nH,
    nL,
    dH,
    dL,
    liste_lg_onde,
)
from aide import *
from convert import *
from calcule_indice import *
from calcule_matrice import *
from calcule_indice_fonction import *
from extremum import *
from mesures import *
# from modif_fonction import *


# calcule matrice
# stockage

formule = "HLHLHLHLHLHL"
liste_n, liste_d = liste_indice(formule, nH, nL, dH, dL)
liste_Y = calcule_matrice(ns, liste_n, liste_d, phi, liste_lg_onde)
liste_R = calcule_R_matrice(liste_Y)
liste_T = calcule_T(liste_R)
convertir_liste_en_txt(
    liste_R,
    liste_lg_onde,
    "/Users/lisa/Desktop/Stage_L2/comp open:programm",
    "HLHLHLHLHLHL,dh=100,dl=300,nH=2.35,nL=1.45,ns=1.52",
)
supprimer_premiere_ligne_csv('/Users/lisa/Desktop/Stage_L2/fichier_csv/Echant 1 - UHC 2 - 02-07.csv')
lg_UHC_rectif,T_uhc_rectif,R_uhc_rectif=convertir_csv_en_liste('/Users/lisa/Desktop/Stage_L2/fichier_csv/Echant 1 - UHC 2 - 02-07.csv')
R_uhc_rectif=convertir_pourcent(R_uhc_rectif)
T_uhc_rectif=convertir_pourcent(T_uhc_rectif)

convertir_liste_en_txt(R_uhc_rectif,lg_UHC_rectif,chemin,'R rectif uhc')
convertir_liste_en_txt(T_uhc_rectif,lg_UHC_rectif,chemin,'T rectif uhc')



# print('liste_R matrice',liste_R)
# print('liste_T',liste_T)
# print('liste_R_theo',liste_R_theo)
# tracer cos(phi) pour verif en fonction de lambda


# grosse fonction
(
    smooth_liste_lg_A,
    smooth_liste_lg_B,
    smooth_liste_T_A_ZnS_vitesse,
    smooth_liste_T_B_ZnS_vitesse,
    smooth_liste_R_A_ZnS_vitesse,
    smooth_liste_R_B_ZnS_vitesse,
    liste_tous_ns,
    red_liste_T_nu,
    liste_n_T_et_R_A_vitesse,
    red_liste_lg_onde_A,
    liste_n_T_et_R_B_vitesse,
    red_liste_lg_onde_B,
    red_lg_onde_nu_vitesse,
    incertitude_A_vitesse,
    incertitude_B_vitesse,
    liste_tous_n_A_vitesse,
    liste_tous_n_B_vitesse,
    liste_tous_n_A_T_vitesse,
    liste_tous_n_B_T_vitesse
) = trouver_n(
    chemin_dossier,
    chemin_new_dossier,
    chemin_fichier_nu,
    chemin_fichier_A,
    chemin_fichier_B,
)


(
    smooth_liste_lg_A_ZnS,
    smooth_liste_lg_B_ZnS,
    smooth_liste_T_A_ZnS,
    smooth_liste_T_B_ZnS,
    smooth_liste_R_A_ZnS,
    smooth_liste_R_B_ZnS,
    liste_tous_ns,
    red_liste_T_nu,
    liste_n_T_et_R_A_ZnS,
    red_liste_lg_onde_A_ZnS,
    liste_n_T_et_R_B_ZnS,
    red_liste_lg_onde_B_ZnS,
    red_lg_onde_nu_ZnS,
    incertitude_A_ZnS,
    incertitude_B_ZnS,
    liste_tous_n_A_ZnS,
    liste_tous_n_B_ZnS,
    liste_tous_n_A_T_ZnS,
    liste_tous_n_B_T_ZnS
) = trouver_n(
    chemin_dossier,
    chemin_new_dossier,
    chemin_fichier_nu,
    chemin_fichier_A_ZnS,
    chemin_fichier_B_ZnS,
)


(
    smooth_liste_lg_A_YF3,
    smooth_liste_lg_B_YF3,
    smooth_liste_T_A_YF3,
    smooth_liste_T_B_YF3,
    smooth_liste_R_A_YF3,
    smooth_liste_R_B_YF3,
    liste_tous_ns,
    red_liste_T_nu,
    liste_n_T_et_R_A_YF3,
    red_liste_lg_onde_A_YF3,
    liste_n_T_et_R_B_YF3,
    red_liste_lg_onde_B_YF3,
    red_lg_onde_nu_YF3,
    incertitude_A_YF3,
    incertitude_B_YF3,
    liste_tous_n_A_YF3,
    liste_tous_n_B_YF3,
    liste_tous_n_A_T_YF3,
    liste_tous_n_B_T_YF3
) = trouver_n(
    chemin_dossier,
    chemin_new_dossier,
    chemin_fichier_nu,
    chemin_YF3_A,
    chemin_YF3_B,
    boolA=False,
    boolB=False,
)


red_liste_lg_onde_A_YF3_1000,liste_tous_n_A_T_YF3_1000,liste_tous_n_A_YF3_1000=enlever_au_dela_1000(red_liste_lg_onde_A_YF3,liste_tous_n_A_T_YF3,liste_tous_n_A_YF3)
red_liste_lg_onde_B_YF3_1000,liste_tous_n_B_T_YF3_1000,liste_tous_n_B_YF3_1000=enlever_au_dela_1000(red_liste_lg_onde_B_YF3,liste_tous_n_B_T_YF3,liste_tous_n_B_YF3)
red_lg_onde_nu_YF3_1000,liste_tous_ns_1000,liste_tous_T_nu_1000=enlever_au_dela_1000(red_lg_onde_nu_YF3,liste_tous_ns,red_liste_T_nu)

# plt.plot(red_lg_onde_nu_YF3_1000,liste_tous_ns_1000,label='ns')
plt.title(' La transmission de B270 en fonction des longueurs d\'onde' )
plt.xlabel('longueur d\'onde')
plt.ylabel('T')
plt.plot(red_lg_onde_nu_YF3_1000,liste_tous_T_nu_1000,label='T')
plt.legend()
plt.show()


incertitude_A_YF3_1000=incertitude_n(liste_tous_n_A_YF3_1000,liste_tous_n_A_T_YF3_1000)
incertitude_B_YF3_1000=incertitude_n(liste_tous_n_B_YF3_1000,liste_tous_n_B_T_YF3_1000)




print('incertitude_A_ZnS',incertitude_A_ZnS)
print('incertitude_B_ZnS',incertitude_B_ZnS)
print('incertitude_A_YF3',incertitude_A_YF3)
print('incertitude_B_YF3',incertitude_B_YF3)
print('incertitude_A_YF3_1000',incertitude_A_YF3_1000)
print('incertitude_B_YF3_1000',incertitude_B_YF3_1000)

d_YF3_A = 671.740
d_ZnS_A = 606.6447
liste_d_YF3_A = [671.740] * len(liste_n_T_et_R_A_YF3)
liste_d_ZnS_A = [606.6447] * len(liste_n_T_et_R_A_ZnS)
liste_d_YF3_B = [671.740] * len(
    liste_n_T_et_R_A_YF3
)  # changer la valeur mettre la vraie
liste_d_ZnS_B = [606.6447] * len(liste_n_T_et_R_B_YF3)
print(len(liste_tous_ns))
print(len(liste_n_T_et_R_A_YF3))
print(len(liste_n_T_et_R_A_ZnS))
print(len(red_liste_lg_onde_A_YF3))
print(len(red_liste_lg_onde_A_ZnS))


liste_Y_YF3_A = calcule_matrice_liste_ns(
    liste_tous_ns, liste_n_T_et_R_A_YF3, liste_d_YF3_A, phi, red_liste_lg_onde_A_YF3
)
liste_R_YF3_A = calcule_R_matrice(liste_Y_YF3_A)
liste_T_YF3_A = calcule_T(liste_R_YF3_A)

liste_Y_ZnS_A = calcule_matrice_liste_ns(
    liste_tous_ns, liste_n_T_et_R_A_ZnS, liste_d_ZnS_A, phi, red_liste_lg_onde_A_ZnS
)
liste_R_ZnS_A = calcule_R_matrice(liste_Y_ZnS_A)
liste_T_ZnS_A = calcule_T(liste_R_ZnS_A)

liste_Y_YF3_B = calcule_matrice_liste_ns(
    liste_tous_ns, liste_n_T_et_R_B_YF3, liste_d_YF3_B, phi, red_liste_lg_onde_B_YF3
)  # changer liste d en B
liste_R_YF3_B = calcule_R_matrice(liste_Y_YF3_B)
liste_T_YF3_B = calcule_T(liste_R_YF3_B)

liste_Y_ZnS_B = calcule_matrice_liste_ns(
    liste_tous_ns, liste_n_T_et_R_B_ZnS, liste_d_ZnS_B, phi, red_liste_lg_onde_B_ZnS
)
liste_R_ZnS_B = calcule_R_matrice(liste_Y_ZnS_B)
liste_T_ZnS_B = calcule_T(liste_R_ZnS_B)

# # print
# print(trouver_n(chemin_dossier,chemin_new_dossier,chemin_fichier_nu,chemin_fichier_A,chemin_fichier_B,boolA=False,boolB=False))

# print(trouver_n(chemin_dossier,chemin_new_dossier,chemin_fichier_nu,chemin_fichier_A,chemin_fichier_B))


print("len(smooth_liste_R_A_ZnS)", len(smooth_liste_R_A_ZnS))
print("liste_R_A_ZnS)", len(liste_R_ZnS_A))
print("len(smooth_liste_R_A_YF3)", len(smooth_liste_R_A_YF3))
print("liste_R_A_YF3)", len(liste_R_YF3_A))
print(
    "erreur_quadratique_liste(smooth_liste_R_A_ZnS, red_lg_onde_ZnS_A,red_R_ZnS_A )",
    erreur_quadratique_liste(
        smooth_liste_R_A_ZnS, red_liste_lg_onde_A_ZnS, liste_R_ZnS_A
    ),
)
print(
    "erreur_quadratique_liste(smooth_liste_R_B_ZnS, red_lg_onde_ZnS_B,red_R_ZnS_B)",
    erreur_quadratique_liste(
        smooth_liste_R_B_ZnS, red_liste_lg_onde_B_ZnS, liste_R_ZnS_B
    ),
)
print(
    "erreur_quadratique_liste(smooth_liste_R_A_YF3, red_lg_onde_YF3_A,red_R_YF3_A)",
    erreur_quadratique_liste(
        smooth_liste_R_A_YF3, red_liste_lg_onde_A_YF3, liste_R_YF3_A
    ),
)
print(
    "erreur_quadratique_liste(smooth_liste_R_B_YF3, red_lg_onde_YF3_B,red_R_YF3_B)",
    erreur_quadratique_liste(
        smooth_liste_R_B_YF3, red_liste_lg_onde_B_YF3, liste_R_YF3_B
    ),
)

# convertir
convertir_liste_en_txt(
    liste_n_T_et_R_A_vitesse, red_liste_lg_onde_A, chemin, "ZnS A 4xvitesse 71"
)
convertir_liste_en_txt(
    liste_n_T_et_R_B_vitesse, red_liste_lg_onde_B, chemin, "ZnS B 4xvitesse 71"
)
convertir_liste_en_txt(
    liste_n_T_et_R_A_ZnS, red_liste_lg_onde_A_ZnS, chemin, "ZnS A 71"
)
convertir_liste_en_txt(
    liste_n_T_et_R_B_ZnS, red_liste_lg_onde_B_ZnS, chemin, "ZnS B 71"
)
convertir_liste_en_txt(
    liste_n_T_et_R_A_YF3, red_liste_lg_onde_A_YF3, chemin, "YF3_A _ fonct 71"
)
convertir_liste_en_txt(
    liste_n_T_et_R_B_YF3, red_liste_lg_onde_B_YF3, chemin, "YF3_B___ fonct 71"
)


chemin_UHC_A = "/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon A - UHC neb - 28-06-2024 copie.csv"
chemin_UHC_A_2="/Users/lisa/Desktop/Stage_L2/fichier_csv/Echant 1 - UHC 2 - 02-07.csv"
chemin_UHC_A_AR="/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon 1 UHC 2 + AR.csv"
chemin_UHC_A_AR_2="/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon A - UHC + AR - 02-07.csv"
chemin_UHC_B = "/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon B - UHC neb - 28-06-24 copie.csv"
chemin_UHC_C = "/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon C - UHC neb - 28-06-24 copie.csv"
chemin_UHC_D = "/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon D - UHC neb - 28-06-24 copie.csv"
chemin_UHC_E = "/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon E - UHC neb - 28-06-24 copie.csv"
chemin_UHC_F = "/Users/lisa/Desktop/Stage_L2/fichier_csv/Echantillon F - UHC neb - 26-06-24 copie.csv"

supprimer_premiere_ligne_csv(chemin_UHC_A)
supprimer_premiere_ligne_csv(chemin_UHC_A_2)
supprimer_premiere_ligne_csv(chemin_UHC_A_AR)
supprimer_premiere_ligne_csv(chemin_UHC_A_AR_2)



supprimer_premiere_ligne_csv(chemin_UHC_B)
supprimer_premiere_ligne_csv(chemin_UHC_C)
supprimer_premiere_ligne_csv(chemin_UHC_D)
supprimer_premiere_ligne_csv(chemin_UHC_E)
supprimer_premiere_ligne_csv(chemin_UHC_F)


liste_lg_onde_UHC_A, liste_T_UHC_A, liste_R_UHC_A = convertir_csv_en_liste_R_puis_T(chemin_UHC_A)
liste_lg_onde_UHC_A_2, liste_T_UHC_A_2, liste_R_UHC_A_2 = convertir_csv_en_liste(chemin_UHC_A_2)
liste_lg_onde_UHC_A_AR, liste_T_UHC_A_AR, liste_R_UHC_A_AR = convertir_csv_en_liste(chemin_UHC_A_AR)
liste_lg_onde_UHC_A_AR_2, liste_T_UHC_A_AR_2, liste_R_UHC_A_AR_2 = convertir_csv_en_liste(chemin_UHC_A_AR_2)

liste_lg_onde_UHC_B, liste_T_UHC_B, liste_R_UHC_B = convertir_csv_en_liste(chemin_UHC_B)
liste_lg_onde_UHC_C, liste_T_UHC_C, liste_R_UHC_C = convertir_csv_en_liste(chemin_UHC_C)
liste_lg_onde_UHC_D, liste_T_UHC_D, liste_R_UHC_D = convertir_csv_en_liste(chemin_UHC_D)
liste_lg_onde_UHC_E, liste_T_UHC_E, liste_R_UHC_E = convertir_csv_en_liste(chemin_UHC_E)
liste_lg_onde_UHC_F, liste_T_UHC_F, liste_R_UHC_F = convertir_csv_en_liste(chemin_UHC_F)


liste_T_UHC_A = convertir_pourcent(liste_T_UHC_A)
liste_R_UHC_A = convertir_pourcent(liste_R_UHC_A)

liste_T_UHC_A_2 = convertir_pourcent(liste_T_UHC_A_2)
liste_R_UHC_A_2 = convertir_pourcent(liste_R_UHC_A_2)

liste_T_UHC_A_AR = convertir_pourcent(liste_T_UHC_A_AR)
liste_R_UHC_A_AR = convertir_pourcent(liste_R_UHC_A_AR)

liste_T_UHC_A_AR_2 = convertir_pourcent(liste_T_UHC_A_AR_2)
liste_R_UHC_A_AR_2 = convertir_pourcent(liste_R_UHC_A_AR_2)

liste_T_UHC_B = convertir_pourcent(liste_T_UHC_B)
liste_R_UHC_B = convertir_pourcent(liste_R_UHC_B)


liste_T_UHC_C = convertir_pourcent(liste_T_UHC_C)
liste_R_UHC_C = convertir_pourcent(liste_R_UHC_C)


liste_T_UHC_D = convertir_pourcent(liste_T_UHC_D)
liste_R_UHC_D = convertir_pourcent(liste_R_UHC_D)

liste_T_UHC_E = convertir_pourcent(liste_T_UHC_E)
liste_R_UHC_E = convertir_pourcent(liste_R_UHC_E)


liste_T_UHC_F = convertir_pourcent(liste_T_UHC_F)
liste_R_UHC_F = convertir_pourcent(liste_R_UHC_F)



convertir_liste_en_txt(liste_T_UHC_A, liste_lg_onde_UHC_A, chemin, "UHC_A_T coeff")
convertir_liste_en_txt(liste_R_UHC_A, liste_lg_onde_UHC_A, chemin, "UHC_A_R")

convertir_liste_en_txt(liste_R_UHC_A_2, liste_lg_onde_UHC_A_2, chemin, "UHC_A_R_2")
convertir_liste_en_txt(liste_T_UHC_A_2, liste_lg_onde_UHC_A_2, chemin, "UHC_A_T_2")

convertir_liste_en_txt(liste_R_UHC_A_AR, liste_lg_onde_UHC_A_AR, chemin, "UHC_A_R_AR")
convertir_liste_en_txt(liste_T_UHC_A_AR, liste_lg_onde_UHC_A_AR, chemin, "UHC_A_T_AR")

convertir_liste_en_txt(liste_R_UHC_A_AR, liste_lg_onde_UHC_A_AR, chemin, "UHC_A_R_AR_2")
convertir_liste_en_txt(liste_T_UHC_A_AR, liste_lg_onde_UHC_A_AR, chemin, "UHC_A_T_AR_2")

convertir_liste_en_txt(liste_T_UHC_B, liste_lg_onde_UHC_B, chemin, "UHC_B_T")
convertir_liste_en_txt(liste_R_UHC_B, liste_lg_onde_UHC_B, chemin, "UHC_B_R")
convertir_liste_en_txt(liste_T_UHC_C, liste_lg_onde_UHC_C, chemin, "UHC_C_T")
convertir_liste_en_txt(liste_R_UHC_C, liste_lg_onde_UHC_C, chemin, "UHC_C_R")
convertir_liste_en_txt(liste_T_UHC_D, liste_lg_onde_UHC_D, chemin, "UHC_D_T")
convertir_liste_en_txt(liste_R_UHC_D, liste_lg_onde_UHC_D, chemin, "UHC_D_R")
convertir_liste_en_txt(liste_T_UHC_E, liste_lg_onde_UHC_E, chemin, "UHC_E_T")
convertir_liste_en_txt(liste_R_UHC_E, liste_lg_onde_UHC_E, chemin, "UHC_E_R")
convertir_liste_en_txt(liste_T_UHC_F, liste_lg_onde_UHC_F, chemin, "UHC_F_T")
convertir_liste_en_txt(liste_R_UHC_F, liste_lg_onde_UHC_F, chemin, "UHC_F_R")

