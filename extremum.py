from scipy import signal


def smooth_liste(liste, W=51):
    return signal.savgol_filter(liste, window_length=W, polyorder=2, mode="nearest")# ce mode car il regle les problèmes qu'ont les point à l'extremité de la fenêtre: cad pas de voisin


def trouver_extremums(liste_smooth, liste_lg_onde):
    df = signal.savgol_filter(
        liste_smooth, window_length=31, polyorder=2, deriv=1, mode="nearest" 
    )
    ddf = signal.savgol_filter(
        liste_smooth, window_length=31, polyorder=2, deriv=2, mode="nearest"
    )

    extremums = {
        "minimum lg": [],
        "minimum smooth": [],
        "maximum lg": [],
        "maximum smooth": [],
    }
    for i in range(1, len(df) - 1):
        if df[i] * df[i - 1] < 0:  # si la dérivée change de signe
            if ddf[i] > 0:
                extremums["minimum lg"].append(
                    (liste_lg_onde[i - 1] + liste_lg_onde[i]) / 2
                )
                extremums["minimum smooth"].append(
                    (liste_smooth[i - 1] + liste_smooth[i]) / 2
                )

            elif ddf[i] < 0:
                extremums["maximum lg"].append(
                    (liste_lg_onde[i - 1] + liste_lg_onde[i]) / 2
                )
                extremums["maximum smooth"].append(
                    (liste_smooth[i - 1] + liste_smooth[i]) / 2
                )

    return extremums
