#pip install CTkTable
import customtkinter
import tkinter as tk
from tkinter import ttk
#aparencia del fondo
customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
#color button
customtkinter.set_default_color_theme("bl   ue")  # Themes: blue (default), dark-blue, green

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

app.mainloop()
