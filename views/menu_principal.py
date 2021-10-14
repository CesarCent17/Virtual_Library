from tkinter import *
from centrar import *
from views.configuracion import *
from views.ciencia_ficcion import *
import sys

class MenuP:
    def __init__(self,obj_usuario):
        self.credenciales = obj_usuario
        self.obj_centrar = Centro()
        self.getVentana()
        self.ventana_menu.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")

        #Objevo canvas
        self.canvas = Canvas(self.ventana_menu,bg="#ffffff",height=600,width=1000,bd=0,highlightthickness=0,relief="ridge")
        self.canvas.place(x=0, y=0)

        #Background
        background_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/MenuP/background.png")
        background = self.canvas.create_image(500.0, 301.5,image=background_img)

        ###################################################################################
        #Buttons
        #Fantasia
        img0 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/MenuP/img0.png")
        self.fantasia = Button(self.ventana_menu,image=img0,borderwidth=0,highlightthickness=0,relief="flat", bg="#FFFFFF")
        self.fantasia.place(x=-32, y=195,width=260,height=73)
        #Ciencia ficcion
        img1 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/MenuP/img1.png")
        self.ciencia_ficcion = Button(self.ventana_menu,image=img1,borderwidth=0,highlightthickness=0,
                                      relief="flat", bg="#FFFFFF", command=self.eleccionFiccion)
        self.ciencia_ficcion.place(x=-32, y=94,width=260,height=73)
        #Drama
        img2 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/MenuP/img2.png")
        self.drama = Button(self.ventana_menu,image=img2,borderwidth=0,highlightthickness=0,relief="flat", bg="#FFFFFF")
        self.drama.place(x=-32, y=296,width=260,height=73)
        ###################################################################################

        #Configuracion
        img3 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/MenuP/img3.png")
        self.configuracion = Button(self.ventana_menu,image=img3,borderwidth=0,highlightthickness=0,
                                    relief="flat", bg="#FFFFFF", command=self.settings)
        self.configuracion.place(x=825, y=25,width=62,height=62)
        #Salir
        img4 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/MenuP/img4.png")
        self.salir = Button(self.ventana_menu,image=img4,borderwidth=0,highlightthickness=0,
                            relief="flat", bg="#FFFFFF", command=self.cerrarSesion)
        self.salir.place(x=905, y=25,width=62,height=62)

        self.ventana_menu.mainloop()


    def getVentana(self):
        self.ventana_menu = Toplevel()
        self.ventana_menu.title("Bienvenido")
        self.obj_centrar.centrar_ventana(self.ventana_menu, 600, 1000)
        self.ventana_menu.resizable(0, 0)

    def eleccionFiccion(self):
        obj = Ficcion()

    def settings(self):
        obj = Configuracion(self.credenciales)

    def cerrarSesion(self):
            self.ventana_menu.destroy()
            sys.exit()


