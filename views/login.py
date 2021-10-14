from tkinter import *
from centrar import *
from views.menu_principal import *
from views.formulario_registro import *
from controllers.crud import *
from tkinter import messagebox


class Login(Frame):
    def __init__(self):
        self.obj_crud = Crud()
        #Ventana raiz
        self.iniciosesion=Tk()
        self.obj_centrar=Centro()
        self.obj_centrar.centrar_ventana(self.iniciosesion, 600,1000)
        self.iniciosesion.configure(bg="#ffffff")
        self.iniciosesion.iconbitmap("C:/Users/PC/Pictures/Virtual Library/graphic_resources/Virtual Library.ico")
        self.iniciosesion.title("Virtual Library")
        self.iniciosesion.resizable(0,0)

        #Objeto canvas
        canvas = Canvas(self.iniciosesion, bg="#ffffff", height=600, width=1000, bd=0, highlightthickness = 0, relief ="flat")
        canvas.place(x=0, y=0)

        fondo_img = PhotoImage(file="C:/Users/PC/Pictures/Virtual Library/graphic_resources/Login/background.png")
        fondo_bg = canvas.create_image(400,300, image=fondo_img)

        cajausuario_img = PhotoImage(file="C:/Users/PC/Pictures/Virtual Library/graphic_resources/Login/img_textBox0.png")
        cajausuario_bg = canvas.create_image(728, 235.5, image= cajausuario_img)
        self.usuario = Entry(self.iniciosesion,bd=False, bg="#e3e3e3", highlightthickness = False, font=("Arial",14))
        self.usuario.place(x=550.5, y=210, width=355, height=49)

        cajapassword_img = PhotoImage(file="C:/Users/PC/Pictures/Virtual Library/graphic_resources/Login/img_textBox1.png")
        cajapassword_bg = canvas.create_image(728, 336.5, image=cajapassword_img)
        self.password = Entry(self.iniciosesion, bd=False, bg="#e3e3e3", highlightthickness=False, font=("Arial", 14))
        self.password.place(x=550.5, y=311, width=355, height=49)
        self.password.config(show="*")

        cajaentrar_img = PhotoImage(file="C:/Users/PC/Pictures/Virtual Library/graphic_resources/Login/img0.png")
        self.entrar = Button(image= cajaentrar_img, borderwidth=False, bg="#ffffff",
                             highlightthickness = False, relief = "flat", command=self.logeo)
        self.entrar.place(x=660, y=430, width=135, height=51)


        cajaregistrarse_img = PhotoImage(file="C:/Users/PC/Pictures/Virtual Library/graphic_resources/Login/img1.png")
        self.registrarse = Button(image=cajaregistrarse_img, borderwidth=False, bg="#ffffff",
                                  highlightthickness=False, relief="flat", command=self.registrarse)
        self.registrarse.place(x=525, y=481, width=406, height=51)

        #Bucle
        self.iniciosesion.mainloop()

    def logeo(self):
        obj_usuario = self.obj_crud.getAuth(self.usuario.get(),self.password.get())
        if obj_usuario != None:
            self.iniciosesion.wm_state('withdrawn')
            obj = MenuP(obj_usuario)
        elif obj_usuario == None:
            messagebox.showinfo("Error", "Usuario no existe")

    def registrarse(self):
        obj = Formulario()

ejecutar = Login()



