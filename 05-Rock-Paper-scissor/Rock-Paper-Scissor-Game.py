from tkinter import Tk, IntVar, StringVar, LabelFrame, Label, Button
from random import randint
from tkinter import messagebox


class Window:
    # Window Initialisation
    root = Tk()
    root.title("Rock Paper scissor Game")
    width = 800
    height = 600
    root.geometry(f"{width}x{height}+0+0")
    root.resizable(False, False)

    def __init__(self):
        # Close [X] Button Function
        self.root.protocol("WM_DELETE_WINDOW", self.__callback)

        # Variable Initialisation
        self.option_list = {1: "Rock", 2: "Paper", 3: "Scissor"}
        self.score_player_var = IntVar(value=0)
        self.score_pc_var = IntVar(value=0)
        self.game_state_var = StringVar(value="Select Prediction")
        self.playing = False

        # About Game Area
        self.about_LabelFrame = LabelFrame(self.root, text="About")
        self.about_LabelFrame.place(x=self.width // 2, y=5, width=self.width // 2 - 10, height=150)

        self.about_Label = Label(self.about_LabelFrame, text=f"Start Game: \n"
                                                             f"Click on your Selection in User Area "
                                                             f"Rock, Paper Scissor\n\n"
                                                             f"Winning Rules as follows :\n"
                                                             f"Rock vs paper-> paper wins\n"
                                                             f"Rock vs scissor-> Rock wins\n"
                                                             f"paper vs scissor-> scissor wins.", font=('Arial', 8))
        self.about_Label.pack()

        # User Area
        self.user_LabelFrame = LabelFrame(self.root, text="User Area")
        self.user_LabelFrame.place(x=5, y=5, width=self.width // 2 - 10, height=self.height - 110)

        self.rock_Button = Button(self.user_LabelFrame, text="Rock", width=15, font=('Arial', 30),
                                  command=lambda: self.process_prediction(1))
        self.rock_Button.pack(pady=35)

        self.paper_Button = Button(self.user_LabelFrame, text="Paper", width=15, font=('Arial', 30),
                                   command=lambda: self.process_prediction(2))
        self.paper_Button.pack(pady=35)

        self.scissor_Button = Button(self.user_LabelFrame, text="Scissor", width=15, font=('Arial', 30),
                                     command=lambda: self.process_prediction(3))
        self.scissor_Button.pack(pady=35)

        # Computer Play Area
        self.pc_LabelFrame = LabelFrame(self.root, text="Computer Area")
        self.pc_LabelFrame.place(x=self.width // 2, y=155, width=self.width // 2 - 10, height=self.height - 260)

        self.pc_Button = Button(self.pc_LabelFrame, text="", width=15, height=6, font=('Arial', 30),
                                state='disabled')
        self.pc_Button.pack(fill='none', expand=True)

        # Score Area
        self.score_LabelFrame = LabelFrame(self.root, text="Score Area")
        self.score_LabelFrame.place(x=5, y=self.height - 105, width=self.width - 15, height=100)

        self.player_Label = Label(self.score_LabelFrame, text="Player", font=('Arial', 15))
        self.player_Label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.player_score_Label = Label(self.score_LabelFrame, textvariable=self.score_player_var, font=('Arial', 15))
        self.player_score_Label.grid(row=1, column=0, padx=10, pady=5, sticky='ew')

        self.score_LabelFrame.grid_columnconfigure(1, minsize=580)

        self.game_status_Label = Label(self.score_LabelFrame, textvariable=self.game_state_var, font=('Arial', 30))
        self.game_status_Label.grid(row=0, column=1, rowspan=2, padx=10, pady=5, sticky='ew')

        self.pc_Label = Label(self.score_LabelFrame, text="Computer", font=('Arial', 15))
        self.pc_Label.grid(row=0, column=2, padx=10, pady=5, sticky='e')

        self.pc_score_Label = Label(self.score_LabelFrame, textvariable=self.score_pc_var, font=('Arial', 15))
        self.pc_score_Label.grid(row=1, column=2, padx=10, pady=5, sticky='ew')

    def process_prediction(self, selection):
        self.playing = True
        self.switch_state()
        pc_prediction = randint(1, 3)
        test_list = [selection, pc_prediction]

        self.pc_Button.config(text=self.option_list[pc_prediction])
        if 1 in test_list and 2 in test_list:
            if test_list[0] == 2:
                self.score_player_var.set(value=self.score_player_var.get() + 1)
            else:
                self.score_pc_var.set(value=self.score_pc_var.get() + 1)
            self.game_state_var.set("Paper Won...!!!")
        elif 1 in test_list and 3 in test_list:
            if test_list[0] == 1:
                self.score_player_var.set(value=self.score_player_var.get() + 1)
            else:
                self.score_pc_var.set(value=self.score_pc_var.get() + 1)
            self.game_state_var.set("Rock Won...!!!")
        elif 2 in test_list and 3 in test_list:
            if test_list[0] == 3:
                self.score_player_var.set(value=self.score_player_var.get() + 1)
            else:
                self.score_pc_var.set(value=self.score_pc_var.get() + 1)
            self.game_state_var.set("Scissor Won...!!!")
        else:
            self.game_state_var.set("Tie...!!!")

        self.playing = False
        self.switch_state()

    def switch_state(self):
        if self.playing:
            self.rock_Button.config(state='disabled')
            self.paper_Button.config(state='disabled')
            self.scissor_Button.config(state='disabled')
        else:
            self.rock_Button.config(state='normal')
            self.paper_Button.config(state='normal')
            self.scissor_Button.config(state='normal')

    # Callback Function for Close Button
    def __callback(self):
        if self.score_pc_var.get() == self.score_player_var.get():
            result = "Tie...!!!"
        elif self.score_pc_var.get() < self.score_player_var.get():
            result = "Player Won The Game."
        else:
            result = "Computer Won The Game."

        messagebox.showinfo("Final Score", f"Scores\n\n"
                                           f"Player - {self.score_player_var.get()}\n"
                                           f"Computer - {self.score_pc_var.get()}\n\n"
                                           f"{result}")

        self.root.quit()

    # Run The Tkinter Main Loop
    def run(self):
        self.root.mainloop()


# If The File Directly Open Run else Do Nothing
if __name__ == "__main__":
    win = Window()
    win.run()
