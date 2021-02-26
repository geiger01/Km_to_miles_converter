from tkinter import *

window = Tk()
window.title("km to miles converter")
window.minsize(width=500, height=300)

my_label= Label(text="0", font=("Ariel", 10, "bold"))
my_label.place(x=220, y=150)

my_label2= Label(text="Km", font=("Ariel", 15, "bold"))
my_label2.place(x=300, y=60)

my_label3= Label(text="is equal to", font=("Ariel", 15, "bold"))
my_label3.place(x=80, y=150)

my_label4= Label(text="Miles", font=("Ariel", 15, "bold"))
my_label4.place(x=300, y=150)

def convert():
    new_text = float(input.get()) * 1.609
    my_label.config(text=new_text)

def reset():
    my_label.config(text="0")


button = Button(text="Calculate", command=convert)
button.place(x=200, y=100)

button2 = Button(text="Reset", command=reset)
button2.place(x=210, y=200)

input = Entry(width=10)
print(input.get())
input.place(x=200, y=60)






window.mainloop()