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

ecran =tkinter.Frame(cadre) #creer l'ecran dans le cadre
composant=tkinter.Label(ecran, text="0", font=("Arial",45),width=nb_colonnes, background= "black", foreground= "white", anchor="e") #composant du haut dans l'ecran

composant.grid(row=0, column=0, columnspan=nb_colonnes, sticky="we")#we= west to east

for lignes in range(nb_lignes):
    for colonnes in range(nb_colonnes):
        val = bouttons[lignes][colonnes]
        boutton = tkinter.Button(ecran,overrelief="sunken" , text=val, font=("Arial", 30),
                                 width=nb_colonnes-1, height=1,
                                  command=lambda valeur=val: boutton_clique(valeur))
        if val in ligne_du_haut:
            boutton.config(foreground="black", background=cold_gray)
        elif val in colonne_droite:
            boutton.config(foreground="white", background="orange")
        else:
            boutton.config(foreground="white", background=flint)
        
        boutton.grid(row=lignes+1, column=colonnes)
        

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
                    B = composant["text"].split()[-1] #récupère le dernier nombre affiché après l'opérateur
                    numeroA = float(A) 
                    numeroB = float(B)
                    if operateur == "+":
                        composant["text"] = retirer_decimale_zero(numeroA + numeroB)
                    elif operateur == "-":
                        composant["text"] = retirer_decimale_zero(numeroA - numeroB)
                    elif operateur == "×":
                        composant["text"] = retirer_decimale_zero(numeroA * numeroB)
                    elif operateur == "÷":
                        composant["text"] = retirer_decimale_zero(numeroA / numeroB)
                    A = "0"
                    B= "None"
                    operateur = None
            elif valeur in "+-×÷":
                if operateur is None: #si ya deja 500 + et qu'on veut faire * ça remplace le + et pas le 500
                    A = composant["text"]
                    B = "0"
                operateur = valeur
                composant["text"] = f"{A} {operateur} "

    elif valeur in ligne_du_haut: #AC, +/-, %
        if valeur == "AC":
            A = "0"
            B= "None"
            operateur = None
            composant["text"] = "0"
        elif valeur == "+/-":
            resultat = float(composant["text"]) * -1
            composant["text"] = retirer_decimale_zero(resultat)
        elif valeur == "%":
            resultat = float(composant["text"]) / 100
            composant["text"] = retirer_decimale_zero(resultat)
    else: #nombres ou décimale ou retour
        if valeur == "←":
            if composant["text"] != "0" and len(composant["text"]) > 1:
                composant["text"] = composant["text"][:-1]
            else:
                composant["text"] = "0"
        elif valeur == ",":
            if valeur not in composant["text"]: #verif double virgule
                composant["text"] += valeur 
        elif valeur in "0123456789":
            if composant["text"] == "0":
                composant["text"] = valeur #remplace le 0 par le nombre cliqué, ex: si ya déjà 0 et qu'on appuie sur 5 ça affiche 5 et pas 05
            else:
                composant["text"] += valeur #ajoute le nombre cliqué à la suite de ce qui est déjà affiché

#centrer l'ecran
cadre.update()

largeur=cadre.winfo_width()
hauteur=cadre.winfo_height()

x=(cadre.winfo_screenwidth()//2) - (largeur//2)
y=(cadre.winfo_screenheight()//2) - (hauteur//2)
cadre.geometry(f"{largeur}x{hauteur}+{x}+{y}")
cadre.mainloop() 