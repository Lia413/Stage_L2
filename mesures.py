from convert import *
from aide import *

# pour chaque fichier


supprimer_premiere_ligne_csv(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 - A -14-06-2024 11.16.csv"
)
supprimer_premiere_ligne_csv(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 - B - 2e - T et R 14-06-2024 15.49.csv"
)
supprimer_premiere_ligne_csv(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 ZnS A - T et R - 14-06-2024 14.31.csv"
)
supprimer_premiere_ligne_csv(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 ZnS - B - T et R 14-06-2024 15.18.csv"
)
supprimer_premiere_ligne_csv(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 YF3-A-14-06-2024 16.11.csv"
)
supprimer_premiere_ligne_csv(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 YF3 - B - T et R - 14-06-2024 16.33.csv"
)

lg_onde_nu_A, T_nu_A, R_nu_A = convertir_csv_en_liste(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 - A -14-06-2024 11.16.csv"
)
lg_onde_nu_B, T_nu_B, R_nu_B = convertir_csv_en_liste(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 - B - 2e - T et R 14-06-2024 15.49.csv"
)
lg_onde_ZnS_A, T_ZnS_A, R_ZnS_A = convertir_csv_en_liste(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 ZnS A - T et R - 14-06-2024 14.31.csv"
)
lg_onde_ZnS_B, T_ZnS_B, R_ZnS_B = convertir_csv_en_liste(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 ZnS - B - T et R 14-06-2024 15.18.csv"
)
lg_onde_YF3_A, liste_T_YF3_A, liste_R_YF3_A = convertir_csv_en_liste(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 YF3-A-14-06-2024 16.11.csv"
)
lg_onde_YF3_B, liste_T_YF3_B, liste_R_YF3_B = convertir_csv_en_liste(
    "/Users/lisa/Desktop/Stage_L2/fichier_csv/B270 YF3 - B - T et R - 14-06-2024 16.33.csv"
)

# Transformé les liste en pourcent en 0.000

T_nu_A = convertir_pourcent(T_nu_A)
T_nu_B = convertir_pourcent(T_nu_B)
T_ZnS_A = convertir_pourcent(T_ZnS_A)
T_ZnS_B = convertir_pourcent(T_ZnS_B)
liste_T_YF3_A = convertir_pourcent(liste_T_YF3_A)
liste_T_YF3_B = convertir_pourcent(liste_T_YF3_B)

R_nu_A = convertir_pourcent(R_nu_A)
R_nu_B = convertir_pourcent(R_nu_B)
R_ZnS_A = convertir_pourcent(R_ZnS_A)
R_ZnS_B = convertir_pourcent(R_ZnS_B)
liste_R_YF3_A = convertir_pourcent(liste_R_YF3_A)
liste_R_YF3_B = convertir_pourcent(liste_R_YF3_B)

# enleve où c'est absorbant

red_lg_onde_nu_A, red_T_nu_A, red_R_nu_A = enleve_longueur_onde_absorbant(
    lg_onde_nu_A, T_nu_A, R_nu_A
)
red_lg_onde_nu_B, red_T_nu_B, red_R_nu_B = enleve_longueur_onde_absorbant(
    lg_onde_nu_B, T_nu_B, R_nu_B
)
red_lg_onde_ZnS_A, red_T_ZnS_A, red_R_ZnS_A = enleve_longueur_onde_absorbant(
    lg_onde_ZnS_A, T_ZnS_A, R_ZnS_A
)
red_lg_onde_ZnS_B, red_T_ZnS_B, red_R_ZnS_B = enleve_longueur_onde_absorbant(
    lg_onde_ZnS_B, T_ZnS_B, R_ZnS_B
)
red_lg_onde_YF3_A, red_T_YF3_A, red_R_YF3_A = enleve_longueur_onde_absorbant(
    lg_onde_YF3_A, liste_T_YF3_A, liste_R_YF3_A
)
red_lg_onde_YF3_B, red_T_YF3_B, red_R_YF3_B = enleve_longueur_onde_absorbant(
    lg_onde_YF3_B, liste_T_YF3_A, liste_R_YF3_B
)

# précision sur YF3

red_lg_onde_YF3_A, red_R_YF3_A, red_T_YF3_A = enlever_au_dela_1500(
    red_lg_onde_YF3_A, red_R_YF3_A, red_T_YF3_A
)
red_lg_onde_YF3_B, red_R_YF3_B, red_T_YF3_B = enlever_au_dela_1500(
    red_lg_onde_YF3_B, red_R_YF3_B, red_T_YF3_B
)
