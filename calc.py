import tkinter

bouttons = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ",", "←", "="],
]


#← = retour en arrière: supprime le dernier numéro du style si 12345 est écrit ça supprime juste le 5 

nb_lignes = len(bouttons) #5
nb_colonnes = len(bouttons[0]) #4

colonne_droite = ["÷", "×", "-", "+", "="] # opérateurs
ligne_du_haut = ["AC", "+/-", "%"] #"fonctions" 

#couleurs
flint = "#5F6368"
cold_gray= "#80868B"
charcoal_frost = "#3C4043"
alexandra ="#4285F4"


#ecran

cadre = tkinter.Tk() #creer le cadre
cadre.title("Calculatrice") #titre du cadre
cadre.resizable(False, False) #faire en sorte qu'on puisse pas resize

ecran = tkinter.Frame(cadre)

barre_menu = tkinter.Frame(ecran, background=charcoal_frost)
barre_menu.grid(row=0, column=0, columnspan=nb_colonnes, sticky="we")

menu = tkinter.Menubutton(barre_menu, relief="flat", text="≡", font=("Arial", 20), background=charcoal_frost, foreground="white")
menu.pack(side="left", ipadx=10, ipady=5)

nom_theme = tkinter.Label(barre_menu, text="theme ...", font=("Arial", 12), background=charcoal_frost, foreground="white")
nom_theme.pack(side="left", padx=5)


grille_boutons = tkinter.Label(ecran, text="0", font=("Arial",45), width=nb_colonnes, background="black", foreground="white", anchor="e")
grille_boutons.grid(row=1, column=0, columnspan=nb_colonnes, sticky="we")







for lignes in range(nb_lignes):
    for colonnes in range(nb_colonnes):
        val = bouttons[lignes][colonnes]
        boutton = tkinter.Button(ecran,relief="solid",overrelief="sunken" , text=val, font=("Arial", 30),
                                 width=nb_colonnes-1, height=1,
                                  command=lambda valeur=val: boutton_clique(valeur))
        if val in ligne_du_haut:
            boutton.config(foreground="black", background=cold_gray)
        elif val in colonne_droite:
            boutton.config(foreground="white", background="orange")
        else:
            boutton.config(foreground="white", background=flint)
        
        boutton.grid(row=lignes+2, column=colonnes)
        

ecran.pack()

#opérations
A="0"
operateur= None
B= None

def retirer_decimale_zero(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)


def boutton_clique(valeur):
    global colonne_droite, ligne_du_haut, A, B, operateur #declarer les variables globales pour pouvoir les modifier dans la fonction
    if valeur in colonne_droite: #÷, ×, -, +, =
            if valeur == "=":
                if A is not None and operateur is not None:
                    B = grille_boutons["text"].split()[-1] #récupère le dernier nombre affiché après l'opérateur
                    numeroA = float(A) 
                    numeroB = float(B)
                    if operateur == "+":
                        grille_boutons["text"] = retirer_decimale_zero(numeroA + numeroB)
                    elif operateur == "-":
                        grille_boutons["text"] = retirer_decimale_zero(numeroA - numeroB)
                    elif operateur == "×":
                        grille_boutons["text"] = retirer_decimale_zero(numeroA * numeroB)
                    elif operateur == "÷":
                        grille_boutons["text"] = retirer_decimale_zero(numeroA / numeroB)
                    A = "0"
                    B= "None"
                    operateur = None
            elif valeur in "+-×÷":
                if operateur is None: #si ya deja 500 + et qu'on veut faire * ça remplace le + et pas le 500
                    A = grille_boutons["text"]
                    B = "0"
                operateur = valeur
                grille_boutons["text"] = f"{A} {operateur} "

    elif valeur in ligne_du_haut: #AC, +/-, %
        if valeur == "AC":
            A = "0"
            B= "None"
            operateur = None
            grille_boutons["text"] = "0"
        elif valeur == "+/-":
            resultat = float(grille_boutons["text"]) * -1
            grille_boutons["text"] = retirer_decimale_zero(resultat)
        elif valeur == "%":
            if operateur is None:
                resultat = float(grille_boutons["text"]) / 100
                grille_boutons["text"] = retirer_decimale_zero(resultat)
            else:
                grille_boutons["text"] = "Error"
    else: #nombres ou décimale ou retour
        if valeur == "←":
            if grille_boutons["text"] != "0" and len(grille_boutons["text"]) > 1:
                grille_boutons["text"] = grille_boutons["text"][:-1]
            else:
                grille_boutons["text"] = "0"
        elif valeur == ",":
            if valeur not in grille_boutons["text"]: #verif double virgule
                grille_boutons["text"] += valeur 
        elif valeur in "0123456789":
            if grille_boutons["text"] == "0":
                grille_boutons["text"] = valeur #remplace le 0 par le nombre cliqué, ex: si ya déjà 0 et qu'on appuie sur 5 ça affiche 5 et pas 05
            else:
                grille_boutons["text"] += valeur #ajoute le nombre cliqué à la suite de ce qui est déjà affiché

#centrer l'ecran
cadre.update()

largeur=cadre.winfo_width()
hauteur=cadre.winfo_height()

x=(cadre.winfo_screenwidth()//2) - (largeur//2)
y=(cadre.winfo_screenheight()//2) - (hauteur//2)
cadre.geometry(f"{largeur}x{hauteur}+{x}+{y}")
cadre.mainloop() 
