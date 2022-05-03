from  tkinter import*
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

#j'ai mis l'application dans une class et j'ai appelé le constructeur
class formulaire_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.parent = parent # c'est pour garder une référence de parent
        self.initialize()# j'ai créé la methode initialize pour y créer tous nos widget

    def initialize(self):
      self.grid()
        

     #   button = tkinter.Button(self,text=u"Click me !")
        #button.grid(column=3,row=6)
    
if __name__ == "__main__":
    app =  formulaire_tk(None)
    app.title('Blinder') 
    app.geometry( '700x700')
    app['bg'] = 'orange'
    app.resizable(height=False,width=False)
    label = Label(app, text="Cv Blinder", font=("Verdana", 30, "italic bold"), fg="white", bg="orange")
    label.place(x=250, y=1)
    app.sourceFile = '' 

    def chooseFile():
     app.sourceFile = filedialog.asksaveasfile(initialdir="/", title='Please select a file')
     entry.delete(0, END)
     entry.insert(0, app.sourceFile.name)
     entry.place( x=400, y=150)
  
   

b_chooseFile =Button(app, text = "Selectionnez votre fichier", width = 20, height = 2, command = chooseFile)
b_chooseFile.place(x = 170,y = 150)
entry = Entry(app)

button = Button(app,text=u"Convertir")
button.place(x =170, y = 300)

button = Button(app,text=u"Télécharger")
button.place(x =330, y = 300)
app.mainloop() 

