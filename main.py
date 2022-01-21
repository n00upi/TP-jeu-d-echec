"""Ce fichier contient l'entièreté du projet de Jeu d'échec.

Dans la prochaine version, je séparerais les fichiers.
Le fichier principal contiendra le jeu, un second les fonctions
et un troisième les constantes.

Le jeu n'est pas terminé.

Version 2.1

"""


"""
===========================
Définitions des constantes
===========================
"""


black_pawn = ['tn', 'cn', 'fn', 'qn', 'kn', 'pn']
white_pawn = ['TB', 'CB', 'FB', 'QB', 'KB', 'PB']


"""
=================
Fonctions du jeu
=================
"""

def plateau_creation():
    """Function : plateau()
    Cette fonction permet de créer le plateau de jeu de dimensions (8 x 8), ainsi que son contenu.
    Les pions noirs sont inscrits en minuscule, les pions blancs en majuscule :
          - tn = Tour Noire           - TN = Tour Blanche
          - cn = Cavalier Noir        - CN = Cavalier Blanc
          - fn = Fou Noir             - FB = Fou Blanc
          - qn = Reine Noire          - QB = Reine Blanche
          - kn = Roi Noir             - KB = Roi Blanc
          - pn = Pion Noir            - PB = Pion Blanc
    Cette fonction est appelée une seule fois dans le programme.
    
    """
    
    plateau = [['tn','cn','fn','qn','kn','fn','cn','tn'],
               ['pn','pn','pn','pn','pn','pn','pn','pn'],
               ['  ','  ','  ','  ','  ','  ','  ','  '],
               ['  ','  ','  ','  ','  ','  ','  ','  '],
               ['  ','  ','  ','  ','  ','  ','  ','  '],
               ['  ','  ','  ','  ','  ','  ','  ','  '],
               ['PB','PB','PB','PB','PB','PB','PB','PB'],
               ['TB','CB','FB','KB','QB','FB','CB','TB'],
               ]
    return plateau
    """Return value:
          - plateau : list. Correspond à la liste crée dans la fonction.

    """



def affichage_plateau(plateau):
    """Function : affichage_plateau(plateau)
    
    Cette fonction permet d'afficher le plateau.
    
    Args : 
        - plateau : list. COntient le plateau de jeu.
        
        """
    
    for i in range(8):
        print(plateau[i])



def verif_placement(plateau, d_axe_x, d_axe_y,a_axe_x, a_axe_y, bool_player):
    """Function verif_emplacement(plateau, d_axe_x, d_axe_y,a_axe_x, a_axe_y, player_list)
    
    Cette fonction permet de vérifier si le déplacement d'un pion est possible
    selon les critères suivants :
    - Si le pion séléctionné est compris dans la taille du plateau (8x8),
    - si la case n'est pas vide,
    - si la case de départ contient le pion du joueur,
    - si la case de départ ne contient pas le pion de l'adverssaire.
    
    Args:
        plateau : list
        d_axe_x : int
        d_axe_y : int
        a_axe_x : int
        a_axe_y : int
        player_list : list
        
        
    """
    
    autorize:bool=False
    
    if ((d_axe_x < 9) and (d_axe_x > -1)) and ((d_axe_y < 9) and (d_axe_y > -1)) and ((a_axe_x < 9) and (a_axe_x > -1)) and ((a_axe_y < 9) and (a_axe_y > -1)):
         
        if bool_player == True:
            if (plateau[d_axe_x][d_axe_y] in white_pawn) or (plateau[a_axe_x][a_axe_y] in black_pawn):
                autorize = verif_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y, bool_player, autorize)
            else:
                autorize = False
                print("Déplacement impossible ! player1")
                 
        elif bool_player == False:
            if (plateau[d_axe_x][d_axe_y] in black_pawn) or (plateau[a_axe_x][a_axe_y] in white_pawn):
                autorize = verif_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y, bool_player, autorize)
            else:
                print("Déplacement impossible ! player2")
                autorize = False
                      
        else:
            return xy_input(bool_player)
         
    else:
        print("Déplacement impossible ! La valeur doit être comprise entre 1 et 8.")
        autorize = False
        
    return autorize               


def placement_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y):
    """Function placement_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y)
    
    Cette fonction permet de placer une pièce en :
    - la stockant dans une variable temporaire
    - la déplaçant à l'endroit voulu
    - supprimant son ancien emplacement.
    
        
    Args :
        plateau : list
        d_axe_x : int
        d_axe_y : int
        a_axe_x : int
        a_axe_y : int
        
        """
    
    
    pawn = plateau[d_axe_x][d_axe_y]
    plateau[a_axe_x][a_axe_y] = pawn
    plateau[d_axe_x][d_axe_y] = '  '
    return(plateau)


def verif_piece(plateau, d_axe_x, d_axe_y, a_axe_a, a_axe_y, bool_player, autorize):
    
    if autorize:
        
        if (plateau[d_axe_x][d_axe_y] == white_pawn[0]) or (plateau[d_axe_x][d_axe_y] == black_pawn[0]):
            print('Tour séléctionnée')
            tour()
        elif (plateau[d_axe_x][d_axe_y] == white_pawn[1]) or (plateau[d_axe_x][d_axe_y] == black_pawn[1]):
            print('Cavalier séléctionnée')
            cavalier()
        elif (plateau[d_axe_x][d_axe_y] == white_pawn[2]) or (plateau[d_axe_x][d_axe_y] == black_pawn[2]):
            print('Fou séléctionnée')
            fou()
        elif (plateau[d_axe_x][d_axe_y] == white_pawn[3]) or (plateau[d_axe_x][d_axe_y] == black_pawn[3]):
            print('Reine séléctionnée')
            reine()
        elif (plateau[d_axe_x][d_axe_y] == white_pawn[4]) or (plateau[d_axe_x][d_axe_y] == black_pawn[4]):
            print('Roi séléctionnée')
            roi()
        elif (plateau[d_axe_x][d_axe_y] == white_pawn[5]) or (plateau[d_axe_x][d_axe_y] == black_pawn[5]):
            print('Pion séléctionnée')
            autorize = pion(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y, bool_player, autorize)
            return autorize

    else:
        pass

def pion(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y, bool_player, autorize):
    if (plateau[d_axe_x][d_axe_y] == plateau[a_axe_x][a_axe_y == d_axe_y + 1]):
        print('deplace pion ok')
        autorize = True
        return autorize
    else:
        autorize = False
def tour():
    pass
def cavalier():
    pass
def fou():
    pass
def reine():
    pass
def roi():
    pass    

"""
===========================================
Fonctions interraction avec l'utilisateur.
===========================================
"""
 
def xy_input(bool_player):
    """Function : xy_input()
    Cette fonction permet de récupérer les coordonnées x et y de l'utilisateur.
    Elle vérifie également si les coordonnées entrées sont valides selon les critères suivants:
                  - Les valeurs doivent êtres comprises entre 1 et 
    """
    autorize = False
    
    
    while autorize == False:
        d_axe_x = type=int(input("Saisir l'axe 'x' de départ : "))
        d_axe_y = type=int(input("Saisir l'axe 'y' de départ : "))
        a_axe_x = type=int(input("Saisir l'axe 'x' d'arrivée : "))
        a_axe_y = type=int(input("Saisir l'axe 'y' d'arrivée: "))
        
        d_axe_x = d_axe_x - 1
        d_axe_y = d_axe_y - 1
        a_axe_x = a_axe_x - 1
        a_axe_y = a_axe_y - 1
        
        if bool_player:
            autorize = verif_placement(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y, True)
            
        else:
            autorize = verif_placement(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y, False)
            

    return(d_axe_x,d_axe_y, a_axe_x, a_axe_y)
    """Return :
    d_axe_x : int. La valeur de 'x' saisie par l'utilisateur.
    d_axe_y : int. La valeur de 'y' saisie par l'utilisateur.
    a_axe_x : int
    a_axe_y : int
    """



def input_player_name():
    """Function input_player_name()
    Cette fonction permet d'entrer le nom des joueurs.
    
    """
    
    player_list = []
    
    player_1 = input("Entrer le nom du joueur 1 : ")
    player_list.append(player_1)
    player_2 = input("Entrer le nom du joueur 2 : ")
    player_list.append(player_2)
    
    print(len(player_list))
    
    return(player_list)
    """Returns :
    player_1 : str. Contient le nom du joueur 1.
    player_2 : str. Contient le nom du joueur 2.

    """



"""
===================
PROGRAMME PRINCIPAL
===================
"""

if __name__ == '__main__':
    
    fin_partie = False
    

    # Message de lancement du jeu.
    print("+----------------------+\n    CHESS GAME V1.1\n      BRUCHE LOUIS\n+----------------------+")
    
    # Demander le nom des joueurs et les stock dans la liste player_list.
    player_list = input_player_name()
    
    
    # Premier tour de la partie.
    print(f"C'est à {player_list[0]} de commencer !")
    plateau = plateau_creation()                                                # Initialisation du plateau.
    affichage_plateau(plateau)                                                  # Affichage du plateau.
    d_axe_x, d_axe_y, a_axe_x, a_axe_y = xy_input(True)                         # xy_input, True = Joueur Blanc.
    plateau= placement_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y)
    affichage_plateau(plateau)
    # Suite de la partie.
    
    while fin_partie == False:
        print(f"C'est à {player_list[1]} de jouer.")
        d_axe_x, d_axe_y, a_axe_x, a_axe_y = xy_input(False)
        plateau = placement_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y)
        affichage_plateau(plateau)


        print(f"C'est à {player_list[0]} de jouer.")
        d_axe_x, d_axe_y, a_axe_x, a_axe_y = xy_input(True)
        plateau = placement_piece(plateau, d_axe_x, d_axe_y, a_axe_x, a_axe_y)
        affichage_plateau(plateau)
        
