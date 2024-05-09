import tkinter
import tkinter.messagebox
import customtkinter
import os
# import time
# import psutil
# import matrices


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")

# custom_font = ("Helvetica", 30) # font used in the buttons of the puzzle
# empty_tile = "    " # text used in the empty tile
          
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("PDF maker")
        self.geometry(f"{1480}x{720}")

        # configure grid layout (4x4) and others general configurations
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, weight=1)

        # left side bar section
        # self.init_left_sidebar()



    def quit_simulation_event(self):
        self.destroy()
        exit()
