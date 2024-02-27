from tkinter import *

def CreateProjectFormulary(app):
    app.WindowsForm = Toplevel()
    app.WindowsForm.title("Criar Projeto")
    app.l=Label(app.WindowsForm, text='Insira as informações do projeto')
    app.l.grid()
    b=Button(app.WindowsForm, text='Fechar', command=lambda: app.WindowsForm.destroy())
    b.grid()
    app.WindowsForm.geometry('300x200')
    app.WindowsForm.transient(app)#
    app.WindowsForm.focus_force()#
    app.WindowsForm.grab_set()#