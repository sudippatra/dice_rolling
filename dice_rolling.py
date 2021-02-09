from tkinter import *
import random
root = Tk()
root.title("Dice Simulator")
root.geometry("600x500")
label = Label(root, font = ("Helvetica", 300, 'bold'), text = "", fg = "green")
def rolldice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text = f'{random.choice(dice)}')
    label.pack()
button = Button(root, font= ("Helvetica", 20, 'bold'), text = "Roll Dice", bg = "lightblue", command = rolldice)
button.pack(side = "bottom")
root.mainloop()