import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_files(directory):
    if not os.path.exists(directory):
        messagebox.showerror("Ошибка", "Указанная директория не существует")
        return

    files_list = os.listdir(directory)
    messagebox.showinfo("Результат", f"Количество файлов в директории '{directory}': {len(files_list)}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        count_files(directory)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Подсчет файлов")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Выберите директорию:")
    label.pack()

    button = tk.Button(frame, text="Обзор", command=select_directory)
    button.pack()

    root.mainloop()
