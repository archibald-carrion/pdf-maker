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
    def init_left_sidebar(self):
        # create and configure the sidebar frame
        self.left_sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.left_sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_sidebar_frame.grid_rowconfigure(5, weight=1)

        # create and configure the logo label
        self.logo_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="PDF maker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))   # set the logo at the top of the left column

        # create and configure the appearance option menu and label
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["Light", "Dark", "System"],
                                                                    command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(0, 10))  # Removed padding at the bottom
        self.appearance_mode_optionemenu.set("Dark")
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="Appearance Mode: ", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(0, 10))

        # create and configure the scaling option menu and label
        self.scaling_label = customtkinter.CTkLabel(self.left_sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=3, column=0, padx=20, pady=(10, 5))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                            command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=4, column=0, padx=20, pady=(5, 10))  # Removed padding at the bottom
        self.scaling_optionemenu.set("100%")

        # created and configure the quit button
        self.quit_button = customtkinter.CTkButton(self.left_sidebar_frame, command=self.quit_simulation_event)
        self.quit_button.grid(row=6, column=0, padx=20, pady=(10, 40))
        self.quit_button.configure(state="enabled", text="Quit simulation")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def quit_simulation_event(self):
        self.destroy()
        exit()
