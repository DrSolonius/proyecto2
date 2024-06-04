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
app_width=240
app_height=240


screen_width=app.winfo_screenwidth()
screen_height=app.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)
app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#app.resizable(0, 0)
def button_function():
    #print(entry_1.get())
    #print(entry_2.get())
    suma=float(entry_1.get())+float(entry_2.get())
    #print("button pressed")
    # Default messagebox for showing some information
    CTkMessagebox(master=app, title="Resultado", message="la suma es: "+str(suma),width=10, height=10)
    
#label para mostrar la posicion para tener una idea de las coordenadas si se quiere mover el panel
label_size=customtkinter.CTkLabel(app,text=f'Width {screen_width} Height {screen_height}')    
label_size.pack(pady=2, padx=2)
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Calcular", command=button_function)
button.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
entry_1 = customtkinter.CTkEntry(master=app, placeholder_text="ingrese numero 1",)
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=app, placeholder_text="ingrese numero 2",)
entry_2.pack(pady=5, padx=5)

app.mainloop()