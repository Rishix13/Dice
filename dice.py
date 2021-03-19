import random
import tkinter

root = tkinter.Tk()
root.geometry("600x400")
root.title('Dice')

label = tkinter.Label(root,font = ('Algeria',200))

def roll_dice():
	dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
	label.pack()


b1 = tkinter.Button(root, text = "Click here to roll", command = roll_dice)
b1.place(x='235',y='10')
#b1.pack()

root.mainloop()