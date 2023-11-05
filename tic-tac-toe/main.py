#  -*- coding: utf-8 -*-s
import tkinter

def check_win(clicked_row, clicked_col):
    # detecter la victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        
        if current_button['text'] == "X":
            count += 1
    
    if count == 3 :
        print("Gagner horizontalement")


def place_symbol(row, column):
    print("click",row,column)

    clicked_button = buttons[column][row]
    clicked_button.config(text="X")

    check_win(row, column)

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

# création de la fenetre du jeu
windows = tkinter.Tk()

# personnalisation de la fenetre
windows.title("TicTacToe")
windows.minsize(500, 500)
windows.config(bg="blue")


draw_grid()
# permet d'ouvrir l'application
windows.mainloop()