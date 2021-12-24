from tkinter import Tk, StringVar, LabelFrame, Frame, Label, Entry, Button, messagebox, OptionMenu, IntVar


class Window:

    # Window Initialisation
    root = Tk()
    root.title("Number Guessing Game")
    width = 330
    height = 330
    root.geometry(f"{width}x{height}+100+100")
    root.resizable(False, False)

    def __init__(self):

        # Variables
        self.start_play = False
        self.start_var = StringVar(value='1')
        self.end_var = StringVar(value='10')
        self.guessed_var = IntVar()
        self.probable_low = 0
        self.probable_high = 0
        self.guessed_status_var = StringVar(value="")
        self.try_counter = 1

        # Dropdown menu options
        self.options = [
            "Guessed High",
            "Guessed Low",
            "Guessed Correct"
        ]

        # Control Frame with Label
        self.control_LabelFrame = LabelFrame(self.root, text="Information Panel")
        self.control_LabelFrame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.45)

        # About Heading of Control Label Frame
        self.about_Frame = Frame(self.control_LabelFrame)
        self.about_Frame.place(relx=0, rely=0, relwidth=0.99, relheight=0.50)

        # About Label
        self.about_Label = Label(self.about_Frame,
                                 text=f"Number Guessed by Computer Game:...\n"
                                      f"User Give the Range to Computer\n"
                                      f"Computer will Predict your Number\n"
                                      f"You Have to Say Weather the number is Low, High or Correct\n",
                                 font=('Arial', 7))
        self.about_Label.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.99)

        # Control Part
        self.control_Frame = Frame(self.control_LabelFrame)
        self.control_Frame.place(relx=0, rely=0.40, relwidth=0.99, relheight=0.50)

        # Game Setting Fields
        self.start_Label = Label(self.control_Frame, text="First Number")
        self.start_Label.grid(row=0, column=0, padx=15, pady=5, sticky='n')

        self.start_Entry = Entry(self.control_Frame, width=8, textvariable=self.start_var, justify='center')
        self.start_Entry.grid(row=1, column=0, padx=15, pady=5, sticky='n')

        self.end_Label = Label(self.control_Frame, text="Last Number")
        self.end_Label.grid(row=0, column=1, padx=15, pady=5)

        self.end_Entry = Entry(self.control_Frame, width=8, textvariable=self.end_var, justify='center')
        self.end_Entry.grid(row=1, column=1, padx=15, pady=5, sticky='n')

        self.start_Button = Button(self.control_Frame, text="Start game", command=self.validate_settings)
        self.start_Button.grid(row=1, column=2, padx=15, pady=5, sticky='n')

        # Playing Area Frame
        self.guessing_LabelFrame = LabelFrame(self.root, text="Game Area")
        self.guessing_LabelFrame.place(relx=0.01, rely=0.46, relwidth=0.98, relheight=0.54)

        # Game Area Define
        self.guessing_Label = Label(self.guessing_LabelFrame, text="Computer Guessed")
        self.guessed_number = Entry(self.guessing_LabelFrame, textvariable=self.guessed_var, state='readonly',
                                    justify='center')
        self.guessing_OptionMenu = OptionMenu(self.guessing_LabelFrame, self.guessed_status_var, *self.options)
        self.guessing_Button = Button(self.guessing_LabelFrame, text="Submit", command=self.validate_guess)

    # Validate Control Area Setting and Generate Number to Guess
    def validate_settings(self):

        # Is the Entered string is Number
        try:
            start_no = int(self.start_var.get())
            end_no = int(self.end_var.get())
        except Exception as e:
            messagebox.showerror("Settings Error", f"First and Last Must Be Numbers\n{e}")
            self.start_var.set('1')
            self.end_var.set('10')
            return

        # Is the Number Range is Valid (min 10 Integers Length)
        if (end_no - start_no + 1) < 10:
            messagebox.showerror("Setting Error", "Minimum Possibility Should 10 Numbers")
            return
        else:
            self.probable_low = start_no
            self.probable_high = end_no

            # If Number List is In any Order Generate Random Number
            self.new_guess()

            # Set Play Status
            self.start_play = True

            # Off Control Area and On Game Area
            self.setting_play_switch()

    def new_guess(self):
        self.guessed_var.set(value=(self.probable_low + self.probable_high) // 2)

    # According to Play State Set or disable Control Area or Guessing Area
    def setting_play_switch(self):
        if self.start_play:
            self.start_Entry.config(state='disabled')
            self.end_Entry.config(state='disabled')
            self.start_Button.config(state='disabled')

            self.guessing_Label.pack(pady=5)
            self.guessed_number.pack(pady=5)

            self.guessing_OptionMenu.pack(pady=5)
            self.guessing_Button.pack(pady=5)

        else:
            self.start_Entry.config(state='normal')
            self.end_Entry.config(state='normal')
            self.start_Button.config(state='normal')
            self.guessed_status_var.set("")
            self.guessing_Label.pack_forget()
            self.guessed_number.pack_forget()
            self.guessing_OptionMenu.pack_forget()
            self.guessing_Button.pack_forget()

    # Validate Guessed Number
    def validate_guess(self):
        status = self.guessed_status_var.get()
        max_try = len(self.end_var.get()) + 1
        if status:
            if self.try_counter < max_try:
                if status == 'Guessed High' and (self.probable_high - self.probable_low) > 2:
                    self.probable_high = self.guessed_var.get()
                    self.try_counter += 1
                    self.new_guess()
                elif status == 'Guessed Low' and (self.probable_high - self.probable_low) > 2:
                    self.probable_low = self.guessed_var.get()
                    self.try_counter += 1
                    self.new_guess()
                else:
                    messagebox.showinfo("Computer Won", f"Computer Won in {self.try_counter} Attempt")
                    self.play_again()
            else:
                messagebox.showinfo("You Won", f"Computer not able to Guess The number in {max_try} Attempt")
                self.play_again()
        else:
            messagebox.showerror("Guess Rating Blank", "Select The State Of Guess")

    # Ask Play Again or Not?
    def play_again(self):
        play_again = messagebox.askyesno("Play Again", "Do You Want to Play Again?")
        self.guessed_var.set(0)

        # If you Want to play Again
        if play_again:

            # Reset Game and Play Status
            self.start_play = False
            self.try_counter = 1

            # Activate Control Area
            self.setting_play_switch()

        # Don't Want to Play Again Quit The Game
        else:
            self.root.quit()

    # Run The Tkinter Main Loop
    def run(self):
        self.root.mainloop()


# If The File Directly Open Run else Do Nothing
if __name__ == "__main__":
    win = Window()
    win.run()
