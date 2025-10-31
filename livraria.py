#   Objetivos - criar um sistema de livraria que tenha entrada de livros, remocao, emprestivo e devolucao.
# Formatacao: por obsequio para padronizar as variaveis quando for
# variavel int iNomeDaVariavel
# variavel float flNomeDaVariavel
# variavel string strNomeDaVariavel
# variavel list lNomeDaVariavel
# variavel dict dNomeDaVariavel
# variavel constante ou seja nao pode alterar o valor NOMEDAVARIAVEL
# variavel bool ou seja nao pode alterar o valor bNomeDaVariavel

# bibliotecas importadas
import pyfiglet as pf
import numpy as np
import os
import datetime as dt
import time as tm

def tempo():
    agora = dt.date.today()
    horas = dt.datetime.now().time()
    horas1 = horas.strftime("%H:%M")
    return(f"Data:{agora}\nHoras:{horas1}")

def MostrarLivrosNaLivraria( Livraria: list ):
    iTamanhoDaLivraria = len( Livraria )
    if iTamanhoDaLivraria <= 0:
        pass
        
    # Vamos percorrer a lista agora se ela nao esta vazia.
    for i in range(iTamanhoDaLivraria):

        # Pegue a classe dentro da lista.
        LivroAtual: Livro = Livraria[i]

        # Pegue o indice do loop e o livro que o corresponde.
        strDisplayDoLivro: str = f"{ i } - { LivroAtual.strNomeDoLivro }"
            
        # Mostre.
        print( strDisplayDoLivro )

lLivraria: list = []

class Livro:
    def __init__( self, NomeDoLivro, DataLancada, Genero ):
        self.strNomeDoLivro: str = NomeDoLivro
        self.strDataLancada: str = DataLancada
        self.strGenero: str = Genero
        self.bEmprestado: bool = False
        self.strQuemAdquiriu: str = ""

    def Emprestar( self, NomeDeQuemAdquiriu ):
        if not self.bEmprestado:
            self.strQuemAdquiriu: str = NomeDeQuemAdquiriu
            self.bEmprestado: bool = True
        else:
            # Debug
            print( "Esse livro ja foi emprestado" )

    def Devolver( self ):
        if self.bEmprestado:
            self.strQuemAdquiriu: str = ""
            self.bEmprestado: bool = False
        else:
            # Debug
            print( "Esse livro ja foi devolvido" ) 

def AdicionarLivroNaLivraria( ):
    print( pf.figlet_format( "Adicionar livro" ) )
    strNomeDoLivro = input( "Diga o nome do livro: " )
    strDataLancada = tempo( )
    strGenero = input( "Diga o genero do livro: " )
    print(f"Nome do livro: {strNomeDoLivro}")

    # adiciona as informacoes a classe.
    NovoLivro = Livro( strNomeDoLivro, strDataLancada, strGenero )

    # adiciona o livro a lista.
    lLivraria.append( NovoLivro )

    # Debug.
    print("Adicionar livro pronto!")

def RemoverLivroNaLivraria( ):
    print(pf.figlet_format("remover livro"))
    # braia: Murilo arruma isso broski.
    #if i in len(lLivraria) > 0:
    #    for i in range(len(lLivraria)):
    #        LivroAtual: Livro = lLivraria[i]
    #        removerlivro = LivroAtual.pop([ii])
    #        strDisplayDoLivro = i + " - " + LivroAtual.strNomeDoLivro
    #        print( strDisplayDoLivro )
            

def EmprestarLivroNaLivraria( ):
    print(pf.figlet_format("Emprestar livro"))
    
    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria )

    # E so pra pausar lel.
    input()
    
#     Agora a parte do emprestimo
#     try:
#         iIndiceDaLista = int
# n
#     except:

def DevolverLivroNaLivraria( ):
   print(pf.figlet_format("Devolver livro"))

while True:
    print(pf.figlet_format("livraria do leo"))
    print("1.adicionar livro                  2.remover livro\n3.emprestimo de livro              4.devolver\n\n\n")
    escolha = int(input(""))

    # Adicionar livro
    if escolha == 1:
        os.system("cls")
        AdicionarLivroNaLivraria()

    # Remover livro    
    elif escolha == 2:
        os.system("cls")
        RemoverLivroNaLivraria()

    # emprestar livro    
    elif escolha == 3:
        os.system("cls")
        EmprestarLivroNaLivraria()

    # devolver livro    
    elif escolha == 4:
        os.system("cls")
        DevolverLivroNaLivraria()
    elif escolha == 0:
        break
    else:
        print("numero invalido")
        tm.sleep(2)
        continue
    








