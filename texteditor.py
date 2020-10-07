import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def fileOpen():
    filepath = askopenfilename(
        filetypes = [("All Files", "*.*")]
    )

    if not filepath:
        return
    textEdit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textEdit.insert(tk.END, text)

    w.title(f"Rupin's Text Editor - {filepath}")

def fileSave():
    filepath = asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [("All Files", "*.*")]
    )

    if not filepath:
        return
    with open(filepath, "w") as outputFile:
        text = textEdit.get("1.0", tk.END)
        outputFile.write(text)

    w.title(f"Rupin's Text Editor - {filepath}")

w = tk.Tk()
w.title("Rupin's Text Editor")

w.rowconfigure(0, minsize = 800, weight = 1)
w.columnconfigure(1, minsize = 800, weight = 1)

textEdit = tk.Text(w)

buttonFrame = tk.Frame(w)

openBut = tk.Button(buttonFrame, text = "Open", command = fileOpen)
saveBut = tk.Button(buttonFrame, text = "Save As...", command = fileSave)

openBut.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
saveBut.grid(row = 1, column = 0, sticky = "ew", padx = 5, pady = 5)

buttonFrame.grid(row = 0, column = 0, sticky = "ns")
textEdit.grid(row = 0, column = 1, sticky = "nsew")


w.mainloop()
