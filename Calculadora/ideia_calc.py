from tkinter import *


# def calculadora():
def pegar_valores(valor):
    numero = ''
    numero = numero.join(valor)

    print(numero)

janela = Tk()
janela.title('Calculadora')
janela.geometry('400x500')

texto_janela = Label(janela, borderwidth=3)
texto_janela.grid(column=0, row=0, padx=5, pady=5)

um = Button(janela, text='1', command=pegar_valores('1'))
um.grid(column=0, row=1, padx=10, pady=10)

dois = Button(janela, text='2', command='')
dois.grid(column=0, row=2, padx=10, pady=10)

tres = Button(janela, text='3', command='')
tres.grid(column=0, row=3, padx=10, pady=10)

quatro = Button(janela, text='4', command='')
quatro.grid(column=1, row=1, padx=10, pady=10)

cinco = Button(janela, text='5', command='')
cinco.grid(column=1, row=2, padx=10, pady=10)

seis = Button(janela, text='6', command='')
seis.grid(column=1, row=3, padx=10, pady=10)

sete = Button(janela, text='7', command='')
sete.grid(column=2, row=1, padx=10, pady=10)

oito = Button(janela, text='8', command='')
oito.grid(column=2, row=2, padx=10, pady=10)

nove = Button(janela, text='9', command='')
nove.grid(column=2, row=3, padx=10, pady=10)

ponto = Button(janela, text='.', command='')
ponto.grid(column=0, row=4, padx=10, pady=10)

zero = Button(janela, text='0', command='')
zero.grid(column=1, row=4, padx=10, pady=10)

igual = Button(janela, text='=', command='')
igual.grid(column=2, row=4, padx=10, pady=10)

mais = Button(janela, text='+', command='')
mais.grid(column=3, row=1, padx=10, pady=10)

menos = Button(janela, text='-', command='')
menos.grid(column=3, row=2, padx=10, pady=10)

divisao = Button(janela, text='/', command='')
divisao.grid(column=3, row=3, padx=10, pady=10)

multiplicacao = Button(janela, text='*', command='')
multiplicacao.grid(column=3, row=4, padx=10, pady=10)

janela.mainloop()
