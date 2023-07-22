import customtkinter as ctk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo, showerror
from tkinter.font import Font

from video import DownloadVideo

def choose_directory():
    chosen_directory = askdirectory()
    path_entry.delete(0, ctk.END)
    path_entry.insert(ctk.END, chosen_directory)


def download_video():
    video_url = url_entry.get()
    output_directory = path_entry.get()

    # Проверка наличия URL и пути сохранения
    if not video_url:
        showerror('Ошибка', 'Введите URL видео')
        return

    if not output_directory:
        showerror('Ошибка', 'Выберите папку для сохранения')
        return

    downloader = DownloadVideo(video_url, output_directory)

    try:
        downloader.get_video()
        video_info = downloader.get_video_info()
        if video_info:
            info_text = f"Название видео: {video_info.get('Название видео', 'Нет информации')}\nАвтор: {video_info.get('Автор', 'Нет информации')}"
        else:
            info_text = "Информация о видео недоступна"
        showinfo("Успешно", f"Видео успешно скачано.\n\n{info_text}")
    except Exception as e:
        showerror("Ошибка", f"Ошибка при скачивании видео: {e}")

root = ctk.CTk()
root.geometry('400x200')
root.resizable(False, False)
root.title('YouTube Downloader')

# Поля ввода для URL и пути для сохранения
font = ctk.CTkFont(family='Consolas', size=14,)

url_label = ctk.CTkLabel(
    root, 
    text='URL видео:', 
    text_color='#999999',
    font=font,
    )
url_label.pack()

url_entry = ctk.CTkEntry(
    root, 
    width=300, 
    fg_color='#f0d930', 
    border_color='gray', 
    text_color='#1c1c1b',
    font=font,
    )
url_entry.pack()

path_label = ctk.CTkLabel(
    root, 
    text='Путь для сохранения:', 
    text_color='#999999',
    font=font,
    )
path_label.pack()

path_entry = ctk.CTkEntry(
    root, 
    width=300, 
    fg_color='#f0d930', 
    border_color='gray', 
    text_color='#1c1c1b',
    font=font,
    )
path_entry.pack()

# Кнопка для выбора папки сохранения
choose_button = ctk.CTkButton(
    root, 
    width=145,
    text='Выбрать папку', 
    command=choose_directory, 
    fg_color='#f0d930', 
    hover_color='#ffff42',
    border_color='gray', 
    text_color='#1c1c1b',
    font=font,
    )
choose_button.place(x=50, y=125)

# Кнопка для скачивания видео и вывода информации о нем
download_button = ctk.CTkButton(
    root, 
    width=145,
    text='Скачать видео', 
    command=download_video, 
    fg_color='#f0d930', 
    hover_color='#ffff42', 
    border_color='gray', 
    text_color='#1c1c1b',
    font=font,
    )
download_button.place(x=200, y=125)

root.mainloop()
