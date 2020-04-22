from tkinter import *
from tkinter import messagebox

#   Autor: Marcelo da Silva
#   Email: umadosedeprogramacao@gmail.com
#   Cria a classe MyInterface, para gerar a janela principal do programa que
#   calcula o valor percentual de lucro.

class MyInterface:

    #   Construtor
    def __init__(self,jan):

        photo = PhotoImage(file="calcular.png")

        self.lblTitulo = Label(jan, text="Calculo do Lucro Percentual", fg='red', font=("Helvetica", 16))
        self.lblTitulo.place(x=10, y=20)

        self.lblcusto = Label(jan, text="Preço de Custo(R$)", fg='black', font=("Helvetica", 14))
        self.lblcusto.place(x=10, y=85)

        self.txtPrecoCusto = Entry(jan, bd=0, font=("Helvetica", 14))
        self.txtPrecoCusto.place(x=200, y=85)

        self.lblvenda = Label(jan, text="Preço de Venda(R$)", fg='black', font=("Helvetica", 14))
        self.lblvenda.place(x=10, y=115)

        self.txtPrecoVenda = Entry(jan, bd=0, font=("Helvetica", 14))
        self.txtPrecoVenda.place(x=200, y=115)

        self.btnCalcular = Button(jan,text="Calcular",fg='blue', command=self.calcularPercentualDeLucro)
        self.btnCalcular.place(x=200, y=160)

    #   Método para Calcular o percentual
    def calcularPercentualDeLucro(self):

        if (self.txtPrecoCusto.get() == ""):
            messagebox.showinfo("Information", "Preencha o campo Preco de Custo")
            return

        if (self.txtPrecoVenda.get() == ""):
            messagebox.showinfo("Information", "Preencha o campo Preco de Venda")
            return


        valorcusto = float(self.txtPrecoCusto.get())
        valorvenda = float(self.txtPrecoVenda.get())

        #calcula a diferença de preço e calcula a porcentagem de lucro
        valoramais = valorvenda - valorcusto
        percentagemdelucro = (valoramais / valorcusto) * 100

        #messagebox.showerror("Error", "Error message")
        #messagebox.showwarning("Warning", "Warning message")
        messagebox.showinfo("Information", f"A porcentagem de Lucro é de: {percentagemdelucro}")



