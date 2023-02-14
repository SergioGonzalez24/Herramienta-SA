# Desarrollo de Interfaz grafica para Herramientas.py

import tkinter as tk
import customtkinter as ctk # type: ignore

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app_herramientas = ctk.CTk()  # create CTk window like you do with the Tk window
app_herramientas.geometry("600x900") # set the size of the window


app_herramientas.mainloop() # start the mainloop