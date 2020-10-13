import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH")

lbl.pack()
btn.pack()
tk.mainloop()