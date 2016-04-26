import tkinter

top = tkinter.Tk()

quit = tkinter.Button(top, text = 'Hello world!',
    command = top.quit)
quit.pack()
tkinter.mainloop()
