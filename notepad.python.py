import tkinter as tk
from tkinter import filedialog

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def save_as_file():
    save_file()

def cut_text():
    try:
        text_area.event_generate("<<Cut>>")
    except tk.TclError:
        pass

def copy_text():
    try:
        text_area.event_generate("<<Copy>>")
    except tk.TclError:
        pass

def paste_text():
    try:
        text_area.event_generate("<<Paste>>")
    except tk.TclError:
        pass

root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Text Area
text_area = tk.Text(root, wrap="word", bg="white", fg="black", insertbackground="black", font=("Arial", 14))
text_area.pack(expand=1, fill=tk.BOTH)

# Buttons Outside the Panel
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=10)

save_as_button = tk.Button(button_frame, text="Save As", command=save_as_file, bg="white", fg="black", font=("Arial", 12))
save_as_button.pack(side=tk.LEFT, padx=5)

cut_button = tk.Button(button_frame, text="Cut", command=cut_text, bg="white", fg="black", font=("Arial", 12))
cut_button.pack(side=tk.LEFT, padx=5)

copy_button = tk.Button(button_frame, text="Copy", command=copy_text, bg="white", fg="black", font=("Arial", 12))
copy_button.pack(side=tk.LEFT, padx=5)

paste_button = tk.Button(button_frame, text="Paste", command=paste_text, bg="white", fg="black", font=("Arial", 12))
paste_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
