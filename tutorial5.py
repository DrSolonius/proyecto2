#pip install CTkTable
import customtkinter
import tkinter as tk
from tkinter import ttk
#aparencia del fondo
customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
#color button
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print(entry_1.get())
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
entry_1 = customtkinter.CTkEntry(master=app, placeholder_text="CTkEntry",)
entry_1.pack(pady=10, padx=10)

treeview = ttk.Treeview(columns=("size", "lastmod"))
treeview.heading("#0", text="File")
treeview.heading("size", text="Size")
treeview.heading("lastmod", text="Last modification")
treeview.insert(
    "",
    tk.END,
    text="README.txt",
    values=("850 bytes", "18:30")
)
treestyle = ttk.Style()
treestyle.theme_use('default')
###Treeview Customisation (theme colors are selected)
bg_color = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
text_color = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkLabel"]["text_color"])
selected_color = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkButton"]["fg_color"])
treestyle.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color, borderwidth=0)
treestyle.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
app.bind("<<TreeviewSelect>>", lambda event: app.focus_set())
treeview.pack()

app.mainloop()
