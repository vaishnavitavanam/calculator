from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

player = "X"
board = [""] * 9

def click(btn, index):
    global player
    if board[index] == "":
        btn["text"] = player
        board[index] = player
        if check_win():
            Label(root, text=f"Player {player} wins!", font=("Arial", 14)).grid(row=3, column=0, columnspan=3)
            disable_all()
        elif "" not in board:
            Label(root, text="It's a draw!", font=("Arial", 14)).grid(row=3, column=0, columnspan=3)
        else:
            player_switch()

def player_switch():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def check_win():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for win in wins:
        if board[win[0]] == board[win[1]] == board[win[2]] != "":
            return True
    return False

def disable_all():
    for btn in buttons:
        btn["state"] = "disabled"

buttons = []
for i in range(9):
    btn = Button(root, text="", font=("Arial", 20), width=5, height=2)
    btn.grid(row=i//3, column=i%3)
    btn.config(command=lambda b=btn, idx=i: click(b, idx))
    buttons.append(btn)

root.mainloop()