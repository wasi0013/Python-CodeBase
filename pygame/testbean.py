from Tkinter import *

class Program:
    def __init__(self):
        top = Tk()

        self.chk1Checked = BooleanVar()

        chk1 = Checkbutton(top, text = "Testing", variable = self.chk1Checked)
        chk1.pack()

        btn1 = Button(top, text = "Click Me", command = self.btn1CallBack)
        btn1.pack()

        top.mainloop()

    def btn1CallBack(self):
        print(self.chk1Checked.get())

if __name__ == "__main__":
    Program()
