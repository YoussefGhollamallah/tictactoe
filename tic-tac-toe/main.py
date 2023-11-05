#  -*- coding: utf-8 -*-s
import tkinter

# fonction qui permet de renvoyer quel symbole à gagné
def print_winner():
    global win

    if win is False:
        win = True
        print("Le joueur " + current_player + " a gagner")

# fonction permettant de changer de joueur à chaque tour
def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"  


# permet de vérifier la victoire selon la direction
def check_win(clicked_row, clicked_col):
    # detecter la victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button['text'] == current_player:
            count += 1
    
    if count == 3 :
        print_winner()
    

    # dectecter la victoire verticalement
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # dectecter la victoire en diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # dectecter la victoire en diagonale inversé
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print()

    # vérifie qu'aucun joueur à gagné est affiche le match nul
    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button["text"] == "X" or current_button["text"] == "O":
                    count +=1
        if count == 9:
            print("Match nul")


# permet de placé le symbole et de vérifié que la case est bien vide
def place_symbol(row, column):
    clicked_button = buttons[column][row]
    if clicked_button["text"] == "":
        clicked_button.config(text=current_player)

        check_win(row, column)
        switch_player()


# Permet d'afficher les buttons en forme de carré et donné une forme de grille
def draw_grid():
    for column in range(3):
        button_in_cols = []
        for row in range(3):
            button = tkinter.Button(windows,
                                    font=("Arial",50),
                                    width=5, height=3,
                                    command=lambda r=row, c=column :place_symbol(r,c),
                                    bg='#ffffff'
                                    )
            button.grid(row=row,padx=1, pady=1,column=column)
            button_in_cols.append(button)
        buttons.append(button_in_cols)

buttons = []
current_player = "X"
win = False

# création de la fenetre du jeu
windows = tkinter.Tk()

# personnalisation de la fenetre
windows.title("TicTacToe")
windows.minsize(500, 500)
windows.config(bg="blue")

draw_grid()
# permet d'ouvrir l'application
windows.mainloop()