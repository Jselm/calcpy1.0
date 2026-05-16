import tkinter

bouttons = [
    ["AC", "()", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ",", "←", "="],
]


#← = retour en arrière: supprime le dernier numéro du style si 12345 est écrit ça supprime juste le 5 

nb_lignes = len(bouttons) #5
nb_colonnes = len(bouttons[0]) #4

colonne_droite = ["÷", "×", "-", "+", "="] # opérateurs
ligne_du_haut = ["AC", "()", "%"] #"fonctions" 

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
composant=tkinter.Label(ecran, text="0", font=("Arial",45), background= charcoal_frost, foreground= cold_gray, anchor="e") #creer un composant dans l'ecran

composant.grid(row=0, column=0, columnspan=nb_colonnes, sticky="we")#we= west to east

for lignes in range(nb_lignes):
    for colonnes in range(nb_colonnes):
        val = bouttons[lignes][colonnes]
        boutton = tkinter.Button(ecran,overrelief="sunken" , background=charcoal_frost,foreground=cold_gray, text=val, font=("Arial", 30),
                                 width=nb_colonnes-1, height=1,
                                  command=lambda valeur=val: boutton_clique(val))
        boutton.grid(row=lignes+1, column=colonnes)
        



def boutton_clique(val):
    pass
ecran.pack()

cadre.mainloop() 