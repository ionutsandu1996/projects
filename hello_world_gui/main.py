import tkinter as tk

def on_click():
    label.config(text="Hello World!")

root = tk.Tk()
root.title("Hello World GUI")

root.geometry("300x150")

label = tk.Label(root, text="Apasa butonul", font=("Arial", 14))
label.pack(pady=10)

button = tk.Button(root, text = "Click", command=on_click)
button.pack()

root.mainloop()