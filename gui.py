#!/bin/python3

import customtkinter as customtk
import interface

class App(customtk.CTk):
    def __init__(self):
        super().__init__()

        #MAIN WINDOW PROPERTIES
        self.title("Project-A")
        self.geometry("1000x700")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        customtk.set_appearance_mode("dark")



        ##LEFT SIDE BUTTONS
        #frame definitions
        self.button_frame = customtk.CTkFrame(self)
        self.button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(0, weight=1)
        self.button_frame.grid_rowconfigure(1, weight=0)

        #category frame
        self.cat_button_frame = customtk.CTkFrame(self.button_frame)
        self.cat_button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.cat_button_frame.grid_rowconfigure(0, weight=1)

        #category buttons
        self.button_1 = customtk.CTkButton(self.cat_button_frame, text="Politics")
        self.button_1.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.button_2 = customtk.CTkButton(self.cat_button_frame, text="Finance")
        self.button_2.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        self.button_3 = customtk.CTkButton(self.cat_button_frame, text="Weather")
        self.button_3.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

        self.button_4 = customtk.CTkButton(self.cat_button_frame, text="General")
        self.button_4.grid(row=3, column=0, padx=10, pady=10, sticky="nw")


        #menu frame
        self.menu_button_frame = customtk.CTkFrame(self.button_frame)
        self.menu_button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="sw")
        self.menu_button_frame.grid_rowconfigure((0, 1), weight=0)

        #menu buttons
        self.button_3 = customtk.CTkButton(self.menu_button_frame, text="Settings")
        self.button_3.grid(row=0, column=0, padx=10, pady=10, sticky='sw')

        self.button_4 = customtk.CTkButton(self.menu_button_frame, text="Fetch", command=interface.refresh)
        self.button_4.grid(row=1, column=0, padx=10, pady=10, sticky='sw')




        ##MAIN APPLICATION FRAME
        #main frame init (row/col config with main label and scrolling frame)
        self.main_frame = customtk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=0)
        self.main_frame.grid_rowconfigure(1, weight=1)

        
        self.heading = customtk.CTkLabel(self.main_frame, text='Politics', font=('Ubuntu', 24))
        self.heading.grid(row=0, column=0, padx=30, pady=10, sticky='nw')

        self.scrolling_frame = ScrollingFrame(self.main_frame)
        self.scrolling_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')      
       


class ScrollingFrame(customtk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        #story tiles        
        self.story_tile_1 = customtk.CTkFrame(self)
        self.story_tile_1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.story_tile_2 = customtk.CTkFrame(self)
        self.story_tile_2.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        self.story_tile_3 = customtk.CTkFrame(self)
        self.story_tile_3.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

        self.story_tile_4 = customtk.CTkFrame(self)
        self.story_tile_4.grid(row=4, column=0, padx=10, pady=10, sticky='ew')


        #story contents



app = App()
app.mainloop()
