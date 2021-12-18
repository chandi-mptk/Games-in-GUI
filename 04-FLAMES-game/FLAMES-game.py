from tkinter import Tk, StringVar, LabelFrame, Label, Entry, Button
from re import match
from tkinter import messagebox


class Window:

    # Window Initialisation
    root = Tk()
    root.title("Flames Calculator")
    width = 300
    height = 250
    root.geometry(f"{width}x{height}+100+100")
    root.resizable(False, False)

    def __init__(self):

        # Program Class Initialise
        self.flames_class = FLAMES()

        # Variable Declaration
        self.name_1_var = StringVar()
        self.name_2_var = StringVar()

        # Frame, Label, Entry & Button Field Creation
        self.flames_LabelFrame = LabelFrame(self.root, text="FLAMES Test")
        self.flames_LabelFrame.place(x=10, y=30, width=self.width - 20, height=180)

        self.name_1_Label = Label(self.flames_LabelFrame, text='First Name')
        self.name_1_Label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.name_1_Entry = Entry(self.flames_LabelFrame, textvariable=self.name_1_var)
        self.name_1_Entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.name_2_Label = Label(self.flames_LabelFrame, text='Second Name')
        self.name_2_Label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.name_2_Entry = Entry(self.flames_LabelFrame, textvariable=self.name_2_var)
        self.name_2_Entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        self.flames_Button = Button(self.flames_LabelFrame, text="Calculate", command=self.flames_calculate)
        self.flames_Button.grid(row=3, column=1, padx=10, pady=10, sticky='e')

    # Button Function
    def flames_calculate(self):

        # Get data
        n1 = self.name_1_var.get()
        n2 = self.name_2_var.get()

        # Clear Entry field
        self.name_1_var.set("")
        self.name_2_var.set("")

        # Validate the data with Flames Class
        if self.flames_class.valid_names(n1, n2):

            # Get Result of the Test
            result = self.flames_class.flames_test()

            # Show The Relation
            messagebox.showinfo("Relation is", f"{n1} and {n2} are {result}")
        else:
            messagebox.showerror("Error", "Entered Name Contains Non Acceptable String")

    # Run The Tkinter Main Loop
    def run(self):
        self.root.mainloop()


class FLAMES:

    def __init__(self):
        self.flames_dict = {"F": "Friends", "L": "Lovers", "A": "in Affection", "M": "Married", "E": "Enemies",
                            "S": "Siblings"}
        self.names = []

    # Validation and Filter
    def valid_names(self, a, b):

        # Check If Blank
        if a != '' and b != '':

            # Join Both Names
            c = a + b

            # Check All are Letters, Space or '.'
            if match("^[a-zA-Z .]*$", c):

                # Convert to Set ro remove Duplicate Letters by keeping one
                c_set = set([letter.lower() for letter in c])

                # Converted To List
                self.names = list(c_set)

                # Accept as Valid
                return True
            else:
                return False
        else:
            return False

    # Count the Flames to get the result
    def flames_test(self):
        length_name = len(self.names)
        flames_list = list(self.flames_dict.keys())
        f_len = len(flames_list)
        while f_len == 1:
            x = length_name % f_len
            flames_list.pop(x)
            f_len = len(flames_list)
        return self.flames_dict[flames_list[0]]


# If The File Directly Open Run else Do Nothing
if __name__ == "__main__":
    win = Window()
    win.run()
