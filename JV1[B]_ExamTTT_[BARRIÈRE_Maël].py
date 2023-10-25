#Tic Tac Toe

#1 - Écrire la fonction per:mettant d'afficher la grille grâce aux données du tableau

class TicTacToe:
    board = list
    current_player = str
    ligne = int
    col = int
    
def board(self):
    self.board = [[''for i in range(3)] for i in range (3)]
    self.current_player = "X"
def print_board(self):
    print("---")
    for ligne in self.board:
        print("|", end = "")
        for cell in ligne:
            print(cell, end = "|")
        print("\n---")

#2 - Écrire la fonction permettant de jouer un O ou un X. Elle prend un tableau en entrée, et le modifie afin d’ajouter un O ou un X à l’endroit souhaité par le joueur courant.

def bouger(self, ligne: int, col :int):
    if ligne < 0 or ligne >= 3 or col < 0 or col >=3 or self.board[ligne][col]!= 0:
        raise ValueError ("Déplacement impossible")
    self.board[ligne][col] = self.current_player
    self.current_player = "O" if self.current_player == "X" else "X"
    
#3 & 4 - Écrire la fonction vérifiant si la grille est complète et si il y a un gagnant ayant aligner trois points

def gagnant(self):
    for ligne in self.board :
        if ligne[0] == ligne[1] == ligne[2] != " ":
            return ligne[0]
    for col in range(3):
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
            return self.board[0][col]
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
        return self.board[0][0]
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
        return self.board[0][2]
    return None

#5 - Écrire un programme permettant de jouer à deux au Tic tac toe

class TicTacToe:
    board = list
    current_player = str
    second_player = str
    ligne = int
    col = int
    
def board(self):
    self.board = [[''for i in range(3)] for i in range (3)]
    self.current_player = "X"
    self.second_player =  "O"
def print_board(self):
    print("---")
    for ligne in self.board:
        print("|", end = "")
        for cell in ligne:
            print(cell, end = "|")
        print("\n---")
def bouger(self, ligne: int, col :int):
    if ligne < 0 or ligne >= 3 or col < 0 or col >=3 or self.board[ligne][col]!= 0:
        raise ValueError ("Déplacement impossible")
    self.board[ligne][col] = self.current_player and self.second_player
    self.second_player = "O" if self.current_player == "X" else "X"

def gagnant(self):
    for ligne in self.board :
        if ligne[0] == ligne[1] == ligne[2] != " ":
            return ligne[0]
    for col in range(3):
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
            return self.board[0][col]
    if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
        return self.board[0][0]
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
        return self.board[0][2]
    return None

#6 - Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de Puissance 4 ?

#Afin de programmer un Puissance 4 il nous faudra augmenter le nombre de cases avec le def board
#on devrait donc faire def board(self): self.board = [[''for i in range(4)] for i in range (4)] par exemple.
#Pareil pour définir un vainceur. Mais, surtout, le Puissance 4 joue sur la gavité, pour placer un jeton il est nécessaire qu'un autre se trouve en dessous.
#Impossible de les placers où on le souhaites dans les cases comme avec le Tic Tac Toe, alors, tant que le jeton parcour des cases vides, le programme ne cesse
#de déplacer ce dernier dans un sens unique jusqu'à ce qu'il atterisse au sol ou sur un autre jeton.
#On peut se simplifier la vie en déterminant un nouveau jeton comme étant le sol de la case à laquelle il appartient tant qu'aucun nouveau ne s'est posé sur lui.
    