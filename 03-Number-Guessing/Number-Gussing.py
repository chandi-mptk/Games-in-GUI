from tkinter import Tk, StringVar, LabelFrame, Frame, Label, Entry, Button, messagebox
from random import randint


class Window:
    # Window Initialisation
    root = Tk()
    root.title("Number Guessing Game")
    width = 330
    height = 330
    root.geometry(f"{width}x{height}+100+100")

    def __init__(self):

        # Variables
        self.start_play = False
        self.random_number = None
        self.start_var = StringVar(value='1')
        self.end_var = StringVar(value='10')
        self.guessed_var = StringVar()
        self.try_counter = 1

        # Control Frame with Label
        self.control_LabelFrame = LabelFrame(self.root, text="Control Panel")
        self.control_LabelFrame.place(x=2, y=1, width=self.width - 4, height=self.height // 2)

        # About Heading of Control Label Frame
        self.about_Frame = Frame(self.control_LabelFrame)
        self.about_Frame.place(x=0, y=0, width=self.width - 4, height=self.height // 2 - 100)

        # About Label
        self.about_Label = Label(self.about_Frame,
                                 text=f"Number Guessing Game:...\n"
                                      f"Guess The Number Randomly Selected By computer\n"
                                      f"By Default Computer Guess The Number Between\n"
                                      f"1 and 10 Inclusive of both\n"
                                      f"You can Change the values and Play", font=('Arial', 7))
        self.about_Label.pack(fill='both')

        # Control Part
        self.control_Frame = Frame(self.control_LabelFrame)
        self.control_Frame.place(x=0, y=self.height // 2 - 100, width=self.width - 4, height=100)

        # Game Setting Fields
        self.start_Label = Label(self.control_Frame, text="First Number")
        self.start_Label.grid(row=0, column=0, padx=10, pady=10, sticky='n')

        self.start_Entry = Entry(self.control_Frame, width=8, textvariable=self.start_var, justify='center')
        self.start_Entry.grid(row=1, column=0, padx=10, pady=10, sticky='n')

        self.end_Label = Label(self.control_Frame, text="Last Number")
        self.end_Label.grid(row=0, column=1, padx=10, pady=10)

        self.end_Entry = Entry(self.control_Frame, width=8, textvariable=self.end_var, justify='center')
        self.end_Entry.grid(row=1, column=1, padx=10, pady=10, sticky='n')

        self.start_Button = Button(self.control_Frame, text="Start game", command=self.validate_settings)
        self.start_Button.grid(row=1, column=2, padx=10, pady=10, sticky='n')

        # Playing Area Frame
        self.guessing_LabelFrame = LabelFrame(self.root, text="Game Area")
        self.guessing_LabelFrame.place(x=2, y=self.height // 2, width=self.width - 4, height=self.height // 2 - 4)

        # Game Area
        self.guessing_Label = Label(self.guessing_LabelFrame, text="Enter Your Guess")
        self.guessing_Label.pack(pady=10)
        self.guessing_Entry = Entry(self.guessing_LabelFrame, width=8, textvariable=self.guessed_var, justify='center',
                                    state='disabled')
        self.guessing_Entry.pack(pady=10)
        self.guessing_Button = Button(self.guessing_LabelFrame, text="Submit", command=self.validate_guess,
                                      state='disabled')
        self.guessing_Button.pack(pady=10)

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
        if (abs(start_no - end_no) + 1) < 10:
            messagebox.showerror("Setting Error", "Minimum Possibility Should 10 Numbers")
        else:

            # If Number List is In any Order Generate Random Number
            if start_no < end_no:
                self.random_number = randint(start_no, end_no)
            else:
                self.random_number = randint(end_no, start_no)

            # Set Play Status
            self.start_play = True

            # Off Control Area and On Game Area
            self.setting_play_switch()

    # According to Play State Set or disable Control Area or Guessing Area
    def setting_play_switch(self):
        if self.start_play:
            self.start_Entry.config(state='disabled')
            self.end_Entry.config(state='disabled')
            self.guessing_Entry.config(state='normal')
            self.guessing_Button.config(state='normal')
        else:
            self.start_Entry.config(state='normal')
            self.end_Entry.config(state='normal')
            self.guessing_Entry.config(state='disabled')
            self.guessing_Button.config(state='disabled')

    # Validate Guessed Number
    def validate_guess(self):

        # Check The Entered String is Number
        try:
            guess_no = int(self.guessed_var.get())

            # Calculate the Quarter, Half of the range
            quarter = abs(int(self.start_var.get()) - int(self.end_var.get())) / 4
            half = abs(int(self.start_var.get()) - int(self.end_var.get())) / 2

        except Exception as e:
            messagebox.showerror("Error Guessed",
                                 f"Your Guess should be a number in range {self.start_var.get()} "
                                 f"and {self.end_var.get()}\n{e}")
            self.guessed_var.set("")
            return

        # IF Guess Correct
        if self.random_number == guess_no:
            messagebox.showinfo("Success", "You Guessed Correctly")

            # Ask Play Again or Not?
            self.play_again()

        # Guess Is Wrong
        else:

            # Calculate How Off the Prediction
            guessed_offset = abs(self.random_number - guess_no)

            # If Guess Off Less Than or Equal to half the Prediction is Very Close
            if guessed_offset <= quarter:
                messagebox.showinfo("Guess Accuracy", f"The Guess is Very Close\nAttempt No {self.try_counter}")
                self.guessed_var.set(value="")

            # If Guess Off Less Than or Equal to quarter the Prediction is Not Very Close
            elif guessed_offset <= half:
                messagebox.showinfo("Guess Accuracy", f"The Guess is Not Very Close\nAttempt No {self.try_counter}")
                self.guessed_var.set(value="")

            # If Guess Off More Than Half It's Too Far
            else:
                messagebox.showinfo("Guess Accuracy", f"The Guess is Very Far\nAttempt No {self.try_counter}")
                self.guessed_var.set(value="")

            # Increment Attempt Counter
            self.try_counter += 1

            # You can Only Try to Guess the number only less than 50% of the total numbers
            if self.try_counter > half:
                messagebox.showerror("No More Try", f"You Tried {self.try_counter - 1} Times it is Nearly 50% of "
                                                    f"Possibilities")

                # Ask Play Again or Not?
                self.play_again()

    # Ask Play Again or Not?
    def play_again(self):
        play_again = messagebox.askyesno("Play Again", "Do You Want to Play Again?")
        self.guessed_var.set(value="")

        # If Want to play Agani
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
