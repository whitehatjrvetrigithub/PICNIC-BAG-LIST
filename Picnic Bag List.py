from tkinter import *
import random
root=Tk()
root.title("Picnic Items")
root.geometry("600x600")

listdisplay=Label(root)
randomvalue=Label(root)
items=["Bottle", "Tiffin", "ID Card", "Chocolates", "Chips", "Tickets", "Hanky"]
listdisplay["text"]="Listed items - " + str(items)
def grn():
    random_num1 = random.randint(0, len(items)-1)
    randomvalue["text"]="Put item number " + str(random_num1) + " in the bag."

button1 = Button(root, text="Which item to put in the bag?", command=grn, fg="white", bg="orange")
button1.place(relx=0.5, rely=0.4, anchor=CENTER)
listdisplay.place(relx=0.5, rely=0.2, anchor=CENTER)
randomvalue.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()