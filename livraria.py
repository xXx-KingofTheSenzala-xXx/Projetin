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
import pandas as pd
import pyfiglet as pf
import numpy as np
import os
import datetime as dt
import time as tm
import random
import colorama as cl

ESTAGIOPADRAO = 0
ESTAGIOMOSTRARSOMENTEEMPRESTAVEL = 1
ESTAGIOMOSTRARESCOLHIDO = 2

def tempo():
    agora = dt.date.today()
    horas = dt.datetime.now().time()
    horas1 = horas.strftime("%H:%M")
    return f"as:{horas1} do dia: {agora}"

def MostrarLivrosNaLivraria( Livraria: list, Estagio: int = ESTAGIOPADRAO, IndiceDoEscolhido: int = 0 ):
    iTamanhoDaLivraria = len( Livraria )
    if iTamanhoDaLivraria <= 0:
        pass

    # Vamos percorrer a lista agora se ela nao esta vazia.
    for i in range( iTamanhoDaLivraria ):

        # Pegue a classe dentro da lista.
        LivroAtual: Livro = Livraria[ i ]

        # Nao mostre os livros nao emprestaveis
        if Estagio == ESTAGIOMOSTRARSOMENTEEMPRESTAVEL and LivroAtual.strRestricao == "Vermelho":
            continue

        # Nao mostre aqueles fora do indice
        if Estagio == ESTAGIOMOSTRARESCOLHIDO and i != IndiceDoEscolhido:
            continue
        
        strEmojiDeCor = ""
        if LivroAtual.strRestricao == "Verde":
            strEmojiDeCor = "🟩"
        elif LivroAtual.strRestricao == "Vermelho":
            strEmojiDeCor = "🟥"
            
        # Pegue o indice do loop e o livro que o corresponde.
        strDisplayDoLivro: str = f"{ i } - { LivroAtual.strNomeDoLivro } \n Genero: { LivroAtual.strGenero } \n Idade Minima: { LivroAtual.iIdadeMinima } \n Marcacao: { strEmojiDeCor } \n Prateleira: { LivroAtual.iPrateleira } \n Codigo: { LivroAtual.strCodigoDoLivro }\n"

        if LivroAtual.bEmprestado:
            strDisplayDoLivro += f" - Emprestado para: { LivroAtual.strQuemAdquiriu } { LivroAtual.strDataEmprestada }"

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
        except Exception as e:
            if e == KeyboardInterrupt:
                break

            print( "Por favor coloque um numero" )

    return iValorDeRetorno

def InputDeRestricao( strEntrada: str ):
    # Uh, pelo oq vi da conversa do leo, o xandao e a tamires( nao e minha ex e a bibliotecaria nao fode porra ).
    # sera feito assim, restricao vermelha nao podera ser emprestado
    # verde podera ser emprestado.
    strSaida = ""

    while True:

        # Pegue qual e a restricao.
        strSaida = input( strEntrada )

        # Padronize isso.        
        strSaida = strSaida.capitalize( )
        
        if strSaida == "Vermelho":
            break
        elif strSaida == "Verde":
            break
        else:
            print( "Essa palavra não está no catalogo de restrição." )

    return strSaida

def InputDeIdadeMinima( strEntrada: str ):
    # Inicializa a variavel.
    iIdadeMinima = ""

    while True:
        # Input do idade
        iIdadeMinima = input( strEntrada )

        # Padronizar a variavel.
        iIdadeMinima = iIdadeMinima.upper( )

        if iIdadeMinima == "L":
            iIdadeMinima = 0
            break
        elif iIdadeMinima == "10":
            iIdadeMinima = 10
            break
        elif iIdadeMinima == "12":
            iIdadeMinima = 12
            break
        elif iIdadeMinima == "14":
            iIdadeMinima = 14
            break
        elif iIdadeMinima == "16":
            iIdadeMinima = 16
            break
        elif iIdadeMinima == "18":
            iIdadeMinima = 18
            break
        else:
            print("numero invalido")  

    return iIdadeMinima

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
            print( "A faixa etária desse livro não e permitido para esse aluno." )
            return False

        elif self.strRestricao == "Vermelho":
            print( "Esse livro é VERMELHO não pode ser emprestado." )
            return False

        # Debug
        print( "Esse livro ja foi emprestado." )
        return False

    def Devolver( self, NomeDeQuemAdquiriu: str ):
        if self.bEmprestado and self.strQuemAdquiriu == NomeDeQuemAdquiriu:
            self.strQuemAdquiriu: str = ""
            self.bEmprestado: bool = False
            return True

        elif self.strQuemAdquiriu != NomeDeQuemAdquiriu:
            print( "Não foi esse aluno que pegou emprestado." )
            return False

        # Debug
        print( "Esse livro ja foi devolvido." )
        return False

def AdicionarLivroNaLivraria( ):
    bPare = False

    while True:
        if bPare:
            break

        print( pf.figlet_format( "Adicionar livro" ) )
        strNomeDoLivro = input( "Diga o nome do livro: " )
        LimparConsole()
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print(f"Nome: {strNomeDoLivro}")
        strGenero = input( "Diga o genero do livro: " )
        LimparConsole()
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print(f"Nome: {strNomeDoLivro}")
        print(f"Genero: {strGenero}")
        iIdadeMinima = InputDeIdadeMinima( "Diga a idade minima para adquirir o livro( L  10   12   14   16   18 ): " )
        LimparConsole()
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print(f"Nome: {strNomeDoLivro}")
        print(f"Genero: {strGenero}")
        print(f"classificação: {iIdadeMinima}")
        strRestricao = InputDeRestricao( "Diga qual restricao esse livro possui se e vermelho ou verde: " )
        LimparConsole()

        print( pf.figlet_format( "Adicionar livro" ) )
        print(f"Nome: {strNomeDoLivro}")
        print(f"Genero: {strGenero}")
        print(f"classificação: {iIdadeMinima}")
        print(f"restrição : {strRestricao}")
        iPrateleira = InputDeInteiro( "Diga qual prateleira esse livro pertence: " )
        LimparConsole()
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print(f"Nome: {strNomeDoLivro}")
        print(f"Genero: {strGenero}")
        print(f"classificação: {iIdadeMinima}")
        print(f"restrição : {strRestricao}")
        print(f"pratileira: {iPrateleira}")

        while True:
            x = input("\n ta certo?(N/Y)").upper( )
            if x == ("N"):
                LimparConsole()
                break
            elif x == ("Y"):
                bPare = True
                break
            else:
                print("Opções invalida")
                continue

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
        print( "A livraria ta vazia, por favor adicione algum livro." )
        pass

    # Salve a escolha do usuario.
    iEscolha = InputDeInteiro( "Diga o numero do livro a ser removido do catalogo.\n" )

    # Check para evitar indices invalidos.
    if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
        print( "Por favor coloque um dos numeros listado." )
        pass

    # Remova o livro.
    lLivraria.pop( iEscolha )

def EmprestarLivroNaLivraria( ):
    print(pf.figlet_format("Emprestar livro"))

    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria, ESTAGIOMOSTRARSOMENTEEMPRESTAVEL )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro." )
        pass

    # Para o loop broski.
    bPare = False

    # Parte do emprestimo.
    while True:

        # Salve a escolha do usuario.
        iEscolha = InputDeInteiro( "Escolha o indice do livro que deseja pegar emprestado. (digite -1 para sair) \n" )
        

        # Nosso usuario deseja sair.
        if iEscolha == -1:
            break

        # Check para evitar indices invalidos.
        if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
            print( "Por favor coloque um dos numeros listado." )
            continue

        # Salve o usuario que vai pegar emprestado o livro.
        strNomeDeQuemVaiPegarEmprestado = input( "Digite o nome de quem vai pegar emprestado: \n" )

        # Salve a idade do usuario que vai pegar emprestado o livro.
        iIdadeDeQuemVaiPegarEmprestado = InputDeInteiro( "Digite a idade de quem vai pegar emprestado: \n" )

        # Rode a funcao dur.
        bPare = lLivraria[ iEscolha ].Emprestar( strNomeDeQuemVaiPegarEmprestado, iIdadeDeQuemVaiPegarEmprestado )

        # Pare o loop ja atingimos nosso objeto.
        if bPare:
            break

def DevolverLivroNaLivraria( ):
    print( pf.figlet_format( "Devolver livro" ) )

    # Mostre os livros que tem na livraria.
    MostrarLivrosNaLivraria( lLivraria, ESTAGIOMOSTRARSOMENTEEMPRESTAVEL )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro." )
        pass

    # Pare o loop broski.
    bPare = False

    # Parte da devolucao.
    while True:
            
        # Salve a escolha do usuario.
        iEscolha = InputDeInteiro( "Escolha o numero do livro que deseja devolver: (digite -1 para sair)\n" )

        # Nosso usuario deseja sair.
        if iEscolha == -1:
            break

        # Check para evitar indices invalidos.
        if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
            print( "Por favor coloque um dos numeros listado" )
            continue

        # Salve o usuario que talvez tinha pego o livro.
        strNomeDeQuemTalvezTenhaPegadoEmprestado = input( "Digite o nome de quem vai devolver o livro: \n" )

        # Rode a funcao dur.
        bPare = lLivraria[ iEscolha ].Devolver( strNomeDeQuemTalvezTenhaPegadoEmprestado )

        # Pare o loop ja atingimos nosso objeto.
        if bPare:
            break

def ConversaoDaListaParaDicionario( Livraria: list ):
    # Pegue o tamanho da lista.
    iTamanhodaLista = len( Livraria )

    # Se a lista estiver vazia nao rode essa porra.
    if iTamanhodaLista <= 0:
        print( "O catalogo esta vazio!" )
        pass
    
    lIndicesDoDicionario = [
                            "Nome do Livro",
                            "Genero",
                            "Emprestado",
                            "Quem Adquiriu",
                            "Data Emprestada",
                            "Codigo do Livro",
                            "Idade Minima",
                            "Restricao",
                            "Prateleira"
                            ]

    # Conversao da lista para dicionario.
    # Pra evitar dor de cabeca.
    dictLivraria = {
                     "Nome do Livro"   : [],
                     "Genero"          : [],
                     "Emprestado"      : [],
                     "Quem Adquiriu"   : [],
                     "Data Emprestada" : [],
                     "Codigo do Livro" : [],
                     "Idade Minima"    : [],
                     "Restricao"       : [],
                     "Prateleira"      : [],
                   }
    
    for i in range( iTamanhodaLista ):

        # Pegue a classe dentro do catalogo.
        LivroAtual: Livro = Livraria[ i ]

        dictLivraria[ lIndicesDoDicionario[ 0 ] ].append( LivroAtual.strNomeDoLivro )
        dictLivraria[ lIndicesDoDicionario[ 1 ] ].append( LivroAtual.strGenero )
        dictLivraria[ lIndicesDoDicionario[ 2 ] ].append( LivroAtual.bEmprestado )
        dictLivraria[ lIndicesDoDicionario[ 3 ] ].append( LivroAtual.strQuemAdquiriu )
        dictLivraria[ lIndicesDoDicionario[ 4 ] ].append( LivroAtual.strDataEmprestada )
        dictLivraria[ lIndicesDoDicionario[ 5 ] ].append( LivroAtual.strCodigoDoLivro )
        dictLivraria[ lIndicesDoDicionario[ 6 ] ].append( LivroAtual.iIdadeMinima )
        dictLivraria[ lIndicesDoDicionario[ 7 ] ].append( LivroAtual.strRestricao )
        dictLivraria[ lIndicesDoDicionario[ 8 ] ].append( LivroAtual.iPrateleira )
    
    return dictLivraria

def OperacoesEmExcel( ):
    # Cara sinceramente nao sei oq dizer.
    # Conversao da lista livraria para pandas.

    dictLivraria = ConversaoDaListaParaDicionario( lLivraria )
       
    dataframe = pd.DataFrame( dictLivraria )
    print( dataframe )

    #TODO; terminar e por a parte de import

    input("Aperte qualquer tecla para continuar\n")

while True:
    LimparConsole()
    print(cl.Fore.CYAN + pf.figlet_format( "                            livraria do                                          Leleo          " ) )
    print( "                                              0.Sair\n                       1.Adicionar livro                  2.Remover livro\n\n                       3.Emprestimo de livro              4.Devolver\n\n                                              5.Excel\n" )

    try:
        # Salve a escolha do usuario.
        iEscolha = int( input( "" ) )

        match iEscolha:
            # Sair do Script.
            case 0:
                LimparConsole( )
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

            # Sistema de exportacao.
            case 5:
                LimparConsole( )
                OperacoesEmExcel( )

            # Caso se o numero nao for nenhum dos anteriores.
            case _:
                # braia: por o default: do python e case _ que porra e essa.
                print( "Numero invalido tente novamente" )
                tm.sleep( 1 )

    except Exception as e:
        if KeyboardInterrupt == e:
            break
        
        LimparConsole( )
        print( "Digite um numero por favor" )
