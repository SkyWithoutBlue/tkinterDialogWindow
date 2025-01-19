import tkinter as tk
from tkinter import scrolledtext
from Note import Note  # Добавляем импорт класса Note

class TextEditWindow(tk.Toplevel):
    def __init__(self, parent, filename):
        super().__init__(parent)
        self.note = Note(filename)
        self.geometry("800x600")
        self.text_area = scrolledtext.ScrolledText(self, width=96, height=35)
        self.text_area.insert(tk.END, self.note.get_note_text())
        self.text_area.pack()
        self.button = tk.Button(self, text="Сохранить", command=self.save_note)
        self.button.pack()

    def save_note(self):
        new_text = self.text_area.get(1.0, tk.END)
        self.note.save_note(new_text)
        self.destroy()