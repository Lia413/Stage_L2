import matplotlib.pyplot as plt
from main_modif import *


def plot_R_comparaison(lg_onde, smooth_R, R,min,max,min_lg,max_lg,  legend_smoothR, legend_R, Titre):
    plt.plot(lg_onde, smooth_R, label=legend_smoothR)
    # plt.plot(lg_onde, R, label=legend_R)
    plt.scatter(
        max_lg,
        max,
        color="orange",
        label="maximum R",
    )
    plt.scatter(
        min_lg,
        min,
        color="blue",
        label="minimum R",
    )
    plt.title(Titre)
    plt.xlabel("lg_onde")
    plt.ylabel("R")
    plt.legend()
    plt.show()


smooth_liste_T_A_ZnS_wout = calcule_T_wout_liste(smooth_liste_T_A_ZnS, liste_tous_ns)
smooth_liste_R_A_ZnS_wout = R(smooth_liste_T_A_ZnS_wout)
smooth_liste_T_B_ZnS_wout = calcule_T_wout_liste(smooth_liste_T_B_ZnS, liste_tous_ns)
smooth_liste_R_B_ZnS_wout = R(smooth_liste_T_B_ZnS_wout)
smooth_liste_T_A_YF3_wout = calcule_T_wout_liste(smooth_liste_T_A_YF3, liste_tous_ns)
smooth_liste_R_A_YF3_wout = R(smooth_liste_T_A_YF3_wout)
smooth_liste_T_B_YF3_wout = calcule_T_wout_liste(smooth_liste_T_B_YF3, liste_tous_ns)
smooth_liste_R_B_YF3_wout = R(smooth_liste_T_B_YF3_wout)

# convertir_liste_en_txt(
#     liste_T_ZnS_A, red_liste_lg_onde_A_ZnS, chemin, "T ZnSA matrice wout"
# )
# convertir_liste_en_txt(
#     liste_T_ZnS_B, red_liste_lg_onde_B_ZnS, chemin, "T ZnSB matrice wout"
# )
# convertir_liste_en_txt(
#     liste_R_ZnS_A, red_liste_lg_onde_A_ZnS, chemin, "R ZnSA matrice wout"
# )
# convertir_liste_en_txt(
#     liste_R_ZnS_B, red_liste_lg_onde_B_ZnS, chemin, "R ZnSB matrice wout"
# )
# convertir_liste_en_txt(
#     liste_T_YF3_A, red_liste_lg_onde_A_YF3, chemin, "T YF3A matrice wout"
# )
# convertir_liste_en_txt(
#     liste_T_YF3_B, red_liste_lg_onde_B_YF3, chemin, "T YF3B matrice wout"
# )
# convertir_liste_en_txt(
#     liste_R_YF3_A, red_liste_lg_onde_A_YF3, chemin, "R YF3A matrice wout"
# )
# convertir_liste_en_txt(
#     liste_R_YF3_B, red_liste_lg_onde_B_YF3, chemin, "R YF3B matrice wout"
# )

min_R_A_ZnS = trouver_extremums(smooth_liste_R_A_ZnS_wout, red_liste_lg_onde_A_ZnS)["minimum smooth"]
min_R_B_ZnS = trouver_extremums(smooth_liste_R_B_ZnS_wout, red_liste_lg_onde_B_ZnS)["minimum smooth"]
max_R_A_ZnS= trouver_extremums(smooth_liste_R_A_ZnS_wout, red_liste_lg_onde_A_ZnS)["maximum smooth"]
max_R_B_ZnS = trouver_extremums(smooth_liste_R_B_ZnS_wout, red_liste_lg_onde_B_ZnS)["maximum smooth"]
min_lg_A_ZnS = trouver_extremums(smooth_liste_R_A_ZnS_wout, red_liste_lg_onde_A_ZnS)["minimum lg"]
min_lg_B_ZnS = trouver_extremums(smooth_liste_R_B_ZnS_wout, red_liste_lg_onde_B_ZnS)["minimum lg"]
max_lg_A_ZnS= trouver_extremums(smooth_liste_R_A_ZnS_wout, red_liste_lg_onde_A_ZnS)["maximum lg"]
max_lg_B_ZnS = trouver_extremums(smooth_liste_R_B_ZnS_wout, red_liste_lg_onde_B_ZnS)["maximum lg"]

min_R_A_YF3 = trouver_extremums(smooth_liste_R_A_YF3_wout, red_liste_lg_onde_A_YF3)["minimum smooth"]
min_R_B_YF3 = trouver_extremums(smooth_liste_R_B_YF3_wout, red_liste_lg_onde_B_YF3)["minimum smooth"]
max_R_A_YF3= trouver_extremums(smooth_liste_R_A_YF3_wout, red_liste_lg_onde_A_YF3)["maximum smooth"]
max_R_B_YF3 = trouver_extremums(smooth_liste_R_B_YF3_wout, red_liste_lg_onde_B_YF3)["maximum smooth"]
min_lg_A_YF3 = trouver_extremums(smooth_liste_R_A_YF3_wout, red_liste_lg_onde_A_YF3)["minimum lg"]
min_lg_B_YF3 = trouver_extremums(smooth_liste_R_B_YF3_wout, red_liste_lg_onde_B_YF3)["minimum lg"]
max_lg_A_YF3= trouver_extremums(smooth_liste_R_A_YF3_wout, red_liste_lg_onde_A_YF3)["maximum lg"]
max_lg_B_YF3 = trouver_extremums(smooth_liste_R_B_YF3_wout, red_liste_lg_onde_B_YF3)["maximum lg"]

plot_R_comparaison(
    red_liste_lg_onde_A_ZnS,
    smooth_liste_R_A_ZnS_wout,
    liste_R_ZnS_A,
    min_R_A_ZnS,
    max_R_A_ZnS,
    min_lg_A_ZnS,
    max_lg_A_ZnS,
    "ZnSA lissé mesuré",
    "ZnSA matrice",
    "La Réflexion en fonction de la longueur d'onde pour ZnSA",
)

plot_R_comparaison(
    red_liste_lg_onde_B_ZnS,
    smooth_liste_R_B_ZnS_wout,
    liste_R_ZnS_B,
    min_R_B_ZnS,
    max_R_B_ZnS,
    min_lg_B_ZnS,
    max_lg_B_ZnS,
    "ZnSB lissé mesuré",
    "ZnSB matrice",
    "La Réflexion en fonction de la longueur d'onde pour ZnSB ",
)

plot_R_comparaison(
    red_liste_lg_onde_A_YF3,
    smooth_liste_R_A_YF3_wout,
    liste_R_YF3_A,
    min_R_A_YF3,
    max_R_A_YF3,
    min_lg_A_YF3,
    max_lg_A_YF3,
    "YF3A lissé mesuré",
    "YF3A matrice",
    "La Réflexion en fonction de la longueur d'onde pour YF3A",
)
plot_R_comparaison(
    red_liste_lg_onde_B_YF3,
    smooth_liste_R_B_YF3_wout,
    liste_R_YF3_B,
    min_R_B_YF3,
    max_R_B_YF3,
    min_lg_B_YF3,
    max_lg_B_YF3,
    "YF3B lissé mesuré",
    "YF3B matrice",
    "La Réflexion en fonction de la longueur d'onde pour YF3B ",
)
