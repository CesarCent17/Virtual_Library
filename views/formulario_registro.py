from tkinter import *
from centrar import *
from controllers.crud import *
from tkinter import messagebox

class Formulario:
    def __init__(self):
        self.obj_crud = Crud()
        self.obj_centrar = Centro()
        self.getVentana()
        self.ventana_formulario.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")

        #Objeto canvas
        self.canvas = Canvas(self.ventana_formulario,bg="#ffffff",height=600,width=1000,
        bd=0,highlightthickness=0,relief="ridge")
        self.canvas.place(x=0, y=0)
        #Backgroud
        background_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/background.png")
        background = self.canvas.create_image(500.0, 300.0,image=background_img)

        ###################################################################################
        #Entrys
        #Caja nombre
        entry0_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry0_bg = self.canvas.create_image(502.5, 202.0, image=entry0_img)
        self.nombre = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0,font=("Arial", 14))
        self.nombre.place(x=389.0, y=182, width=227.0, height=38)
        #Caja apellido
        entry1_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry1_bg = self.canvas.create_image(502.5, 276.0, image=entry1_img)
        self.apellido = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0,font=("Arial", 14))
        self.apellido.place(x=389.0, y=256, width=227.0, height=38)
        # Caja usuario
        entry2_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry2_bg = self.canvas.create_image(502.5, 353.0, image=entry2_img)
        self.usuario = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0,font=("Arial", 14))
        self.usuario.place(x=389.0, y=333, width=227.0, height=38)
        # Caja contrasena
        entry3_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry3_bg = self.canvas.create_image(502.5, 426.0, image=entry3_img)
        self.contrasena = Entry(self.ventana_formulario,bd=0, bg="#ffffff",
                                highlightthickness=0, font=("Arial", 14), show="*")
        self.contrasena.place(x=389.0, y=406, width=227.0, height=38)
        ###################################################################################

        #Button
        img0 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img0.png")
        self.registrarte = Button(self.ventana_formulario,image=img0, borderwidth=0, highlightthickness=0,
                                  relief="flat", bg="#D0B8A4", command=self.enviarFormulario)
        self.registrarte.place(x=432, y=500, width=135, height=51)

        #self.getEntry()
        #self.getButton()
        self.ventana_formulario.mainloop()

    def getVentana(self):
        self.ventana_formulario = Toplevel()
        self.ventana_formulario.title("Formulario de registro")
        self.obj_centrar.centrar_ventana(self.ventana_formulario, 600, 1000)
        #self.ventana_formulario.geometry("1000x600")
        self.ventana_formulario.configure(bg="#ffffff")
        self.ventana_formulario.resizable(0,0)

    def getEntry(self):
        #Caja nombre
        entry0_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry0_bg = self.canvas.create_image(502.5, 202.0, image=entry0_img)
        self.nombre = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0)
        self.nombre.place(x=389.0, y=182, width=227.0, height=38)

        #Caja apellido
        entry1_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry1_bg = self.canvas.create_image(502.5, 276.0, image=entry1_img)
        self.apellido = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0)
        self.apellido.place(x=389.0, y=256, width=227.0, height=38)

        #Caja usuario
        entry2_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry2_bg = self.canvas.create_image(502.5, 353.0, image=entry2_img)
        self.usuario = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0)
        self.usuario.place(x=389.0, y=333, width=227.0, height=38)

        #Caja contrasena
        entry3_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img_textBox0.png")
        entry3_bg = self.canvas.create_image(502.5, 426.0, image=entry3_img)
        self.contrasena = Entry(self.ventana_formulario,bd=0, bg="#ffffff", highlightthickness=0)
        self.contrasena.place(x=389.0, y=406, width=227.0, height=38)

    def getButton(self):
        img0 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Formulario/img0.png")
        self.registrarte = Button(self.ventana_formulario,image=img0, borderwidth=0, highlightthickness=0, relief="flat", bg="#D0B8A4")
        self.registrarte.place(x=432, y=518, width=135, height=51)

    def enviarFormulario(self):
        tupla = (self.nombre.get(), self.apellido.get(), self.usuario.get(),  self.contrasena.get())
        obj = self.obj_crud.createUsers(tupla)
        if obj != None:
            messagebox.showinfo("Registro de usuario", "El usuario ha sido ingresado correctamente!")
            self.accionVolver()
        elif obj == None:
            messagebox.showinfo("Error", "Lo sentimos hubo un error, por favor intentelo de nuevo")


    def accionVolver(self):
        self.ventana_formulario.destroy()















