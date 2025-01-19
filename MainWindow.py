import tkinter as tk
from Methods import Methods
from TextEditWindow import TextEditWindow
from Note import Note  # Добавляем импорт класса Note

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__name = "Приложение для заметок"
        self.notes = []
        self.create_widgets()

    def create_widgets(self):
        self.title(self.__name)
        self.geometry("800x600")

        # Кнопка добавления новой заметки
        self.add_button = tk.Button(self, text="+", font=('Arial', 16), command=self.create_note_card)
        self.add_button.pack(side='bottom', pady=5)

        # Отображение существующих заметок
        for note_filename in Methods.get_note_list():
            self.create_note_card(note_filename)

    def start(self):
        self.mainloop()

    def create_note_card(self, filename=None):
        if not filename:
            filename = Note.create_note()
            if not filename:
                return  # Если имя файла не было введено, выходим из функции
        edit_note = TextEditWindow(self, filename)
        edit_note.grab_set()