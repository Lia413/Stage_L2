from main_modif import *

def wrong_coeff(coeff1,coeff2,liste):
    new_liste=[]
    for elmt in liste:
        if len(liste)%2==0:
            new_liste.append(coeff1*elmt)
        else :
            new_liste.append(coeff2*elmt)
    return new_liste


convertir_liste_en_txt_3_colonnes(liste_lg_onde_UHC_A,liste_T_UHC_A,wrong_coeff(1,1/1.03,liste_T_UHC_A),chemin,'Tuhc,Tuhc coeff')
# liste_T_UHC_A=wrong_coeff(1,1/1.03,liste_T_UHC_A)




liste_d_theo=[39.239,208.307,30.798,53.101,51.195,85.258,51.134,177.103,47.807,74.978,44.222,78.643,
              48.21,169.973,47.69,121.141,35.212,73.523,37.601,167.95,82.337,33.651,56.158,403.196]

liste_d_theo_ZnS=[39.239,30.798,51.195,51.134,47.807,44.222,
              48.21,47.69,35.212,37.601,82.337,56.158]

liste_d_theo_YF3=[208.307,53.101,85.258,177.103,74.978,78.643,
              169.973,121.141,73.523,167.95,33.651,403.196]
# liste_d_theo=[1000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


liste_lg_nu_ZnS=garder_meme_val(red_lg_onde_nu_ZnS,red_liste_lg_onde_A_ZnS)
liste_lg_nu_YF3=garder_meme_val(red_lg_onde_nu_YF3,red_liste_lg_onde_A_YF3)
liste_lg=garder_meme_val(liste_lg_nu_ZnS,liste_lg_nu_YF3)



def garder_visible(liste_lg):
    liste_new_lg=[]
    for lg in liste_lg:
        if 400<=lg<=800:
            liste_new_lg.append(lg)
    return liste_new_lg

liste_lg=garder_visible(liste_lg)



liste_n_ZnSA=enlever_R_abs(liste_n_T_et_R_A_ZnS,liste_lg,red_liste_lg_onde_A_ZnS)[1]
liste_n_YF3A=enlever_R_abs(liste_n_T_et_R_A_YF3,liste_lg,red_liste_lg_onde_A_YF3)[1]
liste_n_nu=enlever_R_abs(liste_tous_ns,liste_lg,red_liste_lg_onde_A_ZnS)[1]



# print('len(liste_tous_n_A_ZnS)',len(liste_n_ZnSA))
# print('len(liste_tous_n_A_YF3)',len(liste_n_YF3A))
# print('len(red_liste_lg_onde_A_ZnS)',len(liste_lg))
# print(len(liste_n_nu))

liste_Y_multicouhes=calcule_matrice_liste_multicouches(liste_n_nu,liste_n_ZnSA,liste_n_YF3A,liste_d_theo_ZnS,liste_d_theo_YF3,phi,liste_lg,'HLHLHLHLHLHLHLHLHLHLHLHL',liste_indice)
# print('liste_Y_multicouhes',liste_Y_multicouhes)

def garder_reels(liste_Y_multicouhes):
    liste_y_reels=[]
    for elmt in liste_Y_multicouhes:
        liste_y_reels.append(np.real(elmt))
    return liste_y_reels

liste_Y_multicouhes=garder_reels(liste_Y_multicouhes)
liste_R_multicouhes = calcule_R_matrice(liste_Y_multicouhes)
liste_T_multicouhes = calcule_T(liste_R_multicouhes)
# liste_R_multicouhes=convertir_fois_100(liste_R_multicouhes)
# liste_T_multicouhes=convertir_fois_100(liste_T_multicouhes)

# print('liste_R_multicouhes',liste_R_multicouhes)
# print('liste_T_multicouhes',liste_T_multicouhes)


liste_lg_onde_same=garder_meme_val(liste_lg,arrondir(liste_lg_onde_UHC_A))
# print('lg_onde_same',liste_lg_onde_same)

liste_T_UHC_A=enlever_R_abs(liste_T_UHC_A,liste_lg_onde_same,arrondir(liste_lg_onde_UHC_A))[1]
liste_R_UHC_A=enlever_R_abs(liste_R_UHC_A,liste_lg_onde_same,arrondir(liste_lg_onde_UHC_A))[1]
liste_T_multicouhes=enlever_R_abs(liste_T_multicouhes,liste_lg_onde_same, liste_lg)[1]
liste_R_multicouhes=enlever_R_abs(liste_R_multicouhes,liste_lg_onde_same, liste_lg)[1]

liste_n_ZnSA=enlever_R_abs(liste_n_T_et_R_A_ZnS,liste_lg_onde_same,liste_lg)[1]
liste_n_YF3A=enlever_R_abs(liste_n_T_et_R_A_YF3,liste_lg_onde_same,liste_lg)[1]
liste_n_nu=enlever_R_abs(liste_tous_ns,liste_lg_onde_same,liste_lg)[1]

print('len(liste_lg_onde_same)',len(liste_lg_onde_same))
print('len(liste_R_UHC_A)',len(liste_R_UHC_A))
print('len(liste_T_UHC_A)',len(liste_T_UHC_A))

print('len liste_R_multicouhes',len(liste_R_multicouhes))
print('len liste_T_multicouhes',len(liste_T_multicouhes))




import matplotlib.pyplot as plt

plt.plot(liste_lg_onde_same,liste_T_multicouhes,label='T multicouhes')
plt.plot(liste_lg_onde_same,liste_T_UHC_A,label='T uhcA')
plt.plot(liste_lg_onde_same,liste_R_multicouhes,label='R multicouhes')
plt.plot(liste_lg_onde_same,liste_R_UHC_A,label='R uhcA')
plt.xlabel('lg onde')
plt.ylabel('T')
plt.legend()
plt.show()

# plt.plot(liste_lg_onde_same,liste_n_ZnSA,label='ZnSA')
# plt.plot(liste_lg_onde_same,liste_n_YF3A,label='YF3A')
# plt.legend()
# plt.show()

# plt.plot(liste_lg_onde_same,liste_Y_multicouhes)
# plt.show()




convertir_liste_en_txt(liste_n_ZnSA,liste_lg_onde_same,chemin,'indice n same ZnSA')
convertir_liste_en_txt(liste_n_YF3A,liste_lg_onde_same,chemin,'indice n same YF3A')
convertir_liste_en_txt_3_colonnes(liste_lg_onde_same,liste_T_multicouhes,liste_T_UHC_A,chemin,'T poly et uhc comp ')
convertir_liste_en_txt(liste_T_UHC_A,liste_lg_onde_same,chemin,'UHC A-T coeff yf3 ')


#Tracer l'AR en réflexion sans backside

convert_dossier_xls_en_csv(chemin_dossier, chemin_new_dossier)
chemin_AR='/Users/lisa/Desktop/Stage_L2/fichier_csv/Anti reflet 2 03-07.csv'
supprimer_premiere_ligne_csv(chemin_AR)

liste_lg_onde_AR, liste_T_AR, liste_R_AR = convertir_csv_en_liste(chemin_AR)# trois colonnes
liste_T_AR=convertir_pourcent(liste_T_AR)
liste_R_AR=convertir_pourcent(liste_R_AR)


def garder_visible(liste_lg_onde_AR, liste_R_AR):
    liste_lg=[]
    liste_R=[]
    for i in range(len(liste_lg_onde_AR)):
        if 400<=liste_lg_onde_AR[i]<=800:
            liste_lg.append(liste_lg_onde_AR[i])
            liste_R.append(liste_R_AR[i])
    return liste_lg,liste_R

liste_lg_onde_AR,liste_T_AR=garder_visible(liste_lg_onde_AR, liste_T_AR)
liste_lg_new=garder_meme_val(liste_lg,liste_lg_onde_AR)

def garder_same(liste_lg_new,liste_lg,liste_lg_onde_AR,liste_T_AR,liste_n_nu):
    liste_n_new=[]
    liste_T_new=[]
    for i in range(len(liste_lg)):
        for x in liste_lg_new:
            if x == liste_lg[i]:
                liste_n_new.append(liste_n_nu[i])

    for j in range(len(liste_lg_onde_AR)):
        for x in liste_lg_new:
            if x == liste_lg_onde_AR[j]:
                liste_T_new.append(liste_T_AR[j])
    return liste_n_new,liste_T_new


liste_n_new,liste_T_new=garder_same(liste_lg_new,liste_lg,liste_lg_onde_AR,liste_T_AR,liste_n_nu)


liste_T_AR_wout=calcule_T_wout_liste(liste_T_new,liste_n_new)
liste_R_AR_wout=calcule_R_matrice(liste_T_AR_wout)

plt.plot(liste_lg_new,liste_R_AR_wout,label='Réflexion')
plt.xlabel('longueur d\'onde')
plt.ylabel('Réflexion')
plt.title('AR sur B270 mesuré en réflexion')
plt.legend()
plt.show()



