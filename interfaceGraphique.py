# coding: utf-8
 
from tkinter import * 

class IHM:
    
    def __init__(self):
        self.fenetre = Tk()
        self.inter.demander_choix
        self.label = Label(fenetre, text='question')
        self.label.pack()    

        self.fenetre['bg']='white'

        # frame 1
        Frame1 = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        self.bouton1 = Button(Frame1, text="Beurk", height=4, width=9, background="red")
        self.bouton1.pack()

        Frame1 = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Bof", height=4, width=9, background="orange")
        Bouton.pack()

        Frame1 = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Bon", height=4, width=9, background="yellow")
        Bouton.pack()

        Frame1 = Frame(self.fenetre, borderwidth=2, relief=GROOVE)
        Frame1.pack(side=LEFT, padx=50, pady=30)
        Bouton = Button(Frame1, text="Délicieux", height=4, width=9, background="green")
        Bouton.pack()
        
        
        self.fenetre.mainloop()
    def demander_choix(self, question,listeChoix):
        """modifier les valeurs de question et liste choix
        puis retourner le choix cliqué par l'utilisateur"""

        self.label.config(text=question)

        self.bouton1.config(text=listeChoix[0]) 
    

    
        
