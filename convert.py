import csv
import pandas as pd
import os


# à faire avant : avoir un unique feuillet pour chaque excel
# et attention les colonnes doivent etre dans le meme ordre pour chaque fichier


def convertir_xls_en_csv(fichier_xls, fichier_csv):
    if fichier_xls.endswith(".xls"):
        df = pd.read_excel(fichier_xls, engine="xlrd")
    elif fichier_xls.endswith(".xlsx"):
        df = pd.read_excel(fichier_xls, engine="openpyxl")
    else:
        raise ValueError(f"Unsupported file extension for {fichier_xls}")
    df.to_csv(fichier_csv, index=False, sep=";")


def convert_dossier_xls_en_csv(chemin_dossier, chemin_new_dossier):
    for filename in os.listdir(chemin_dossier):
        if filename.endswith(".xls") or filename.endswith(".xlsx"):
            chemin_fichier_xls = os.path.join(chemin_dossier, filename)
            chemin_fichier_csv = os.path.join(
                chemin_new_dossier,
                filename.replace(".xls", ".csv").replace(".xlsx", ".csv"),
            )
            convertir_xls_en_csv(chemin_fichier_xls, chemin_fichier_csv)


def convertir_csv_en_txt(chemin_fichier_csv, chemin_fichier_txt):
    with open(chemin_fichier_csv, mode="r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        with open(
            chemin_fichier_txt, mode="w", newline="", encoding="utf-8"
        ) as txt_file:
            for row in csv_reader:
                txt_file.write("\t".join(row) + "\n")


def convert_dossier_csv_en_txt(chemin_dossier):
    for filename in os.listdir(chemin_dossier):
        if filename.endswith(".csv"):
            chemin_fichier_csv = os.path.join(chemin_dossier, filename)
            chemin_fichier_txt = os.path.join(
                chemin_dossier, filename.replace(".csv", ".txt")
            )
            convertir_csv_en_txt(chemin_fichier_csv, chemin_fichier_txt)


def supprimer_premiere_ligne_csv(fichier):
    with open(fichier, mode="r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        lignes = list(reader)
    if len(lignes) > 0:
        del lignes[0]
    with open(fichier, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lignes)


def convertir_csv_en_liste(chemin_fichier_csv):
    lg_onde = []
    T = []
    R = []

    with open(chemin_fichier_csv, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for col in reader:
            lg_onde.append(float(col[0]))  # 1ére colonne
            T.append(float(col[1]))  # 2eme colonne
            R.append(float(col[2]))  # 3eme colonne
    return (lg_onde, T, R)

def convertir_csv_en_liste_R_puis_T(chemin_fichier_csv):
    lg_onde = []
    T = []
    R = []

    with open(chemin_fichier_csv, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for col in reader:
            lg_onde.append(float(col[0]))  # 1ére colonne
            R.append(float(col[1]))  # 2eme colonne
            T.append(float(col[2]))  # 3eme colonne
    return (lg_onde, T, R)

def convertir_csv_en_liste_T(chemin_fichier_csv):
    lg_onde = []
    T = []

    with open(chemin_fichier_csv, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for col in reader:
            lg_onde.append(float(col[0]))  # 1ére colonne
            T.append(float(col[1]))  # 2eme colonne

    return (lg_onde, T)

# list to txt


def convertir_liste_en_txt(nom_liste_n, nom_liste_lg, chemin_fichier_txt, nom):
    nom_fichier = f"{nom}.txt"
    chemin = os.path.join(chemin_fichier_txt, nom_fichier)
    with open(chemin, "w") as fichier:
        for i in range(len(nom_liste_n)):
            fichier.write(str(nom_liste_lg[i]) + "    " + str(nom_liste_n[i]) + "\n")


def convertir_liste_en_txt_4_colonnes(
    nom_liste_n, nom_liste_lg, nom_RetT_theo, nom_RetT_exp, chemin_fichier_txt, nom
):
    nom_fichier = f"{nom}.txt"
    chemin = os.path.join(chemin_fichier_txt, nom_fichier)
    with open(chemin, "w") as fichier:
        for i in range(len(nom_liste_n)):
            fichier.write(
                str(nom_liste_lg[i])
                + "    "
                + str(nom_RetT_theo[i])
                + "    "
                + str(nom_RetT_exp[i])
                + "    "
                + str(nom_liste_n[i])
                + "\n"
            )


def convertir_liste_en_txt_3_colonnes(
    nom_liste_lg, nom_R, nom_T, chemin_fichier_txt, nom
):
    nom_fichier = f"{nom}.txt"
    chemin = os.path.join(chemin_fichier_txt, nom_fichier)
    with open(chemin, "w") as fichier:
        for i in range(len(nom_liste_lg)):
            fichier.write(
                str(nom_liste_lg[i])
                + "    "
                + str(nom_R[i])
                + "    "
                + str(nom_T[i])
                + "\n"
            )
