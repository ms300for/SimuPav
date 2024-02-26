from tkinter import *

def CreateProjectFormulary(root):
    root.WindowsForm = Toplevel()
    root.l=Label(root.WindowsForm, text='Feche esta para poder voltar a raiz!')
    root.l.grid()
    b=Button(root.WindowsForm, text='Fechar', command=lambda: root.WindowsForm.destroy())
    b.grid()
    root.WindowsForm.geometry('300x200')
    root.WindowsForm.transient(root)#
    root.WindowsForm.focus_force()#
    root.WindowsForm.grab_set()#