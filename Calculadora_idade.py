#O primeiro passo é importar o tkinter
import tkinter 
from tkinter import *
from tkinter import ttk

# importando tkcalendar
from tkcalendar import Calendar, DateEntry

janela=Tk()
janela.title("Calculadora de idade")
janela.geometry('310x400')

#cores
cor_1="#3b3b3b"#preta leve
cor_2="#333333"#preta forte
cor_3="#ffffff"#cor branca
cor_4="#fcc058"#cor laranja

# Criando frames
frame_cima=Frame(janela,width=310,height=140,pady=0,padx=0,relief=FLAT,bg=cor_2)
frame_cima.grid(row=0,column=0)

frame_baixo=Frame(janela,width=310,height=300,pady=0,padx=0,relief=FLAT,bg=cor_1)
frame_baixo.grid(row=1,column=0)

#criando labels para o frame de cima
l_calculadora=Label(frame_cima,text="Calculadora",width=25,height=1,padx=3,relief=FLAT,anchor='center',font=('Ivy 15 bold'),bg=cor_2,fg=cor_3)
l_calculadora.place(x=0,y=30)
l_idade=Label(frame_cima,text="DE IDADE",width=11,height=1,padx=0,relief=FLAT,anchor='center',font=('Arial 35 bold'),bg=cor_2,fg=cor_4)
l_idade.place(x=0,y=70)

#criando Labels para o frame de baixo
l_data_inicial=Label(frame_baixo,text="Data inicial",height=1,padx=0,pady=0,relief=FLAT,anchor='nw',font=('Ivy 11 '),bg=cor_1,fg=cor_3)
l_data_inicial.place(x=50,y=30)
l_data_nascimento=Label(frame_baixo,text="Data de nascimento",height=1,padx=0,pady=0,relief=FLAT,anchor='nw',font=('Ivy 11 '),bg=cor_1,fg=cor_3)
l_data_nascimento.place(x=50,y=70)

cal_1=DateEntry(frame_baixo, width=13, bg='darkblue',fg=cor_3,borderwith=2,date_patter='mm/dd/yy',y=2023)
cal_1.place(x=170,y=30)

janela.mainloop()