import tkinter as tk
import os
from AppSettings import AppSettings

from View.MenuBar import InitConfigureMenuBar
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.AppConfigs = AppSettings()
        
        self.title("Abaqus Dataset Generator")
        self.geometry("600x400+50+50")
        InitConfigureMenuBar(self)
        
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()