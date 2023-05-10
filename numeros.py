import sys
import os
import random
from sqlite3 import Row
from tkinter import *
from tkinter import ttk


cor_background = "#98fa89"
cor_play = "#39a5f7"

janela =Tk()
janela.title("Numbers")
janela.geometry("300x400")
janela.config(bg=cor_background)

frame1 = Frame(janela, width=300, height=65, bg=cor_background)
frame1.grid(row=0, column=0)

frame2 = Frame(janela, width=300, height=50, bg=cor_background)
frame2.grid(row=1, column=0)

frame3 = Frame(janela, width=300, height=60, bg=cor_background)
frame3.grid(row=3, column=0)

frame4 = Frame(janela, width=300, height=65,bg=cor_background )
frame4.grid(row=4, column=0)

frame5 = Frame(janela,width=300, height=100, bg=cor_background)
frame5.grid(row=5, column=0)

numero_escolhido = 0
print(numero_escolhido)

maior = "O número escolhido\né maior que seu palpite"
menor = "O número escolhido\né menor que seu palpite"
acertou = "Você acertou o numero escolhido\nParabéns"
erro = "Insira somente números"


numeros = range(1000)


def escolher():
    app_label0.pack_forget()
    numero_maior.pack_forget()
    numero_menor.pack_forget()
    ganhou.pack_forget()
    error.pack_forget()
    botão_play.pack_forget()
    global numero_escolhido
    numero_escolhido = random.choice(numeros)
    print(numero_escolhido)
    app_label1.pack(side=RIGHT)
    entrada_palpite.pack(side=RIGHT)
    botão_vai.pack(padx=120, pady=20)
    botão_restart.forget()
    
app_label0 = Label(frame1, text="Esse mini-game consiste em\ntentar acertar um número de 0 a 100\n que foi escolhido por um sorteador\nBoa sorte!", bg=cor_background, relief=FLAT, anchor="center", font=('Ivy 12'))
app_label0.pack(pady=20)
app_label1 = Label(frame2, text="O número foi escolhido\nDigite seu palpite", bg=cor_background, relief=FLAT, anchor="center", font=('Ivy 15'))
numero_maior = Label(frame5, text=maior, bg=cor_background, relief=FLAT, anchor="center", font=('Ivy 15'))
numero_menor = Label(frame5, text=menor, bg=cor_background, relief=FLAT, anchor="center", font=('Ivy 15'))
ganhou = Label(frame5, text=acertou, bg=cor_background, relief=FLAT, anchor="center", font= ("Ivy 15") )
error = Label(frame5, text=erro, bg=cor_background, relief=FLAT, anchor="center", font= ("Ivy 15") )
entrada_palpite = Entry(frame3, width=5, font=("Ivy 20"))

botão_play = Button(frame2, command= escolher, text="PLAY", width=10, height=2, bg=cor_play, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão_play.pack(pady=20)

def exibe():
    numero_maior.pack_forget()
    numero_menor.pack_forget()
    ganhou.pack_forget()
    if int(entrada_palpite.get()) < numero_escolhido:
        numero_maior.pack()
    if int(entrada_palpite.get()) > numero_escolhido:
        numero_menor.pack()
    if int(entrada_palpite.get()) == numero_escolhido:
        ganhou.pack()
        botão_restart.pack(pady=20)
    entrada_palpite.delete(0,END)
    
    

botão_vai = Button(frame4, command= exibe,text= "Vai", bg=cor_play, relief=RAISED, overrelief=RIDGE, anchor="center", font=('Ivy 15'))
botão_restart = Button(frame5, command= escolher,text= "restart", bg=cor_play, relief=RAISED, overrelief=RIDGE, anchor="c", font=('Ivy 15'))
 
janela.mainloop()
