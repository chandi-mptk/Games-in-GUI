from tkinter import Tk, Frame, Button, Label, messagebox


class TicTacToe:
    # Window Initialisation
    root = Tk()
    root.title("Tic Tac Toe")
    width = 330
    height = 330
    root.geometry(f"{width}x{height}+100+100")

    def __init__(self):

        # Variable Declaration
        self.player = 'X'  # First Player is X
        self.cell_values = {}  # Players Entry In a Dict
        self.cell_Button_Dict = {}  # Button Matrix Saved In Dict

        # Player Name Frame
        self.player_name_Frame = Frame(self.root, bg='white')
        self.player_name_Frame.place(x=0, y=0, width=self.width, height=50)

        # Button Matrix Background Frame
        self.cell_Frame = Frame(self.root, bg='lightblue')
        self.cell_Frame.place(x=0, y=50, width=self.width, height=self.height)

        # Currently, Playing Player
        self.player_name_Label = Label(self.player_name_Frame, text=f"Player: {self.player}", font=("Arial", 20),
                                       bg='white')
        self.player_name_Label.pack(fill='both')

        # Set Column Size for Unused columns/Rows
        self.cell_Frame.grid_columnconfigure(0, minsize=50)
        self.cell_Frame.grid_rowconfigure(0, minsize=20)

        # Assign Variable Values and Create Button Matrx
        self.start_playing()

    def start_playing(self):

        # Assign Values to Variables
        self.player = 'X'
        self.cell_values = {}
        self.cell_Button_Dict = {}
        for i in range(1, 4):
            for j in range(1, 4):
                self.cell_values[i, j] = ""

        # Current Player Name Display
        self.player_name_Label.config(text=f"Player: {self.player}")

        # Create Button Matrix and Store in a Dict Key as The X, Y Values
        # Button calls a Function to Validate Game Status
        for i in range(1, 4):
            for j in range(1, 4):
                cell_Button = Button(self.cell_Frame, text="", width=3, font=("Arial", 20),
                                     command=lambda row=i, col=j: self.game_validation(row, col))
                cell_Button.grid(row=i, column=j, padx=10, pady=10)
                self.cell_Button_Dict[f"{i}{j}"] = cell_Button

    # Validate Game Status
    def game_validation(self, i, j):

        # Show Player Sign to The Button Clicked
        self.cell_Button_Dict[f"{i}{j}"].config(text=f"{self.player}")

        # Enter Player's Cell Selection To Dict
        self.cell_values[i, j] = self.player

        # Get all The Selected Cell List
        key_list = [k for k, v in self.cell_values.items() if v == self.player]

        # If Selected More Than 2 Cells Check Game Won or Finished
        if 2 < len(key_list):

            # Send The List of Selections of Current User To Winning Check
            if self.line_fill_check(key_list):

                # If Won Play Again?
                play_again = messagebox.askyesno("Game Over",
                                                 f"Player {self.player} Won The Game\nDo you Want to Play Again?")
                if play_again:

                    # Re-Start Game
                    self.start_playing()
                    return
                else:

                    # Quit Game
                    self.root.quit()
            else:

                # Current Player Done All Moves?
                if len(key_list) == 5:

                    # No One Win The Game Tie....
                    play_again = messagebox.askyesno("Game Over",
                                                     f"Both Are Good In The Game Tie!!!...\nDo you Want to Play Again?")
                    if play_again:

                        # Re-Start Game
                        self.start_playing()
                        return
                    else:

                        # Quit Game
                        self.root.quit()

        # If Current Player Done Switch Player For Next Player's Turn
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

        # Update Player Current Player
        self.player_name_Label.config(text=f"Player: {self.player}")

    @staticmethod
    # Check If The Player Won or Not
    def line_fill_check(key_list):
        for i in range(1, 4):

            # Any Row Booked?
            if sum(map(lambda x: 1 if x[0] == i else 0, key_list)) == 3:
                return True

            # Any Column Booked
            if sum(map(lambda y: 1 if y[1] == i else 0, key_list)) == 3:
                return True

            # Top Left To Bottom Right Diagonal Booked
            if sum(map(lambda val: 1 if val[0] == val[1] else 0, key_list)) == 3:
                return True

            # Top Right To Bottom Left Diagonal Booked
            if sum(map(lambda val: 1 if sum(val) == 4 else 0, key_list)) == 3:
                return True

        # No Line Booked
        return False

    # Run Tkinter Window
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.run()
