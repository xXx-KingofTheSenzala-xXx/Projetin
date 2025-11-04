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
# bom hoje no dia 03/11/2025 tivemos um papo com nosso cliente.
# sera necessario exportacao para um planilha excel.
# restricoes de livros por idade.( feito )
# restricoes para livros que nao possuem muitas unidades ex:
# tem 15 livros iguais 3 deles nao podem ser retirados
# ou tem so um exemplar logo ele nao pode ser emprestado. ( feito )
# codigo para cada livro. ( feito )
# por variavel de qual estante e. ( feito )

# bibliotecas importadas
import pyfiglet as pf
import numpy as np
import os
import datetime as dt
import time as tm
import random

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
        strDisplayDoLivro: str = f"{ i } - { LivroAtual.strNomeDoLivro } - Genero: { LivroAtual.strGenero } - Idade Minima: { LivroAtual.iIdadeMinima } - Marcacao: { LivroAtual.strRestricao } - Prateleira: { LivroAtual.iPrateleira } - Codigo: { LivroAtual.strCodigoDoLivro }"

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

def GerarCodigoUnico( Livraria: list, nTamanho: int ):
    while True:
        # Gere o codigo.
        strCodigo: str = ''.join( random.choices( "1234567890abcdefghijklmnopqrstuvwxyz", k = nTamanho ) ).upper( )

        bUnico = True

        # Check para ver se ja tem algo livro com o mesmo codigo.
        for i in Livraria:
            LivroAtual: Livro = i

            # Se tiver igual roda tudo de novo.
            if LivroAtual.strCodigoDoLivro == strCodigo:
                bUnico = False

        # Esse codigo e unico nao rode dnv.
        if bUnico:
            break

    return strCodigo

def InputDeInteiro( strEntrada: str ):
    # Para que isso?, para eu poupar tempo lel.
    iValorDeRetorno = 0

    while True:
        try:
            iValorDeRetorno = int( input( strEntrada ) )
            break
        except:
            print( "Por favor coloque um numero" )

    return iValorDeRetorno

def InputDeRestricao( strEntrada: str ):
    # Uh, pelo oq vi da conversa do leo, o xandao e a tamires( nao e minha ex e a bibliotecaria nao fode porra ).
    # sera feito assim, restricao vermelha nao podera ser emprestado
    # verde podera ser emprestado.
    strSaida = ""

    while True:
        strSaida = input( strEntrada )
        if strSaida == "vermelho" or strSaida == "Vermelho":
            break
        elif strSaida == "verde" or strSaida == "Verde":
            break
        else:
            print( "Essa palavra nao esta no catalogo de restricao" )

    return strSaida.capitalize( )

lLivraria: list = [ ]

class Livro:
    def __init__( self, NomeDoLivro, Genero, IdadeMinima, Restricao, Prateleira ):
        self.strNomeDoLivro: str = NomeDoLivro
        self.strGenero: str = Genero
        self.bEmprestado: bool = False
        self.strQuemAdquiriu: str = ""
        self.strDataEmprestada: str = ""
        self.strCodigoDoLivro: str = GerarCodigoUnico( lLivraria, 6 )
        self.iIdadeMinima: int = IdadeMinima
        self.strRestricao: str = Restricao
        self.iPrateleira: int = Prateleira

    def Emprestar( self, NomeDeQuemAdquiriu: str, IdadeDeQuemAdquiriu: int ):
        if not self.bEmprestado and IdadeDeQuemAdquiriu >= self.iIdadeMinima and self.strRestricao != "Vermelho":
            self.strQuemAdquiriu: str = NomeDeQuemAdquiriu
            self.strDataEmprestada: str = tempo( )
            self.bEmprestado: bool = True
            return True

        elif IdadeDeQuemAdquiriu < self.iIdadeMinima:
            print( "A fachetaria desse livro nao e permitido para esse aluno" )
            return False

        elif self.strRestricao:
            print( "Esse livro nao e emprestavel" )
            return False

        # Debug
        print( "Esse livro ja foi emprestado" )
        return False

    def Devolver( self, NomeDeQuemAdquiriu: str ):
        if self.bEmprestado and self.strQuemAdquiriu == NomeDeQuemAdquiriu:
            self.strQuemAdquiriu: str = ""
            self.bEmprestado: bool = False
            return True

        elif self.strQuemAdquiriu != NomeDeQuemAdquiriu:
            print( "Nao foi esse usuario que pegou emprestado" )
            return False

        # Debug
        print( "Esse livro ja foi devolvido" )
        return False

def AdicionarLivroNaLivraria( ):
    print( pf.figlet_format( "Adicionar livro" ) )
    strNomeDoLivro = input( "Diga o nome do livro: " )
    strGenero = input( "Diga o genero do livro: " )
    iIdadeMinima = InputDeInteiro( "Diga a idade minima para adquirir o livro: " )
    strRestricao = InputDeRestricao( "Diga qual restricao esse livro possui se e vermelho ou verde: " )
    iPrateleira = InputDeInteiro( "Diga qual prateleira esse livro pertence: " )

    # adiciona as informacoes a classe.
    NovoLivro = Livro( strNomeDoLivro, strGenero, iIdadeMinima, strRestricao, iPrateleira )

    # adiciona o livro a lista.
    lLivraria.append( NovoLivro )

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

    # Para o loop broski.
    bPare = False

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

            # Salve o usuario que vai pegar emprestado o livro.
            strNomeDeQuemVaiPegarEmprestado = input( "Digite o nome de quem vai pegar emprestado \n" )

            # Salve a idade do usuario que vai pegar emprestado o livro.
            iIdadeDeQuemVaiPegarEmprestado = InputDeInteiro( "Digite a idade de quem vai pegar emprestado \n" )

            # Rode a funcao dur.
            bPare = lLivraria[ iEscolha ].Emprestar( strNomeDeQuemVaiPegarEmprestado, iIdadeDeQuemVaiPegarEmprestado )

            # Pare o loop ja atingimos nosso objeto.
            if bPare:
                break

        except Exception as e:
            # Pare o loop caso seja solicitado um interrupt ( CTRL + C ).
            if KeyboardInterrupt == e:
                break

            # Se acontecer outra coisa.
            print("Por favor digite um numero")

def DevolverLivroNaLivraria( ):
    print( pf.figlet_format( "Devolver livro" ) )

    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro" )
        pass

    # Pare o loop broski.
    bPare = False

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

            # Salve o usuario que talvez tinha pego o livro.
            strNomeDeQuemTalvezTenhaPegadoEmprestado = input( "Digite o nome de quem vai devolver o livro \n" )

            # Rode a funcao dur.
            bPare = lLivraria[ iEscolha ].Devolver( strNomeDeQuemTalvezTenhaPegadoEmprestado )

            # Pare o loop ja atingimos nosso objeto.
            if bPare:
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

    try:
        # Salve a escolha do usuario.
        iEscolha = int( input( "" ) )

        match iEscolha:
            # Sair do Script.
            case 0:
                break

            # Adicionar livro na livraria.
            case 1:
                LimparConsole( )
                AdicionarLivroNaLivraria( )

            # Remover livro na livraria.
            case 2:
                LimparConsole( )
                RemoverLivroNaLivraria( )

            # Emprestar livro na livraria.
            case 3:
                LimparConsole( )
                EmprestarLivroNaLivraria( )

            # Devolver livro na livraria.
            case 4:
                LimparConsole( )
                DevolverLivroNaLivraria( )

            # Caso se o numero nao for nenhum dos anteriores.
            case _:
                # braia: por o default: do python e case _ que porra e essa.
                print( "Numero invalido tente novamente" )
                tm.sleep( 2 )

    except Exception as e:
        if KeyboardInterrupt == e:
            break

        print( "Digite um numero por favor" )
