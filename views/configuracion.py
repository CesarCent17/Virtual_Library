from tkinter import *
from centrar import *
from views.editar_perfil import *
from controllers.crud import *
import sys
from tkinter import messagebox
from views.creditos import *


class Configuracion:
    def __init__(self, obj_usuario):
        self.obj_crud = Crud()
        self.credenciales = obj_usuario
        self.obj_usuario = self.obj_crud.getAuthSettings(self.credenciales.nombre, self.credenciales.apellido)
        self.obj_centrar = Centro()
        self.getVentana()
        self.ventana_config.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")

        #Objeto canvas
        canvas = Canvas(self.ventana_config,bg="#ffffff",height=600,width=1000,bd=0,highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)

        #Background
        background_img = PhotoImage(file=f"C:/Users/PC\Pictures/Virtual Library/graphic_resources/Configuracion/background.png")
        background = canvas.create_image(414.0, 300.0,image=background_img)

        ###################################################################################
        #Buttons
        #Eliminar cuenta
        img0 = PhotoImage(file=f"C:/Users/PC\Pictures/Virtual Library/graphic_resources/Configuracion/eliminarcuenta.png")
        self.eliminar_cuenta = Button(self.ventana_config,image=img0,borderwidth=0,
                                      highlightthickness=0,relief="flat", bg="#9E7877", command=self.getDialogo)
        self.eliminar_cuenta.place(x=371, y=318,width=257,height=81)
        #Editar perfil
        img1 = PhotoImage(file=f"C:/Users/PC\Pictures/Virtual Library/graphic_resources/Configuracion/editarperfil.png")
        self.editar_perfil = Button(self.ventana_config,image=img1,borderwidth=0,highlightthickness=0,
                                    relief="flat", bg="#9E7877", command=self.editarP)
        self.editar_perfil.place(x=371, y=200,width=257,height=81)
        #Volver
        img2 = PhotoImage(file=f"C:/Users/PC\Pictures/Virtual Library/graphic_resources/Configuracion/volver.png")
        self.volver = Button(self.ventana_config,image=img2,borderwidth=0,highlightthickness=0,
                             relief="flat", bg="#6E4C5C", command=self.accionVolver)
        self.volver.place( x=884, y=51,width=50,height=50)

        #Creditos
        img3 = PhotoImage(file=f"C:/Users/PC\Pictures/Virtual Library/graphic_resources/Configuracion/img3.png")
        self.creditos = Button(self.ventana_config,image=img3, borderwidth=0, highlightthickness=0, command=self.getCreditos, relief="flat")
        self.creditos.place(x=858, y=537, width=115, height=42)
        ###################################################################################

        self.ventana_config.mainloop()

    def getVentana(self):
        self.ventana_config = Toplevel()
        self.ventana_config.title("Configuracion")
        self.obj_centrar.centrar_ventana(self.ventana_config, 600, 1000)
        self.ventana_config.resizable(0, 0)

    def accionVolver(self):
        self.ventana_config.destroy()

    def editarP(self):
        obj = Editar(self.credenciales)

    def getDialogo(self):
        self.dialog = Toplevel()
        self.dialog.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")
        self.obj_centrar.centrar_ventana(self.dialog, 200, 500)
        self.dialog.title("Eliminar cuenta")
        self.dialog.resizable(0, 0)
        self.dialog.config(bg="#FFFFFF")
        mensaje = "¿Estás seguro? Si aceptas se cerrará el programa y\n" \
                  "se eliminará definitivamente tu cuenta"
        lb1 = Label(self.dialog, text=mensaje, bg="#FFFFFF", font=("Arial", 14))
        lb1.place(x=23, y=25)
        self.cancelar = Button(self.dialog, relief="flat", text="Cancelar", bg="#6E4C5C", font=("Arial", 14),
                          fg="white",command=self.dialog.destroy).place(x=270, y=100, width=110,height=40)

        self.eliminar = Button(self.dialog, relief="flat", text="Eliminar", bg="#6E4C5C", font=("Arial", 14),
                               fg="white",command=self.eliminarCuenta).place(x=130, y=100, width=110,height=40)
        self.dialog.mainloop()

    def eliminarCuenta(self):
        booleano = self.obj_crud.deleteUsers(self.obj_usuario.usuario,self.obj_usuario.contrasena)
        if booleano == 1:
            #self.ventana_menu.destroy()
            messagebox.showinfo("Eliminar cuenta", "Cuenta eliminada correctamente!")
            sys.exit()
        elif booleano == 0:
            messagebox.showinfo("Error", "Ocurrió un error al tratar de eliminar la cuenta")

    def getCreditos(self):
        obj = Creditos()


