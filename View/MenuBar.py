import tkinter as tk

def InitConfigureMenuBar(app):
    app.MenuBar = tk.Menu(app)
    app.config(menu=app.MenuBar)
    
    AddProjectMenu(app)
    AddObjectsMenu(app)
    
    app.MenuBar.add_cascade(label="Projeto", menu=app.ProjectMenu, underline=0)
    app.MenuBar.add_cascade(label="Componentes", menu=app.ObjectsMenu, underline=0)
    
    UpdateMenuConfig(app)
    
def UpdateMenuConfig(app):
    if (app.AppConfigs.HasChargeProject):
        app.ProjectMenu.entryconfigure('Abrir Projeto', state=tk.NORMAL)
        app.ProjectMenu.entryconfigure('Fechar Projeto', state=tk.NORMAL)
        app.MenuBar.entryconfigure('Componentes', state=tk.NORMAL)
    else:
        app.ProjectMenu.entryconfigure('Abrir Projeto', state=tk.DISABLED)
        app.ProjectMenu.entryconfigure('Fechar Projeto', state=tk.DISABLED)
        app.MenuBar.entryconfigure('Componentes', state=tk.DISABLED)
        
def AddProjectMenu(app):
    app.ProjectMenu = tk.Menu(app.MenuBar, tearoff=0)   
    app.ProjectMenu.add_command(label="Criar Projeto", 
                                command = lambda: app.AppConfigs.ProjectService.CreateProject(app))
    app.ProjectMenu.add_command(label="Abrir Projeto")
    app.ProjectMenu.add_command(label="Fechar Projeto")
    app.ProjectMenu.add_separator()
    app.ProjectMenu.add_command(label="Fechar", command=app.destroy)

def AddObjectsMenu(app):
    app.ObjectsMenu = tk.Menu(app.MenuBar, tearoff=0)
    
    AddMaterialMenu(app)
    AddLayerMenu(app)
    
    app.ObjectsMenu.add_cascade(label="Materiais", menu=app.MaterialsMenu, underline=0)
    app.ObjectsMenu.add_cascade(label="Layer", menu=app.LayerMenu, underline=0)
    
def AddMaterialMenu(app):
    app.MaterialsMenu = tk.Menu(app.ObjectsMenu, tearoff=0)
    app.MaterialsMenu.add_command(label="Adicionar")
    app.MaterialsMenu.add_command(label="Listar")

def AddLayerMenu(app):
    app.LayerMenu = tk.Menu(app.ObjectsMenu, tearoff=0)
    app.LayerMenu.add_command(label="Adicionar")
    app.LayerMenu.add_command(label="Listar")