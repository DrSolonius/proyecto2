#pip install CTkTable
from CTkMessagebox import CTkMessagebox
import customtkinter
import tkinter as tk
from tkinter import ttk
#aparencia del fondo
customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
#color button
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.resizable(0, 0)
def button_function():
    print(entry_1.get())
    print(entry_2.get())
    suma=float(entry_1.get())+float(entry_2.get())
    print("button pressed")
    # Default messagebox for showing some information
    CTkMessagebox(master=app, title="Resultado", message="la suma es: "+str(suma),width=10, height=10)
    
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
entry_1 = customtkinter.CTkEntry(master=app, placeholder_text="ingrese numero 1",)
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=app, placeholder_text="ingrese numero 2",)
entry_2.pack(pady=5, padx=5)


app.mainloop()