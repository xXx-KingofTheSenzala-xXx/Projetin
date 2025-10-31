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
    return f"as:{horas1} do dia: {agora}"

def MostrarLivrosNaLivraria( Livraria: list ):
    iTamanhoDaLivraria = len( Livraria )
    if iTamanhoDaLivraria <= 0:
        pass
        
    # Vamos percorrer a lista agora se ela nao esta vazia.
    for i in range( iTamanhoDaLivraria ):

        # Pegue a classe dentro da lista.
        LivroAtual: Livro = Livraria[ i ]

        # Pegue o indice do loop e o livro que o corresponde.
        strDisplayDoLivro: str = f"{ i } - { LivroAtual.strNomeDoLivro }"

        if LivroAtual.bEmprestado:
            strDisplayDoLivro += f" - Emprestado para: { LivroAtual.strQuemAdquiriu } { LivroAtual.strDataLancada }"
            
        # Mostre.
        print( strDisplayDoLivro )

lLivraria: list = [ ]

class Livro:
    def __init__( self, NomeDoLivro, DataLancada, Genero ):
        self.strNomeDoLivro: str = NomeDoLivro
        self.strDataLancada: str = DataLancada
        self.strGenero: str = Genero
        self.bEmprestado: bool = False
        self.strQuemAdquiriu: str = ""

    def Emprestar( self, NomeDeQuemAdquiriu: str ):
        if not self.bEmprestado:
            self.strQuemAdquiriu: str = NomeDeQuemAdquiriu
            self.bEmprestado: bool = True
            return True

        # Debug
        print( "Esse livro ja foi emprestado" )
        return False

    def Devolver( self, NomeDeQuemAdquiriu: str ):
        if self.bEmprestado and self.strQuemAdquiriu == NomeDeQuemAdquiriu:
            self.strQuemAdquiriu: str = ""
            self.bEmprestado: bool = False
            return True

        elif self.strQuemAdquiriu != NomeDeQuemAdquiriu:
            print("Nao foi esse usuario que pegou emprestado")
            return False

        # Debug
        print( "Esse livro ja foi devolvido" )
        return False

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

    # Parte do emprestimo.
    while True:

        # braia: Por que try?
        # Bom isso e para se o usuario por qualquer coisa exceto numero que tenha no range da lista
        # o script nao crashar.
        try:
            # Salve a escolha do usuario.
            iEscolha = int( input( "Escolha o indice do livro que deseja pegar emprestado \n" ) )
            
            # Verifique se esse livro ja foi emprestado nao rode o codigo de emprestamento.
            if lLivraria[ iEscolha ].bEmprestado:
                print( f"Este livro ja foi empretado para: { lLivraria[ iEscolha ].strQuemAdquiriu }" )
                continue
            
            # Salve o usuario que vai pegar emprestado o livro.
            strNomeDeQuemVaiPegarEmprestado = input( "Digite o nome de quem vai pegar emprestado \n" )
            
            # Rode a funcao dur.
            lLivraria[ iEscolha ].Emprestar( strNomeDeQuemVaiPegarEmprestado )
            
            # Pare o loop ja atingimos nosso objeto.
            break

        except Exception as e:
            # Pare o loop caso seja solicitado um interrupt ( CTRL + C ).
            if KeyboardInterrupt == e:
                break
            
            # Caso o numero da escolha nao esteja na lista.
            if IndexError == e:
                print( "Por favor digite um numero que esteja na lista" )

            # Se acontecer outra coisa.
            else:
                print("Por favor digite um numero")

def DevolverLivroNaLivraria( ):
    print(pf.figlet_format( "Devolver livro" ) )

    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria )

    # Parte da devolucao.
    while True:

        # braia: Por que try?
        # Bom isso e para se o usuario por qualquer coisa exceto numero que tenha no range da lista
        # o script nao crashar.
        try:
            # Salve a escolha do usuario.
            iEscolha = int( input( "Escolha o indice do livro que deseja devolver \n" ) )
            
            # Verifique se esse livro nao foi emprestado se nao foi nao rode o resto.
            if not lLivraria[ iEscolha ].bEmprestado:
                print( f"Este livro ja esse livro nao foi emprestado" )
                continue
            
            # Salve o usuario que talvez tinha pego o livro.
            strNomeDeQuemTalvezTenhaPegadoEmprestado = input( "Digite o nome de quem vai devolver o livro \n" )
            
            if strNomeDeQuemTalvezTenhaPegadoEmprestado != lLivraria[ iEscolha ].strQuemAdquiriu:
                print( "Esse usuario nao pegou o livro" )
                continue

            # Rode a funcao dur.
            lLivraria[ iEscolha ].Devolver( strNomeDeQuemTalvezTenhaPegadoEmprestado )
            
            # Pare o loop ja atingimos nosso objeto.
            break

        except Exception as e:
            # Pare o loop caso seja solicitado um interrupt ( CTRL + C ).
            if KeyboardInterrupt == e:
                break
            
            # Caso o numero da escolha nao esteja na lista.
            if IndexError == e:
                print( "Por favor digite um numero que esteja na lista" )

            # Se acontecer outra coisa.
            else:
                print("Por favor digite um numero")

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
    








