from tkinter import *
from centrar import *



class Creditos:
    def __init__(self):
        self.obj_centrar = Centro()
        self.getVentana()
        self.ventana_creditos.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")

        #Objeto canvas
        canvas = Canvas(self.ventana_creditos,bg="#ffffff",height=600,width=1000,bd=0,
            highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Creditos/background.png")
        background = canvas.create_image(500.0, 309.0,image=background_img)

        #Button volver
        img0 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Creditos/img0.png")
        self.volver = Button(self.ventana_creditos,image=img0,borderwidth=0,highlightthickness=0,command=self.accionVolver,
            relief="flat")
        self.volver.place(x=884, y=51,width=50,height=50)
        self.ventana_creditos.mainloop()

    def getVentana(self):
        self.ventana_creditos = Toplevel()
        self.ventana_creditos.title("Créditos")
        self.obj_centrar.centrar_ventana(self.ventana_creditos, 600, 1000)
        self.ventana_creditos.resizable(0, 0)
    def accionVolver(self):
        self.ventana_creditos.destroy()