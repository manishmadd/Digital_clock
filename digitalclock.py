from cProfile import label
from struct import pack
from tkinter import Tk, Label

window =Tk()
window.title("Digital Clock")
window.geometry("600×300")
window.configure(bg="steelblue")
label=Label(window, text="welcome", font=("Arial Black", 78, "bold"), bg="stellblue", fg="whiteblue")
label.pack(pady=100)
window.mainloop()







