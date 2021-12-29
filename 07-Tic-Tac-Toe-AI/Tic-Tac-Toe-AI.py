import time
from tkinter import *
from random import choice
from tkinter import messagebox


class Player:
    def __init__(self, letter):
        # Player X or O
        self.letter = letter

    # Players Next Move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, moves):
        return choice(moves)


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass


class Window:

    # Window Initialisation
    root = Tk()
    root.title("Tic Tac Toe")
    width = 330
    height = 430
    root.geometry(f"{width}x{height}+100+100")
    root.resizable(False, False)

    def __init__(self):

        # Instance
        self.tic_tac_toe = TicTacToe()
        self.player_x = None
        self.player_o = None

        # Variables
        self.options = ["Computer",
                        "Player"]
        self.player_x_Var = StringVar(value=self.options[0])
        self.player_o_Var = StringVar(value=self.options[0])
        self.x_score_var = IntVar(value=0)
        self.o_score_var = IntVar(value=0)
        self.point = {'row': 0, 'col': 0}
        self.is_playing = True
        self.is_x = False
        self.cell_Button_Dict = {}

        # Control Panel
        self.control_Frame = Frame(self.root, bg='gray')
        self.control_Frame.place(x=0, y=0, width=self.width, height=100)

        self.player_x_Label = Label(self.control_Frame, text="X Player")
        self.player_x_Label.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        self.player_x_OptionMenu = OptionMenu(self.control_Frame, self.player_x_Var, *self.options)
        self.player_x_OptionMenu.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.player_x_OptionMenu.config(width=len(self.options[0]))

        self.player_o_Label = Label(self.control_Frame, text="O Player")
        self.player_o_Label.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

        self.player_o_OptionMenu = OptionMenu(self.control_Frame, self.player_o_Var, *self.options)
        self.player_o_OptionMenu.grid(row=1, column=2, padx=10, pady=10, sticky='ew')
        self.player_o_OptionMenu.config(width=len(self.options[0]))

        self.start_Button = Button(self.control_Frame, text="Start", font=('Arial', 13), command=self.start_game)
        self.start_Button.grid(row=1, column=3, padx=15, pady=10, sticky='ew')

        # Score Board
        self.score_board_Frame = Frame(self.root, bg='light gray')
        self.score_board_Frame.place(x=0, y=100, width=self.width, height=50)

        self.score_Label = Label(self.score_board_Frame, width=len(self.options[0]), text="Score")
        self.score_Label.grid(row=0, column=1, padx=5, pady=1, sticky='ew')

        self.x_score_Label = Label(self.score_board_Frame, width=len(self.options[0]), textvariable=self.x_score_var)
        self.x_score_Label.grid(row=1, column=0, padx=5, pady=1, sticky='ew')

        self.o_score_Label = Label(self.score_board_Frame, width=len(self.options[0]), textvariable=self.o_score_var)
        self.o_score_Label.grid(row=1, column=2, padx=5, pady=1, sticky='ew')

        # Button Matrix Background Frame
        self.cell_Frame = Frame(self.root, bg='lightblue')
        self.cell_Frame.place(x=0, y=150, width=self.width, height=self.height)

        # Set Column Size for Unused columns/Rows
        self.cell_Frame.grid_columnconfigure(0, minsize=50)
        self.cell_Frame.grid_rowconfigure(0, minsize=20)

        for row in range(1, 4):
            cell_Button_Dict = {}
            for col in range(1, 4):
                cell_Button = Button(self.cell_Frame, text="", width=3, font=("Arial", 20),
                                     command=lambda r=row, c=col: self.point_update((r, c)))
                cell_Button_Dict[col] = cell_Button
            self.cell_Button_Dict[row] = cell_Button_Dict

    def start_game(self):
        self.menu_control()
        while self.is_playing:
            move_list = self.tic_tac_toe.available_moves()
            if self.is_x:
                if self.player_x_Var.get() == "Computer":
                    self.player_x = RandomComputerPlayer("X")
                    if move_list:
                        cell = self.player_x.get_move(move_list)
                        self.tic_tac_toe.board[cell[0]][cell[1]] = "X"
                        self.update_cell()
                        if self.tic_tac_toe.is_there_a_winner("X"):
                            messagebox.showinfo("Victory", "Player X Won The Game")
                            self.x_score_var.set(self.x_score_var.get() + 1)
                            self.tic_tac_toe.game_restart()
                    else:
                        messagebox.showinfo("Tie...!!!", "It\'s a tie...!!!")
                        self.tic_tac_toe.game_restart()
                    self.is_x = not self.is_x
            else:
                if self.player_o_Var.get() == "Computer":
                    self.player_o = RandomComputerPlayer("O")
                    if move_list:
                        cell = self.player_o.get_move(move_list)
                        self.tic_tac_toe.board[cell[0]][cell[1]] = "O"

                        self.update_cell()
                        if self.tic_tac_toe.is_there_a_winner("O"):
                            messagebox.showinfo("Victory", "Player O Won The Game")
                            self.o_score_var.set(self.o_score_var.get() + 1)
                            self.tic_tac_toe.game_restart()
                    else:
                        messagebox.showinfo("Tie...!!!", "It\'s a tie...!!!")
                        self.tic_tac_toe.game_restart()
                    self.is_x = not self.is_x
                else:
                    self.player_o = HumanPlayer("O")



    def menu_control(self):
        if self.is_playing:
            for widget in self.control_Frame.winfo_children():
                widget.config(state='disabled')
            for row in range(1, 4):
                for col in range(1, 4):
                    self.cell_Button_Dict[row][col].grid(row=row, column=col, padx=10, pady=10)
        else:
            for widget in self.control_Frame.winfo_children():
                widget.config(state='normal')
            for row in range(1, 4):
                for col in range(1, 4):
                    self.cell_Button_Dict[row][col].grid_forget()

    def point_update(self, cell):
        move_list = self.tic_tac_toe.available_moves()
        if self.is_x:
            if not self.player_x:
                self.player_x = HumanPlayer("X")
            if move_list:
                self.tic_tac_toe.board[cell[0]][cell[1]] = "X"
                self.update_cell()
                if self.tic_tac_toe.is_there_a_winner("X"):
                    messagebox.showinfo("Victory", "Player X Won The Game")
                    self.x_score_var.set(self.x_score_var.get() + 1)
                    self.tic_tac_toe.game_restart()
            else:
                messagebox.showinfo("Tie...!!!", "It\'s a tie...!!!")
                self.tic_tac_toe.game_restart()
            self.is_x = not self.is_x




            self.tic_tac_toe.board[cell[0]][cell[1]] = "X"
        else:
            self.tic_tac_toe.board[cell[0]][cell[1]] = "O"
        self.update_cell()

    def update_cell(self):
        for row in range(1, 4):
            for col in range(1, 4):
                self.cell_Button_Dict[row][col].config(text=f"{self.tic_tac_toe.board[row][col]}")

    def run(self):
        self.root.mainloop()


class TicTacToe:
    def __init__(self):
        self.board = {row: {col: "" for col in range(1, 4)} for row in range(1, 4)}
        self.current_winner = False

    def available_moves(self):
        moves = []
        for row in range(1, 4):
            for col in range(1, 4):
                if self.board[row][col] == "":
                    moves.append((row, col))
        return moves

    def is_there_a_winner(self, player):

        # Row Selected By Same Player
        if any(all(True if self.board[i][j] == player else False for j in range(1, 4)) for i in range(1, 4)):
            return True

        # Column Selected By Same Player
        if any(all(True if self.board[j][i] == player else False for j in range(1, 4)) for i in range(1, 4)):
            return True

        # Diagonal 1 (\) Selected By Same Player
        if all(True if self.board[i][i] == player else False for i in range(1, 4)):
            return True

        # Diagonal 2 (/) Selected By Same Player
        if all(True if self.board[i][4-i] == player else False for i in range(1, 4)):
            return True

        # No Line Booked
        return False

    def game_restart(self):
        self.board = {row: {col: "" for col in range(1, 4)} for row in range(1, 4)}


if __name__ == '__main__':
    win = Window()
    win.run()


