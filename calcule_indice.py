import numpy as np


def calcule_n_ex(listeTwithB):
    liste_nex = []
    for t in listeTwithB:
        liste_nex.append((1 + np.sqrt(1 - t**2)) / t)
    return liste_nex


def calcule_T_wout(listeTwithB, ns):
    liste_Twout = []
    for i in range(len(listeTwithB)):
        u = 1 + 1 / listeTwithB[i] - (ns + 1) ** 2 / (4 * ns)
        liste_Twout.append(1 / u)
    return liste_Twout


def calcule_T_wout_liste(listeTwithB, liste_ns):
    liste_Twout = []
    for i in range(len(listeTwithB)):
        u = 1 + 1 / listeTwithB[i] - (liste_ns[i] + 1) ** 2 / (4 * liste_ns[i])
        liste_Twout.append(1 / u)
    return liste_Twout


def calcule_R_wout(listeTwithB, liste_ns_reg):
    liste_Rwout = []
    for i in range(len(listeTwithB)):
        u = 1 + 1 / listeTwithB[i] - (liste_ns_reg[i] + 1) ** 2 / (4 * liste_ns_reg[i])
        liste_Rwout.append(1 - 1 / u)
    return liste_Rwout


def R(listeTwout):  # si on a déja T Wout ça sert à rien de tout recalculer
    liste_R = []
    for x in listeTwout:
        liste_R.append(1 - x)
    return liste_R


def T_with(liste_Rwith):
    liste_T = []
    for x in liste_Rwith:
        liste_T.append(1 - x)
    return liste_T


def trouve_indice(R_hight, ns):
    u = (-np.sqrt(R_hight) - 1) * ns / (np.sqrt(R_hight) - 1)
    return np.sqrt(u)


def calcule_d(p, lamb, n_lamb):
    return ((2 * p + 1) * lamb) / (4 * n_lamb)


def calcule_d_qwot(qwot, lamb, n_lamb):
    return ((qwot) * lamb) / (4 * n_lamb)


# print(calcule_d_qwot(10.76,500,2.45))#B
# print(calcule_d_qwot(10.61,500,2.45))#A


def trouve_indice_liste(liste_R_hight, liste_ns_reg):
    liste_n = []
    for i in range(len(liste_R_hight)):
        u = (
            (1 + np.sqrt(liste_R_hight[i]))
            * liste_ns_reg[i]
            / (1 - np.sqrt(liste_R_hight[i]))
        )
        liste_n.append(np.sqrt(u))
    return liste_n


def trouve_indice_by_T(liste_T_min, liste_ns):
    liste_n = []
    for i in range(len(liste_T_min)):
        liste_n.append(
            ((np.sqrt(liste_T_min[i] + 1) + 1) * liste_ns[i])
            / (1 - np.sqrt(liste_T_min[i] + 1))
        )
    return liste_n


def n_substrat(liste_Rmin):
    liste_ns = []
    for i in range(len(liste_Rmin)):
        liste_ns.append(-(np.sqrt(liste_Rmin[i]) + 1) / (np.sqrt(liste_Rmin[i]) - 1))
    return liste_ns


def trouver_ns_reg(a, b, c, liste_val_lambda):
    liste_ns_reg = []
    for val in liste_val_lambda:
        liste_ns_reg.append(a * val**2 + b * val + c)
    return liste_ns_reg


def trouver_R_reg(a, b, c, d, e, f, liste_val_lambda):
    liste_R_reg = []
    for val in liste_val_lambda:
        liste_R_reg.append(
            a * val**5 + b * val**4 + c * val**3 + d * val**2 + e * val + f
        )
    return liste_R_reg


def trouver_n_reg(a, b, c, val_lambda):
    return a * val_lambda**2 + b * val_lambda + c


def trouver_tous_les_n(a, b, c, liste_x):
    liste_n = []
    for x in liste_x:
        liste_n.append(a * x**2 + b * x + c)
    return liste_n


def trouver_tous_les_n_1(a, b, liste_x):
    liste_n = []
    for x in liste_x:
        liste_n.append(a * x + b)
    return liste_n


def erreur_quadratique_n(a_s, b_s, c_s, liste1_sur_lamb_carre, a, b, c):
    liste_erreur = []
    for elmt in liste1_sur_lamb_carre:
        u_theo = a_s * elmt**2 + b_s * elmt + c_s
        u_exp = a * elmt**2 + b * elmt + c
        liste_erreur.append((u_theo - u_exp) ** 2)
    return liste_erreur


def erreur_quadratique_liste_n(
    liste_tous_les_ns_exp, liste1surlamb, liste_tous_les_n_theo
):
    liste_erreur = []
    for i in range(len(liste1surlamb)):
        liste_erreur.append(
            1
            / len(liste_tous_les_n_theo)
            * (liste_tous_les_n_theo[i] - liste_tous_les_ns_exp[i]) ** 2
        )
    return liste_erreur


def erreur_quadratique_liste(liste_tous_les_exp, liste1surlamb, liste_tous_les_theo):
    liste_erreur = []
    sum = 0
    for i in range(len(liste1surlamb)):
        liste_erreur.append(
            1
            / len(liste_tous_les_theo)
            * (liste_tous_les_theo[i] - liste_tous_les_exp[i]) ** 2
        )
    for elmt in liste_erreur:
        sum += elmt
    return sum


def calcule_indice_ZnS_YF3(red_lg_onde_max, lg_onde, liste_n_ex):
    liste_n_ex_max = []
    for i in range(len(lg_onde)):
        for elmt in red_lg_onde_max:
            if lg_onde[i] == elmt:
                liste_n_ex_max.append(liste_n_ex[i])
    return liste_n_ex_max


def choisir_ns(liste_div_lg_min, liste_div_lg_nu, liste_tous_ns):
    liste_ns = []
    for i in range(len(liste_div_lg_nu)):
        for elmt in liste_div_lg_min:
            if elmt == liste_div_lg_nu[i]:
                liste_ns.append(liste_tous_ns[i])
    return liste_ns


def combine_n(liste_n_par_R, liste_n_par_T):
    liste_combine = []
    for i in range(len(liste_n_par_R)):
        liste_combine.append((liste_n_par_R[i] + liste_n_par_T[i]) / 2)
    return liste_combine
