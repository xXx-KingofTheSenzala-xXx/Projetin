# Objetivos - criar um sistema de livraria que tenha entrada de livros, remocao, emprestivo e devolucao.
# Formatacao: por obsequio para padronizar as variaveis quando for
# variavel int iNomeDaVariavel
# variavel float flNomeDaVariavel
# variavel string strNomeDaVariavel
# variavel list lNomeDaVariavel
# variavel dict dNomeDaVariavel
# variavel constante ou seja nao pode alterar o valor NOMEDAVARIAVEL
# variavel bool ou seja nao pode alterar o valor bNomeDaVariavel

# Para fazer;
# braia: mano bora por essa porra pra exportar e importar a variavel Livraria.

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

def LimparConsole( ):
    # braia: Para que isso?
    # Eu to no linux filho da puta cls nao limpa a porra do console caralho.
    # se o os.name retornar 'nt' quer dizer que voce ta no windows
    # caso retorne posix provavelmente voce esta num sistema baseado no linux.

    # Caso esteja no windows.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

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
    print( f"Nome do livro: { strNomeDoLivro }" )

    # adiciona as informacoes a classe.
    NovoLivro = Livro( strNomeDoLivro, strDataLancada, strGenero )

    # adiciona o livro a lista.
    lLivraria.append( NovoLivro )

    # Debug.
    print( "Adicionar livro pronto!" )

def RemoverLivroNaLivraria( ):
    print( pf.figlet_format( "remover livro" ) )

    # Mostrar os livros que tem ai no role.
    MostrarLivrosNaLivraria( lLivraria )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro" )
        pass

    while True:
        try:
            # Salve a escolha do usuario.
            iEscolha = int( input( "Diga o indice do livro a ser removido do catalogo\n" ) )

            # Check para evitar indices invalidos.
            if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
                print( "Por favor coloque um dos indices listado" )
                continue
            
            # Remova o livro.
            lLivraria.pop( iEscolha )

            # Ja atingimos nosso objetivo pare o loop.
            break
        
        except Exception as e:
            # Pare o loop caso seja solicitado um interrupt ( CTRL + C ).
            if KeyboardInterrupt == e:
                break

            print("Por favor coloque um numero")         

def EmprestarLivroNaLivraria( ):
    print(pf.figlet_format("Emprestar livro"))
    
    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro" )
        pass

    # Parte do emprestimo.
    while True:

        # braia: Por que try?
        # Bom isso e para se o usuario por qualquer coisa exceto numero que tenha no range da lista
        # o script nao crashar.
        try:
            # Salve a escolha do usuario.
            iEscolha = int( input( "Escolha o indice do livro que deseja pegar emprestado ou digite -1 para sair \n" ) )
            
            # Nosso usuario deseja sair.
            if iEscolha == -1:
                break
            
            # Check para evitar indices invalidos.
            if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
                print( "Por favor coloque um dos indices listado" )
                continue

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
            
            # Se acontecer outra coisa.
            print("Por favor digite um numero")

def DevolverLivroNaLivraria( ):
    print(pf.figlet_format( "Devolver livro" ) )

    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro" )
        pass

    # Parte da devolucao.
    while True:

        # braia: Por que try?
        # Bom isso e para se o usuario por qualquer coisa exceto numero que tenha no range da lista
        # o script nao crashar.
        try:
            # Salve a escolha do usuario.
            iEscolha = int( input( "Escolha o indice do livro que deseja devolver ou digite -1 para sair\n" ) )

            # Nosso usuario deseja sair.
            if iEscolha == -1:
                break
            
            # Check para evitar indices invalidos.
            if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
                print( "Por favor coloque um dos indices listado" )
                continue

            # Verifique se esse livro nao foi emprestado se nao foi nao rode o resto.
            if not lLivraria[ iEscolha ].bEmprestado:
                print( f"Este livro ja esse livro nao foi emprestado" )
                continue
            
            # Salve o usuario que talvez tinha pego o livro.
            strNomeDeQuemTalvezTenhaPegadoEmprestado = input( "Digite o nome de quem vai devolver o livro \n" )
            
            # Verifique se foi esse usuario que pegou emprestado.
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
            
            # Se acontecer outra coisa.
            print("Por favor digite um numero")

while True:
    print( pf.figlet_format( "livraria do leo" ) )
    print( "1.adicionar livro                  2.remover livro\n3.emprestimo de livro              4.devolver\n\n\n" )
    escolha = int( input( "" ) )

    # Adicionar livro
    if escolha == 1:
        LimparConsole( )
        AdicionarLivroNaLivraria( )

    # Remover livro    
    elif escolha == 2:
        LimparConsole( )
        RemoverLivroNaLivraria( )

    # emprestar livro    
    elif escolha == 3:
        LimparConsole( )
        EmprestarLivroNaLivraria( )

    # devolver livro    
    elif escolha == 4:
        LimparConsole( )
        DevolverLivroNaLivraria( )

    elif escolha == 0:
        break
    
    else:
        print("numero invalido")
        tm.sleep(2)
        continue
    








