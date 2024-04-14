import tkinter as tk
from modules import *

def button1():

    text_to_add = encrypt(text.get("1.0", "end-1c"))
    text.delete(1.0, tk.END)
    text.insert(tk.END, text_to_add)


def button2():
    text_to_add = decrypt(text.get("1.0", "end-1c"))
    text.delete(1.0, tk.END)
    text.insert(tk.END, text_to_add)


# tkinter page setup
root = tk.Tk()
root.title("Resizable Text Input")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

text = tk.Text(frame, wrap=tk.WORD)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, command=text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text.config(yscrollcommand=scrollbar.set)

button1 = tk.Button(root, text="Encrypt", command=button1)
button1.pack(side="left")
button2 = tk.Button(root, text="Decrypt", command=button2)
button2.pack(side="right")


root.mainloop()
