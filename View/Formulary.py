from tkinter import *

def CreateProjectFormulary(app):
    email = StringVar()
    
    app.WindowsForm = Toplevel()
    app.WindowsForm.title("Criar Projeto")
    
    app.base_frame = Frame(app.WindowsForm)
    app.base_frame.pack(padx=40, pady=10, fill='x', expand=True)
    
    app.label = Label(app.base_frame, text='Insira as informações do projeto')
    app.label.grid()
    
    app.ok_button = Button(app.base_frame, text="criar")
    app.ok_button.grid()
    app.close_button = Button(app.base_frame, text='Fechar', command=lambda: app.WindowsForm.destroy())
    app.close_button.grid()
    
    app.WindowsForm.geometry('300x200')
    app.WindowsForm.resizable(False, False)
    app.WindowsForm.transient(app)
    app.WindowsForm.focus_force()
    app.WindowsForm.grab_set()