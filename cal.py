from tkinter import *

#Window
root = Tk()
root.title("Calculator")
root.geometry("250x300")
root.resizable(False, False)
#Frames
display_area = Frame(root)
display_area.pack(fill="x")
row_zero = Frame(root)
row_zero.pack()
row_one = Frame(root)
row_one.pack()
row_two = Frame(root)
row_two.pack()
row_three = Frame(root)
row_three.pack()
row_four = Frame(root)
row_four.pack()
#displayarea
text_display_area = Entry(display_area, font={"arial", 18, "bold"}, textvariable = "default", width = 50, bg = "#ffffff", bd=0)
display_text_variable = StringVar()
current_display_text = ""
display_text_variable.set(current_display_text)
display_text = Label(
    display_area,
    font={"arial", 120, "bold"},
    textvariable=display_text_variable,
    width=32,
    height=2,
    bg="#ffffff",
    bd=5,
    anchor="e",
    justify="left",
)
display_text.grid(column=0, row=0, sticky="E")
display_text.pack(fill="x")

#Methods
class CalcDisplay(object):
    def __init__(self):
        self.current_display_text = ""

    def add_text(self, text_to_add):
        self.current_display_text += text_to_add
        display_text_variable.set(self.current_display_text)


    def eval(self):
        try:
            eval_text = eval(self.current_display_text)
            self.current_display_text = str(eval_text)
            display_text_variable.set(str(self.current_display_text))
            self.current_display_text = ""
        except Exception as e:
            display_text_variable.set("e")
            pass

    def clear(self):
        self.current_display_text = ""
        display_text_variable.set(self.current_display_text)


calc_display = CalcDisplay()


def zero_callBack():
    calc_display.add_text("0")


def one_callBack():
    calc_display.add_text("1")


def two_callBack():
    calc_display.add_text("2")


def three_callBack():
    calc_display.add_text("3")


def four_callBack():
    calc_display.add_text("4")


def five_callBack():
    calc_display.add_text("5")


def six_callBack():
    calc_display.add_text("6")


def seven_callBack():
    calc_display.add_text("7")


def eight_callBack():
    calc_display.add_text("8")


def nine_callBack():
    calc_display.add_text("9")


def exp_callBack():
    calc_display.add_text("**")

def modulo_callBack():
    calc_display.add_text("%")


def multiply_callBack():
    calc_display.add_text("*")


def divide_callBack():
    calc_display.add_text("/")


def add_callBack():
    calc_display.add_text("+")


def subtract_callBack():
    calc_display.add_text("-")


def dot_callBack():
    calc_display.add_text(".")


def equal_callBack():
    calc_display.eval()


def clear_callBack():
    calc_display.clear()

#button
clear_button = Button(row_zero, text="Clear", fg="black", width="50", height="2", command=clear_callBack)
seven_button = Button(row_one, text="7", fg="black", width=6, height=3, command=seven_callBack)
eight_button = Button(row_one, text="8", fg="black", width=6, height=3, command=six_callBack)
nine_button = Button(row_one, text="9", fg="black", width=6, height=3, command=nine_callBack)
divide_button = Button(row_one, text="/", fg="black", width=6, height=3, command=divide_callBack)
modulo_button = Button(row_one, text="%", fg="black", width=6, height=3, command=modulo_callBack)
four_button = Button(row_two, text="4", fg="black", width=6, height=3, command=four_callBack)
five_button = Button(row_two, text="5", fg="black", width=6, height=3, command=five_callBack)
six_button = Button(row_two, text="6", fg="black", width=6, height=3, command=six_callBack)
plus_button = Button(row_two, text="+", fg="black", width=6, height=3, command=add_callBack)
minus_button = Button(row_two, text="-", fg="black", width=6, height=3, command=subtract_callBack)
one_button = Button(row_three, text="1", fg="black", width=6, height=3, command=one_callBack)
two_button = Button(row_three, text="2", fg="black", width=6, height=3, command=two_callBack)
three_button = Button(row_three, text="3", fg="black", width=6, height=3, command=three_callBack)
zero_button = Button(row_four, text="0", fg="black", width=25, height=3, command=zero_callBack)
dot_button = Button(row_three, text=".", fg="black", width=6, height=3, command=dot_callBack)
exp_button = Button(row_three, text="EXP", fg="black", width=6, height=3, command=exp_callBack)
equal_button = Button(row_four, text="=", fg="black", width=25, height=3, command=equal_callBack)


clear_button.pack()
seven_button.pack(side=LEFT)
eight_button.pack(side=LEFT)
nine_button.pack(side=LEFT)
divide_button.pack(side=LEFT)
modulo_button.pack(side=LEFT)
four_button.pack(side=LEFT)
five_button.pack(side=LEFT)
six_button.pack(side=LEFT)
plus_button.pack(side=LEFT)
minus_button.pack(side=LEFT)
one_button.pack(side=LEFT)
two_button.pack(side=LEFT)
three_button.pack(side=LEFT)
dot_button.pack(side=LEFT)
exp_button.pack(side=LEFT)
zero_button.pack(side=LEFT)
equal_button.pack()




root.mainloop()