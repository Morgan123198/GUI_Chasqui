from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from matplotlib.backends._backend_tk import FigureCanvasTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt

class Producto:

    def __init__(self, root):
        self.wind=root
        self.wind.title("Cubesat Educativo - Chasqui II")
        self.wind.geometry("800x600")
        self.wind.iconbitmap("icono_chasqui_transformed.ico")
        #Confiracion del fondo
        imagen_fondo=Image.open("fondo3.png")
        imagen_fondo=imagen_fondo.resize((2100,1000))
        imagen_fondo_tk=ImageTk.PhotoImage(imagen_fondo)
        lb_img_fondo=Label(self.wind, image=imagen_fondo_tk)
        lb_img_fondo.place(x=-2,y=0)
        self.imagen_fondo_tk=imagen_fondo_tk
        #Configuracion de la latitud
        latitud=-68.5
        str_latitud=f"{latitud}"
        #Configuracion de la longitud
        longitud=-16.4
        str_longitud=f"{longitud}"
        #Configuracion de los datos del entry3 para bateria
        nivel_bateria=85
        str_bateria=f"{nivel_bateria}%"
        #Crear entrys 
        entry1=ttk.Entry(root,state="readonly")
        entry1.place(x=250, y=130)
        entry1.config(state=NORMAL,font=("Calibri", 14,),justify="center",foreground="blue")
        entry1.insert(0, str_latitud)
        entry1.config(state="readonly")

        entry2=ttk.Entry(state="readonly")
        entry2.place(x=250, y=160)
        entry2.config(state=NORMAL, font=("Calibri", 14),justify="center",foreground="blue")
        entry2.insert(0, str_longitud)
        entry2.config(state="readonly")

        entry3=ttk.Entry(state="readonly")
        entry3.place(x=250, y=190)
        entry3.config(state=NORMAL, font=("Calibri", 14),justify="center",foreground="blue")
        entry3.insert(0, str_bateria)
        entry3.config(state="readonly")

        #Crear labels
        text0=Label(root,font=("Calibri", 20) ,text="UNIVERSIDAD NACIONAL DE INGENIERÍA",bg='black',fg='white')
        text0.pack(fill="both", expand="yes")
        text0.place(x=130,y=37)
        text1=Label(root,font=("Calibri", 18) ,text="Proyecto Chasqui II",bg='black',fg='white')
        text1.pack(fill="both", expand="yes")
        text1.place(x=130,y=67)
        text1=Label(root,font=("Calibri", 30) ,text="CubeSat Educativo",bg='black',fg='white')
        text1.pack(fill="both", expand="yes")
        text1.place(x=800,y=50)
        text2=Label(root,font=("Calibri", 14) ,text="Latitud:",bg='black',fg='white')
        text2.pack(fill="both", expand="yes")
        text2.place(x=130,y=130)
        text3=Label(root,font=("Calibri", 14) ,text="Longitud:",bg='black',fg='white')
        text3.pack(fill="both", expand="yes")
        text3.place(x=130,y=160)
        text4=Label(root,font=("Calibri", 14) ,text="Nivel de bateria:",bg='black',fg='white')
        text4.pack(fill="both", expand="yes")
        text4.place(x=130,y=190)
        text5=Label(root,font=("Times", 14) ,text="By: Sara Choque",bg='black',fg='white')
        text5.pack(fill="both", expand="yes")
        text5.place(x=1780,y=950)

        img_org1=Image.open("logo_uni.png")
        img_red1=img_org1.resize((108,135))
        img_org2=Image.open("logo_chasqui_1.jpg")
        img_red2=img_org2.resize((130,120))
        #Cargar y mostrar imagenes
        self.imagen1=ImageTk.PhotoImage(img_red1)
        lb_img1=ttk.Label(root,image=self.imagen1,background='black')
        lb_img1.pack()
        lb_img1.place(x=12,y=12)
        self.imagen2=ImageTk.PhotoImage(img_red2)
        lb_img2=ttk.Label(root,image=self.imagen2)
        lb_img2.pack()
        lb_img2.place(x=1768,y=25)
        #creacion de labels
        frame1=LabelFrame(self.wind, text=" XYZ Magnetometer ", font=("Consolas 20 bold", 14,),bg="Black",fg="white",relief="groove", bd=2, labelanchor='n')
        frame2=LabelFrame(self.wind, text=" Altitud ", font=("Consolas 20 bold", 14,),bg="Black",fg="white",relief="groove", bd=2, labelanchor='n' )
        frame3=LabelFrame(self.wind, text=" Temperatura ", font=("Consolas 20 bold", 14,),bg="Black",fg="white",relief="groove", bd=2, labelanchor='n')
        frame4=LabelFrame(self.wind, text=" Orientacion XYZ ", font=("Consolas 20 bold", 14,),bg="Black",fg="white",relief="groove", bd=2, labelanchor='n')
        frame5=LabelFrame(self.wind, text=" INFORMACIÓN GENERAL ", font=("Consolas 20 bold", 14,),bg="Black",fg="white",relief="groove", bd=2, labelanchor='n' )
        frame6=LabelFrame(self.wind, text=" Raw Telemetry ", font=("Consolas 20 bold", 14,),bg="Black",fg="white",relief="groove", bd=2, labelanchor='n' )

        frame1.place(x=101, y=225, width=450, height=300)
        frame2.place(x=560, y=225, width=450, height=300)
        frame3.place(x=101, y=550, width=460, height=330)
        frame4.place(x=1020, y=225, width=450, height=300)
        frame5.place(x=1480, y=225, width=410, height=600)
        frame6.place(x=580, y=550, width=870, height=330)
        #crear y configurar grafico de XYZ magnetometer
        fig1, ax1=plt.subplots()
        x=[0,1,2,3,4,5]
        y1 = [0, 2, 4, 6, 8, 10]
        y2 = [0, 1, 2, 3, 4, 5]
        y3 = [10, 8, 6, 4, 2, 0]
        ax1.plot(x, y1, label='X', color='r')
        ax1.plot(x, y2, label='Y', color='g')
        ax1.plot(x, y3, label='Z', color='b')
        ax1.legend()
        ax1.set_facecolor('white')
        canvas = FigureCanvasTkAgg(fig1, master=frame1)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        #grafico de orientacion XYZ
        fig4, ax4=plt.subplots()
        x2=[0,1,2,3,4,5]
        y4 = [0, 2, 4, 6, 8, 10]
        y5 = [0, 1, 2, 3, 4, 5]
        y6 = [10, 8, 6, 4, 2, 0]
        ax4.plot(x2, y4, label='X', color='r')
        ax4.plot(x2, y5, label='Y', color='g')
        ax4.plot(x2, y6, label='Z', color='b')
        ax4.legend()
        ax4.set_facecolor('white')
        canvas4 = FigureCanvasTkAgg(fig4, master=frame4)
        canvas4.draw()
        canvas4.get_tk_widget().pack(fill="both", expand=True)
        #grafico de la altitud
        fig2, ax2=plt.subplots()
        ax2.set_facecolor('white')
        canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill="both", expand=True)
        #grafico de temperatura
        fig3, ax3=plt.subplots()
        ax3.set_facecolor('white')
        ax3.set_xlabel("Tiempo (s)", color='black')
        ax3.set_ylabel("Grados (°C)", color='black')
        #ax3.tick_params(direction='out',Lenght=6)
        canvas3 = FigureCanvasTkAgg(fig3, master=frame3)
        canvas3.draw()
        canvas3.get_tk_widget().pack(fill="both", expand=True)
        #añadir texto al frame5
        lbl_inf1=Label(frame5, text="Battery Voltage", font=("Calibri", 12), fg='white',bg='black')
        lbl_inf1.place(x=0,y=0)
        lbl_inf1.pack()
        #Creacion de botones para actualizar y descargar la data
        btn_update = Button(self.wind, text="Actualizar", command=self.update_data, font=("Arial",16), bg='lightblue')
        btn_update.place(x=800, y=900)

        btn_download = Button(self.wind, text="Descargar Data", command=self.download_data, font=("Arial",16), bg='lightblue')
        btn_download.place(x=990, y=900)

#funciones para los botones de actualizar y descargar data
    def update_data(self):
        # Código para actualizar los datos
        #...
        print("Actualizando datos...")
    def download_data(self):
        # Código para descargar los datos en una base de datos
        #...
        print("Descargando datos...")
if __name__== '__main__':
        root=Tk()
        product = Producto(root)
        root.mainloop()

