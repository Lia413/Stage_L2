from calcule_indice import *
from aide import *
from convert import (
    convertir_csv_en_liste,
    supprimer_premiere_ligne_csv,
    convertir_liste_en_txt,
    convert_dossier_xls_en_csv,
)

from val import *
from extremum import *
import matplotlib.pyplot as plt

# bool est vrai si on etudie Rmax pour obtenir l'indice de la couche


def trouver_n(
    chemin_dossier,
    chemin_new_dossier,
    chemin_fichier_nu,
    chemin_fichier_A,
    chemin_fichier_B,
    boolA=True,
    boolB=True,
    W=71,
):
    convert_dossier_xls_en_csv(chemin_dossier, chemin_new_dossier)

    supprimer_premiere_ligne_csv(chemin_fichier_nu)
    supprimer_premiere_ligne_csv(chemin_fichier_A)
    supprimer_premiere_ligne_csv(chemin_fichier_B)

    liste_lg_onde_nu, liste_T_nu, liste_R_nu = convertir_csv_en_liste(chemin_fichier_nu)
    liste_lg_onde_A, liste_T_A, liste_R_A = convertir_csv_en_liste(chemin_fichier_A)
    liste_lg_onde_B, liste_T_B, liste_R_B = convertir_csv_en_liste(chemin_fichier_B)
    # arrondir
    liste_lg_onde_nu = arrondir(liste_lg_onde_nu)
    liste_lg_onde_A = arrondir(liste_lg_onde_A)
    liste_lg_onde_B = arrondir(liste_lg_onde_B)

    liste_T_nu = convertir_pourcent(liste_T_nu)
    liste_R_nu = convertir_pourcent(liste_R_nu)
    liste_T_A = convertir_pourcent(liste_T_A)
    liste_T_B = convertir_pourcent(liste_T_B)
    liste_R_A = convertir_pourcent(liste_R_A)
    liste_R_B = convertir_pourcent(liste_R_B)

    # enlever absorbant
    # enleve où c'est absorbant

    (
        red_liste_lg_onde_nu,
        red_liste_T_nu,
        red_liste_R_nu,
    ) = enleve_longueur_onde_absorbant(liste_lg_onde_nu, liste_T_nu, liste_R_nu)
    red_liste_lg_onde_A, red_liste_T_A, red_liste_R_A = enleve_longueur_onde_absorbant(
        liste_lg_onde_A, liste_T_A, liste_R_A
    )
    red_liste_lg_onde_B, red_liste_T_B, red_liste_R_B = enleve_longueur_onde_absorbant(
        liste_lg_onde_B, liste_T_B, liste_R_B
    )

    liste_lg_A = garder_meme_val(red_liste_lg_onde_nu, red_liste_lg_onde_A)
    liste_lg_B = garder_meme_val(red_liste_lg_onde_nu, red_liste_lg_onde_B)

    red_liste_lg_onde_A, red_liste_R_A = enlever_R_abs(
        red_liste_R_A, red_liste_lg_onde_A, liste_lg_A
    )
    red_liste_lg_onde_B, red_liste_R_B = enlever_R_abs(
        red_liste_R_B, red_liste_lg_onde_B, liste_lg_B
    )
    red_liste_lg_onde_A, red_liste_T_A = enlever_R_abs(
        red_liste_T_A, red_liste_lg_onde_A, liste_lg_A
    )
    red_liste_lg_onde_B, red_liste_T_B = enlever_R_abs(
        red_liste_T_B, red_liste_lg_onde_B, liste_lg_B
    )

    div_red_liste_lg_onde_A = liste_1_sur_carre(red_liste_lg_onde_A)
    div_red_liste_lg_onde_B = liste_1_sur_carre(red_liste_lg_onde_B)

    # lissage
    smooth_liste_R_A = signal.savgol_filter(
        red_liste_R_A, window_length=W, polyorder=2, mode="nearest"
    )
    smooth_liste_R_B = signal.savgol_filter(
        red_liste_R_B, window_length=W, polyorder=2, mode="nearest"
    )
    smooth_liste_T_A = signal.savgol_filter(
        red_liste_T_A, window_length=W, polyorder=2, mode="nearest"
    )
    smooth_liste_T_B = signal.savgol_filter(
        red_liste_T_B, window_length=W, polyorder=2, mode="nearest"
    )

    smooth_liste_lg_A = signal.savgol_filter(
        red_liste_lg_onde_A, window_length=W, polyorder=2, mode="nearest"
    )
    smooth_liste_lg_B = signal.savgol_filter(
        red_liste_lg_onde_B, window_length=W, polyorder=2, mode="nearest"
    )
    # lg onde pour R
    min_lg_R_A = trouver_extremums(smooth_liste_R_A, red_liste_lg_onde_A)["minimum lg"]
    min_lg_R_B = trouver_extremums(smooth_liste_R_B, red_liste_lg_onde_B)["minimum lg"]
    max_lg_R_A = trouver_extremums(smooth_liste_R_A, red_liste_lg_onde_A)["maximum lg"]
    max_lg_R_B = trouver_extremums(smooth_liste_R_B, red_liste_lg_onde_B)["maximum lg"]

    # Rmin/max
    min_liste_R_A = trouver_extremums(smooth_liste_R_A, red_liste_lg_onde_A)[
        "minimum smooth"
    ]
    min_liste_R_B = trouver_extremums(smooth_liste_R_B, red_liste_lg_onde_B)[
        "minimum smooth"
    ]
    max_liste_R_A = trouver_extremums(smooth_liste_R_A, red_liste_lg_onde_A)[
        "maximum smooth"
    ]
    max_liste_R_B = trouver_extremums(smooth_liste_R_B, red_liste_lg_onde_B)[
        "maximum smooth"
    ]

    # lg onde pour T
    min_lg_T_A = trouver_extremums(smooth_liste_T_A, red_liste_lg_onde_A)["minimum lg"]
    min_lg_T_B = trouver_extremums(smooth_liste_T_B, red_liste_lg_onde_B)["minimum lg"]
    max_lg_T_A = trouver_extremums(smooth_liste_T_A, red_liste_lg_onde_A)["maximum lg"]
    max_lg_T_B = trouver_extremums(smooth_liste_T_B, red_liste_lg_onde_B)["maximum lg"]

    # Tmin/max
    min_T_A = trouver_extremums(smooth_liste_T_A, red_liste_lg_onde_A)["minimum smooth"]
    min_T_B = trouver_extremums(smooth_liste_T_B, red_liste_lg_onde_B)["minimum smooth"]
    max_T_A = trouver_extremums(smooth_liste_T_A, red_liste_lg_onde_A)["minimum smooth"]
    max_T_B = trouver_extremums(smooth_liste_T_B, red_liste_lg_onde_B)["maximum smooth"]

    # ns
    liste_n_ex = calcule_n_ex(red_liste_T_nu)
    liste_n_ex = np.array(liste_n_ex)

    # liste indice substrat
    liste_div_lg_nu = liste_1_sur_carre(red_liste_lg_onde_nu)

    a_s, b_s, c_s = np.polyfit(liste_div_lg_nu, liste_n_ex, 2)

    liste_div_lg_max_A = liste_1_sur_carre(max_lg_R_A)
    liste_div_lg_max_B = liste_1_sur_carre(max_lg_R_B)
    liste_div_lg_min_A = liste_1_sur_carre(min_lg_R_A)
    liste_div_lg_min_B = liste_1_sur_carre(min_lg_R_B)

    # trouver tous les n par reg lin

    liste_tous_ns = trouver_tous_les_n(a_s, b_s, c_s, liste_div_lg_nu)


    # T avec backside
    liste_TmaxWith_A = T_with(max_liste_R_A)
    liste_TmaxWith_B = T_with(max_liste_R_B)
    liste_TminWith_A = T_with(min_liste_R_A)
    liste_TminWith_B = T_with(min_liste_R_B)

    # Rmin/max sans backside
    # par R
    liste_RmaxWout_A = calcule_R_wout(liste_TmaxWith_A, liste_tous_ns)
    liste_RmaxWout_B = calcule_R_wout(liste_TmaxWith_B, liste_tous_ns)

    liste_RminWout_A = calcule_R_wout(liste_TminWith_A, liste_tous_ns)
    liste_RminWout_B = calcule_R_wout(liste_TminWith_B, liste_tous_ns)

    # par T
    liste_RmaxWout_A_T = calcule_R_wout(min_T_A, liste_tous_ns)
    liste_RmaxWout_B_T = calcule_R_wout(min_T_B, liste_tous_ns)
    liste_RminWout_A_T = calcule_R_wout(max_T_A, liste_tous_ns)
    liste_RminWout_B_T = calcule_R_wout(max_T_B, liste_tous_ns)

    
    liste_div_lg_max_A = liste_1_sur_carre(max_lg_R_A)
    liste_div_lg_max_B = liste_1_sur_carre(max_lg_R_B)
    liste_div_lg_min_A = liste_1_sur_carre(min_lg_R_A)
    liste_div_lg_min_B = liste_1_sur_carre(min_lg_R_B)

    if boolA == True and boolB == True:
        liste_n_A = trouve_indice_liste(liste_RmaxWout_A, liste_tous_ns)
        liste_n_B = trouve_indice_liste(liste_RmaxWout_B, liste_tous_ns)
        liste_n_A_T = trouve_indice_liste(liste_RmaxWout_A_T, liste_tous_ns)
        liste_n_B_T = trouve_indice_liste(liste_RmaxWout_B_T, liste_tous_ns)
        if len(liste_div_lg_max_A) > 2 and len(liste_div_lg_max_B) > 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 2)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 2)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 2)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
          
        elif len(liste_div_lg_max_A) <= 2 and len(liste_div_lg_max_B) > 2:
            a_A, b_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 1)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 2)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 1)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_max_A) > 2 and len(liste_div_lg_max_B) <= 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 2)
            a_B, b_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 1)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 2)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_max_A) <= 2 and len(liste_div_lg_max_B) <= 2:
            a_A, b_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 1)
            a_B, b_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 1)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 1)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)

    elif boolA == True and boolB != True:
        liste_n_A = trouve_indice_liste(liste_RmaxWout_A, liste_tous_ns)
        liste_n_B = trouve_indice_liste(liste_RminWout_B, liste_tous_ns)
        liste_n_A_T = trouve_indice_liste(liste_RmaxWout_A_T, liste_tous_ns)
        liste_n_B_T = trouve_indice_liste(liste_RminWout_B_T, liste_tous_ns)
        if len(liste_div_lg_max_A) > 2 and len(liste_div_lg_min_B) > 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 2)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 2)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 2)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_max_A) <= 2 and len(liste_div_lg_min_B) > 2:
            a_A, b_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 1)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 2)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 1)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(a_A_T, b_A_T,0, div_red_liste_lg_onde_A)
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_max_A) > 2 and len(liste_div_lg_min_B) <= 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 2)
            a_B, b_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 1)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 2)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_max_A) <= 2 and len(liste_div_lg_min_B) <= 2:
            a_A, b_A = np.polyfit(liste_div_lg_max_A, liste_n_A, 1)
            a_B, b_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 1)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_max_A, liste_n_A_T, 1)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)

    elif boolA != True and boolB == True:
        liste_n_A = trouve_indice_liste(liste_RminWout_A, liste_tous_ns)
        liste_n_B = trouve_indice_liste(liste_RmaxWout_B, liste_tous_ns)
        liste_n_A_T = trouve_indice_liste(liste_RminWout_A_T, liste_tous_ns)
        liste_n_B_T = trouve_indice_liste(liste_RmaxWout_B_T, liste_tous_ns)
        if len(liste_div_lg_min_A) > 2 and len(liste_div_lg_max_B) > 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 2)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 2)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 2)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_min_A) <= 2 and len(liste_div_lg_max_B) > 2:
            a_A, b_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 1)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 2)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 1)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_min_A) > 2 and len(liste_div_lg_max_B) <= 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 2)
            a_B, b_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 1)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 2)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_min_A) <= 2 and len(liste_div_lg_max_B) <= 2:
            a_A, b_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 1)
            a_B, b_B = np.polyfit(liste_div_lg_max_B, liste_n_B, 1)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 1)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_max_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
    else:
        liste_n_A = trouve_indice_liste(liste_RminWout_A, liste_tous_ns)
        liste_n_B = trouve_indice_liste(liste_RminWout_B, liste_tous_ns)
        liste_n_A_T = trouve_indice_liste(liste_RminWout_A_T, liste_tous_ns)
        liste_n_B_T = trouve_indice_liste(liste_RminWout_B_T, liste_tous_ns)
        if len(liste_div_lg_min_A) > 2 and len(liste_div_lg_min_B) > 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 2)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 2)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 2)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)

            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
        elif len(liste_div_lg_min_A) <= 2 and len(liste_div_lg_min_B) > 2:
            a_A, b_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 1)
            a_B, b_B, c_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 2)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 1)
            a_B_T, b_B_T, c_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 2)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, c_B, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, c_B_T, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_min_A) > 2 and len(liste_div_lg_min_B) <= 2:
            a_A, b_A, c_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 2)
            a_B, b_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 1)
            a_A_T, b_A_T, c_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 2)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, c_A, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, c_A_T, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
        elif len(liste_div_lg_min_A) <= 2 and len(liste_div_lg_min_B) <= 2:
            a_A, b_A = np.polyfit(liste_div_lg_min_A, liste_n_A, 1)
            a_B, b_B = np.polyfit(liste_div_lg_min_B, liste_n_B, 1)
            a_A_T, b_A_T = np.polyfit(liste_div_lg_min_A, liste_n_A_T, 1)
            a_B_T, b_B_T = np.polyfit(liste_div_lg_min_B, liste_n_B_T, 1)
            liste_tous_n_A = trouver_tous_les_n(a_A, b_A, 0, div_red_liste_lg_onde_A)
            liste_tous_n_B = trouver_tous_les_n(a_B, b_B, 0, div_red_liste_lg_onde_B)
            liste_tous_n_A_T = trouver_tous_les_n(
                a_A_T, b_A_T, 0, div_red_liste_lg_onde_A
            )
            liste_tous_n_B_T = trouver_tous_les_n(
                a_B_T, b_B_T, 0, div_red_liste_lg_onde_B
            )
            liste_n_T_et_R_A = combine_n(liste_tous_n_A, liste_tous_n_A_T)
            liste_n_T_et_R_B = combine_n(liste_tous_n_B, liste_tous_n_B_T)
            incertitude_A=incertitude_n(liste_tous_n_A,liste_tous_n_A_T)
            incertitude_B=incertitude_n(liste_tous_n_B,liste_tous_n_B_T)
            


    return (
        smooth_liste_lg_A,
        smooth_liste_lg_B,
        smooth_liste_T_A,
        smooth_liste_T_B,
        smooth_liste_R_A,
        smooth_liste_R_B,
        liste_tous_ns,
        red_liste_T_nu,
        liste_n_T_et_R_A,
        red_liste_lg_onde_A,
        liste_n_T_et_R_B,
        red_liste_lg_onde_B,
        red_liste_lg_onde_nu,
        incertitude_A,
        incertitude_B,
        liste_tous_n_A,
        liste_tous_n_B,
        liste_tous_n_A_T,
        liste_tous_n_B_T,

    )
