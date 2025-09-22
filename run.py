from geminiFunctions import myFunction
import tkinter as tk


root = tk.Tk()

button = tk.Button(root, text="Click", command=myFunction)
button.pack()


root.mainloop()
