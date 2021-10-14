from tkinter import *
from centrar import *
import webbrowser as wb
from tkinter import messagebox


class Ficcion:
    def __init__(self):
        self.obj_centrar = Centro()
        self.getVentana()
        self.ventana_ficcion.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")

        #Objeto canvas
        canvas = Canvas(self.ventana_ficcion, bg="#ffffff", height=600, width=1000, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        #Background
        background_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Ficcion/background.png")
        background = canvas.create_image(653.0, 299.5, image=background_img)

        ###################################################################################
        #Buttons
        #1984
        img0 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Ficcion/img0.png")
        self.libro1 = Button(self.ventana_ficcion,image=img0, borderwidth=0, highlightthickness=0,
                             relief="flat", bg="#ffffff", command=self.abrirlibro1)
        self.libro1.place(x=85, y=118, width=136, height=136)
        #La ultima pregunta
        img1 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Ficcion/img1.png")
        self.libro2 = Button(self.ventana_ficcion,image=img1, borderwidth=0, highlightthickness=0,
                             relief="flat", bg="#ffffff", command=self.abrirlibro2)
        self.libro2.place(x=85, y=275, width=136, height=136)
        #Yo, robot
        img2 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Ficcion/img2.png")
        self.libro3 = Button(self.ventana_ficcion,image=img2, borderwidth=0, highlightthickness=0,
                             relief="flat", bg="#ffffff", command=self.abrirlibro3)
        self.libro3.place(x=85, y=432, width=136, height=136)
        #Volver
        img3 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Ficcion/img3.png")
        self.volver = Button(self.ventana_ficcion,image=img3, borderwidth=0, highlightthickness=0,
                             relief="flat", bg="#ffffff", command=self.accionVolver)
        self.volver.place(x=913, y=37, width=50, height=50)
        ###################################################################################

        self.ventana_ficcion.mainloop()

    def getVentana(self):
        self.ventana_ficcion = Toplevel()
        self.ventana_ficcion.title("Editar perfil")
        self.obj_centrar.centrar_ventana(self.ventana_ficcion, 600, 1000)
        self.ventana_ficcion.resizable(0, 0)

    def accionVolver(self):
        self.ventana_ficcion.destroy()

    #Eleccion
    def abrirlibro1(self):
        wb.open_new(r"C:/Users/PC/Pictures/Virtual Library/books/Ciencia ficcion/George Orwell 1984.pdf")
    def abrirlibro2(self):
        wb.open_new(r"C:/Users/PC/Pictures/Virtual Library/books/Ciencia ficcion/Isaac Asimov la ultima pregunta.pdf")
    def abrirlibro3(self):
        wb.open_new(r"C:/Users/PC/Pictures/Virtual Library/books/Ciencia ficcion/Isaac Asimov yo robot.pdf")

    #Prueba
    def mensajeEleccion(self):
        messagebox.showinfo("Elección de libro", "El libro se abrirá en su aplicación predeterminada")
