from tkinter import *
from centrar import *
from controllers.crud import *
from tkinter import messagebox

class Editar:
    def __init__(self,obj_usuario):
        self.obj_crud = Crud()
        self.credenciales = obj_usuario
        self.obj_usuario = self.obj_crud.getAuthSettings(self.credenciales.nombre,self.credenciales.apellido)

        self.obj_centrar = Centro()
        self.getVentana()
        self.ventana_editar.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")

        #Objeto canvas
        canvas = Canvas(self.ventana_editar, bg="#ffffff", height=600, width=1000, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        #Background
        background_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Editar/background.png")
        background = canvas.create_image(433.0, 300.0, image=background_img)

        ###################################################################################
        #Entrys
        #Imagen de la caja de texto/Usuario
        entry0_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Editar/img_textBox0.png")
        entry0_bg = canvas.create_image(500.0, 334.0, image=entry0_img)
        #Usuario
        self.usuarioactual = StringVar()
        self.usuarioactual.set(f"{self.obj_usuario.usuario}")
        self.new_user = Entry(self.ventana_editar,bd=0, bg="#ffffff",
                       highlightthickness=0,font=("Arial", 14),textvariable=self.usuarioactual)
        self.new_user.place(x=364.0, y=313, width=272.0, height=42)
        #Imagen de la caja de texto/Contrasena
        entry1_img = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Editar/img_textBox1.png")
        entry1_bg = canvas.create_image(500.0, 429.0, image=entry1_img)
        #Contrasena
        self.contraactual = StringVar()
        self.contraactual.set(f"{self.obj_usuario.contrasena}")
        self.new_passw = Entry(self.ventana_editar,bd=0, bg="#ffffff",
                       highlightthickness=0,font=("Arial", 14),textvariable=self.contraactual)
        self.new_passw.place(x=364.0, y=408, width=272.0, height=42)
        ###################################################################################

        #Button guardar
        img0 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Editar/img0.png")
        self.guardar = Button(self.ventana_editar,image=img0, borderwidth=0,
                              highlightthickness=0, relief="flat", bg="#FFFFFF",command=self.editarUsuario)
        self.guardar.place(x=432, y=496, width=135, height=51)

        #Button volver
        img1 = PhotoImage(file=f"C:/Users/PC/Pictures/Virtual Library/graphic_resources/Editar/img1.png")
        b1 = Button(self.ventana_editar,image=img1, borderwidth=0, highlightthickness=0,
                    relief="flat", bg="#FFFFFF", command=self.accionVolver)
        b1.place(x=884, y=48, width=50, height=50)

        self.ventana_editar.mainloop()

    def getVentana(self):
        self.ventana_editar = Toplevel()
        self.ventana_editar.title("Editar perfil")
        self.obj_centrar.centrar_ventana(self.ventana_editar, 600, 1000)
        self.ventana_editar.resizable(0, 0)

    def accionVolver(self):
        self.ventana_editar.destroy()

    def editarUsuario(self):
        tupla = (self.obj_usuario.nombre,self.obj_usuario.apellido,self.new_user.get(),self.new_passw.get(),self.obj_usuario.usuario)
        obj_usuario = self.obj_crud.updateUsers(tupla)
        if obj_usuario != None:
            messagebox.showinfo("Editar perfil", "Los datos se actualizaron correctamente!")
            self.ventana_editar.destroy()
        elif obj_usuario == None:
            messagebox.showinfo("Error", "Lo sentimos hubo un error, intentalo nuevamente")

