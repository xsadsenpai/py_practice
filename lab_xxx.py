import tkinter as tk
from tkinter import messagebox
import pandas as pd


class NoteWidget:
    def __init__(self, master):
        self.master = master
        self.master.title("Заметки")

        self.notes = []

        self.label = tk.Label(master, text="Введите заметку:")
        self.label.pack()

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        self.button = tk.Button(master, text="Добавить заметку", command=self.add_note)
        self.button.pack()

        self.save_button = tk.Button(master, text="Сохранить в Excel", command=self.save_to_excel)
        self.save_button.pack()

    def add_note(self):
        note_text = self.entry.get()
        if note_text:
            self.notes.append(note_text)
            self.entry.delete(0, tk.END)
            messagebox.showinfo("Успех", "Заметка добавлена успешно!")
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите текст заметки.")

    def save_to_excel(self):
        if self.notes:
            df = pd.DataFrame({"Заметки": self.notes})
            df.to_excel("заметки.xlsx", index=False)
            messagebox.showinfo("Успех", "Заметки успешно сохранены в файл 'заметки.xlsx'.")
        else:
            messagebox.showwarning("Внимание", "Нет заметок для сохранения.")


def main():
    root = tk.Tk()
    note_widget = NoteWidget(root)
    root.mainloop()


if __name__ == "__main__":
    main()
