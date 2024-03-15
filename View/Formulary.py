from tkinter import *

def CreateProjectFormulary(app):
    project_name = StringVar()
    
    app.WindowsForm = Toplevel()
    app.WindowsForm.title("Criar Projeto")
    app.WindowsForm.geometry('300x150')
    app.WindowsForm.resizable(False, False)
    app.WindowsForm.transient(app)
    app.WindowsForm.focus_force()
    app.WindowsForm.grab_set()
    
    app.base_frame = Frame(app.WindowsForm)
    app.base_frame.pack(padx=5, pady=5, fill='x', expand=True)

    app.base_frame.columnconfigure(0, weight=1)
    app.base_frame.columnconfigure(1, weight=5)
    
    app.label_project_name = Label(app.base_frame, text='Nome do projeto: ')
    app.label_project_name.grid(column=0, row=0, sticky=W, padx=5, pady=5)

    app.project_name_entry = Entry(app.base_frame, textvariable=project_name)
    app.project_name_entry.grid(column=1, row=0, sticky=W, padx=5, pady=5)
    
    app.ok_button = Button(app.base_frame, text="criar")
    app.ok_button.grid(column=1, row=1, sticky=W, padx=5, pady=5)

    app.close_button = Button(app.base_frame, text='Fechar', command=lambda: app.WindowsForm.destroy())
    app.close_button.grid(column=1, row=1, padx=5, pady=5)