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
import time as tm
import colorama as cl
import os

# arquivos locais importados.
import Utils
import BaseLivraria

ESTAGIOPADRAO = 0
ESTAGIOMOSTRARSOMENTEEMPRESTAVEL = 1
ESTAGIOMOSTRARESCOLHIDO = 2
ESTAGIOMOSTRAREMPRESTADOS = 3

lLivraria: list = [ ]

def AdicionarLivroNaLivraria( ):
    bPare = False

    while True:
        print( pf.figlet_format( "Adicionar livro" ) )
        strNomeDoLivro = input( "Diga o nome do livro: " )
        Utils.LimparConsole( )
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print(f"Nome: { strNomeDoLivro }")
        strGenero = input( "Diga o genero do livro: " )
        Utils.LimparConsole( )
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print( f"Nome: { strNomeDoLivro }" )
        print( f"Genero: { strGenero }" )
        iIdadeMinima = Utils.InputDeIdadeMinima( "Diga a idade minima para adquirir o livro( L  10   12   14   16   18 ): " )
        Utils.LimparConsole( )
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print( f"Nome: { strNomeDoLivro }" )
        print( f"Genero: { strGenero }" )
        print( f"Classificação: { iIdadeMinima }" )
        strRestricao = Utils.InputDeRestricao( "Diga qual restricao esse livro possui se e vermelho ou verde: " )
        Utils.LimparConsole( )

        print( pf.figlet_format( "Adicionar livro" ) )
        print( f"Nome: { strNomeDoLivro }" )
        print( f"Genero: { strGenero }" )
        print( f"Classificação: { iIdadeMinima }" )
        print( f"Restrição : { strRestricao }" )
        iPrateleira = Utils.InputDeInteiro( "Diga qual prateleira esse livro pertence: " )
        Utils.LimparConsole( )
        
        print( pf.figlet_format( "Adicionar livro" ) )
        print( f"Nome: { strNomeDoLivro }" )
        print( f"Genero: { strGenero }" )
        print( f"Classificação: { iIdadeMinima }" )
        print( f"Restrição : { strRestricao }" )
        print( f"Pratileira: { iPrateleira }" )

        while True:

            # Salve a escolha do usuario, o upper( ) e para padronizar.
            strEscolha = input( "\n ta certo? ( Y/N ) " ).upper( )

            if strEscolha == "N":
                Utils.LimparConsole( )
                break
            elif strEscolha == "Y":
                bPare = True
                break
            else:
                print( "Opções invalida" )
                continue
        
        if bPare:
            break

    # adiciona as informacoes a classe.
    NovoLivro = BaseLivraria.Livro( strNomeDoLivro, strGenero, False, "-", "-", BaseLivraria.GerarCodigoUnico( lLivraria, 6 ), iIdadeMinima, strRestricao, iPrateleira )

    # adiciona o livro a lista.
    lLivraria.append( NovoLivro )

def RemoverLivroNaLivraria( ):
    print( pf.figlet_format( "remover livro" ) )

    # Mostrar os livros que tem ai no role.
    BaseLivraria.MostrarLivrosNaLivraria( lLivraria )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "A livraria ta vazia, por favor adicione algum livro." )
        input( "Aperte 'ENTER' para continuar" )
        return

    # Salve a escolha do usuario.
    iEscolha = Utils.InputDeInteiro( "Diga o numero do livro a ser removido do catalogo.\n" )

    # Check para evitar indices invalidos.
    if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
        print( "Por favor coloque um dos numeros listado." )
        return

    # Remova o livro.
    lLivraria.pop( iEscolha )

def EmprestarLivroNaLivraria( ):
    print(pf.figlet_format("Emprestar livro"))

    # Mostre os livros que tem na livraria.
    BaseLivraria.MostrarLivrosNaLivraria( lLivraria, ESTAGIOMOSTRARSOMENTEEMPRESTAVEL )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "nenhum livro aqui.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )
        input( "Aperte 'ENTER' para continuar" )
        return
    
    # Nao tem nenhum livro para ser emprestado.
    if not BaseLivraria.TemLivrosParaEmprestar( lLivraria ):
        print( "nenhum livro para emprestar.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )
        input( "Aperte 'ENTER' para continuar" )
        return

    # Para o loop broski.
    bPare = False

    # Parte do emprestimo.
    while True:

        # Salve a escolha do usuario.
        iEscolha = Utils.InputDeInteiro( "Escolha o indice do livro que deseja pegar emprestado. (digite -1 para sair) \n" )
        
        # Nosso usuario deseja sair.
        if iEscolha == -1:
            break

        # Check para evitar indices invalidos.
        if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
            print( "Por favor coloque um dos numeros listado." )
            continue
        
        LivroAtual: BaseLivraria.Livro = lLivraria[ iEscolha ]

        # Check se o livro nao foi emprestado.
        if LivroAtual.bEmprestado:
            print( "Esse livro ja foi emprestado" )
            continue

        # Salve o usuario que vai pegar emprestado o livro.
        strNomeDeQuemVaiPegarEmprestado = input( "Digite o nome de quem vai pegar emprestado: \n" )

        # Salve a idade do usuario que vai pegar emprestado o livro.
        iIdadeDeQuemVaiPegarEmprestado = Utils.InputDeInteiro( "Digite a idade de quem vai pegar emprestado: \n" )

        # Rode a funcao dur.
        bPare = lLivraria[ iEscolha ].Emprestar( strNomeDeQuemVaiPegarEmprestado, iIdadeDeQuemVaiPegarEmprestado )

        # Pare o loop ja atingimos nosso objeto.
        if bPare:
            break

def DevolverLivroNaLivraria( ):
    print( pf.figlet_format( "Devolver livro" ) )

    # Mostre os livros que tem na livraria.
    BaseLivraria.MostrarLivrosNaLivraria( lLivraria, ESTAGIOMOSTRAREMPRESTADOS )

    # Pegue o tamanho da lista
    iTamanhoDaLivraria = len( lLivraria )

    # A lista ta vazia os codigos abaixo serao inuteis.
    if iTamanhoDaLivraria <= 0:
        print( "nenhum livro aqui.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )
        input( "Aperte 'ENTER' para continuar" )
        return
    
    # Nao tem nenhum livro para ser emprestado.
    if not BaseLivraria.TemLivrosParaDevolver( lLivraria ):
        print( "nenhum livro para devolver.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" )
        input( "Aperte 'ENTER' para continuar" )
        return

    # Pare o loop broski.
    bPare = False

    # Parte da devolucao.
    while True:
            
        # Salve a escolha do usuario.
        iEscolha = Utils.InputDeInteiro( "Escolha o numero do livro que deseja devolver: (digite -1 para sair)\n" )

        # Nosso usuario deseja sair.
        if iEscolha == -1:
            break

        # Check para evitar indices invalidos.
        if iEscolha < 0 or iEscolha > iTamanhoDaLivraria:
            print( "Por favor coloque um dos numeros listado" )
            continue
        
        LivroAtual: BaseLivraria.Livro = lLivraria[ iEscolha ]

        # Check se o livro nao foi emprestado.
        if not LivroAtual.bEmprestado:
            print( "Esse livro ja nao foi emprestado" )
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
        input( "Aperte 'ENTER' para continuar" )
        return
    
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
        LivroAtual: BaseLivraria.Livro = Livraria[ i ]

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

def ConversaoDeDicionarioParaLista( Livraria: dict ):
    # braia: for real cara acho q fazendo isso perdi 5 anos de vida por tanto estresse sem kao vo me matar.
    # volta pra mim mariana me perdoe por ser um verme cntg

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
    
    # braia: ta? se eu nao me engano isso talvez funcione
    # o dataframe nao e criado se os array la de dentro n tiver o mesmo tamanho
    # entao isso talvez esteja certo xddddddd.
    iTamanhoDaLista = len( Livraria[ lIndicesDoDicionario[ 0 ] ] )

    # cara aquela mulher era gostosa em.
    for i in range( iTamanhoDaLista ):
        LivroAtual : BaseLivraria.Livro = BaseLivraria.Livro( Livraria[ lIndicesDoDicionario[ 0 ] ][ i ],
                                                              Livraria[ lIndicesDoDicionario[ 1 ] ][ i ],
                                                              Livraria[ lIndicesDoDicionario[ 2 ] ][ i ],
                                                              Livraria[ lIndicesDoDicionario[ 3 ] ][ i ],
                                                              Livraria[ lIndicesDoDicionario[ 4 ] ][ i ], 
                                                              Livraria[ lIndicesDoDicionario[ 5 ] ][ i ],
                                                              Livraria[ lIndicesDoDicionario[ 6 ] ][ i ],
                                                              Livraria[ lIndicesDoDicionario[ 7 ] ][ i ], 
                                                              Livraria[ lIndicesDoDicionario[ 8 ] ][ i ] )

        lLivraria.append( LivroAtual )

def ExportacaoParaExcel( ):
    # braia: ta essa funcao pode esta incompleta e mal feita
    # porem deve funcionar lel.

     # Pegue o tamanho da lista.
    iTamanhodaLista = len( lLivraria )

    # Se a lista estiver vazia nao rode essa porra.
    if iTamanhodaLista <= 0:
        print( "O catalogo esta vazio!" )
        input( "Aperte 'ENTER' para continuar" )
        return

    # Vamos salvar essa bosta numa pasta aqui onde o script foi rodado.
    # me lembro disto ser mais dificil.
    strDiretorioAtual = os.getcwd( )

    # Direcione para o diretorio desejado.
    strDiretorioAtual = os.path.join( strDiretorioAtual, "output" )

    # Vamos criar a pasta se nao existir logico e se tiver permissao.
    try:
        os.mkdir( strDiretorioAtual )
    except Exception as e:
        if e == FileExistsError:
            print( "pasta ja criada anteriormente, ignorando funcao de criacao da pasta." )
        
        if e == PermissionError:
            print( "essa pasta nao pode ser criada no diretorio onde se encontra o script, provavelmente essa pasta e restrita para administradores." )

    # Salve o nome desejado para o arquivo.
    strNomeDoArquivo = input( "Qual sera o nome do arquivo? \n" )
    strNomeDoArquivo += ".xlsx"

    # aqui vai ser o diretorio da saida mais o nome do arquivo que vai ser gerado.
    strDiretorioFinal = os.path.join( strDiretorioAtual, strNomeDoArquivo )

    # Converte a lista para dicionario.
    dictLivraria = ConversaoDaListaParaDicionario( lLivraria )
    
    # Conversao da lista livraria para pandas.
    dfEntrada = pd.DataFrame( dictLivraria )

    # Exporte isso.
    dfEntrada.to_excel( strDiretorioFinal, index=False )

    print( f"Arquivo excel gerado em: {strDiretorioFinal}" )
    input( "Aperte 'ENTER' para continuar" )

def ImportacaoParaExcel( ):
    # braia: cara isso deu uma dor de cabeca q vc n ta ligado.

    # Cara isso ficou mt foda taaaaa?
    strCaminhoParaOArquivoExcel = Utils.BusqueOArquivo( )

    if strCaminhoParaOArquivoExcel == "":
        print("Diretorio nao selecionado, retornando...")
        return
    
    # braia: uma pequena observacao, eu tenho ctz se por a caso corromper o arquivo isso ai vai pro krl.

    # Parte da leitura do arquivo excel.
    ArquivoExcel = pd.read_excel( strCaminhoParaOArquivoExcel )

    # Parte da conversao para dicionario, o orient='list' e para usar lista
    # no dicionario vai ser mais facil para converter novamente para a classe.
    dictConversaoParaDictionario = ArquivoExcel.to_dict( orient='list' )

    # Como toda lista nesse dicionario tem o mesmo tamanho provavel que isso de certo.
    ConversaoDeDicionarioParaLista( dictConversaoParaDictionario )

    input( "Aperte 'ENTER' para continuar" )

def OperacoesEmExcel( ):
    # Cara sinceramente nao sei oq dizer.

    print( "O que voce deseja?" )
    print( "1 - Exportar" )
    print( "2 - Importar" )

    while True:
        # Salve a escolha.
        iEscolha = Utils.InputDeInteiro( "" )

        match iEscolha:
            case 1:
                ExportacaoParaExcel( )
                break
            case 2:
                ImportacaoParaExcel( )
                break
            case _:
                print( "Numero fora da lista de escolha" )

while True:
    Utils.LimparConsole( )
    print(cl.Fore.CYAN + pf.figlet_format( "                            livraria do                                          Leleo          " ) )
    print( "                                              0.Sair\n                       1.Adicionar livro                  2.Remover livro\n\n                       3.Emprestimo de livro              4.Devolver\n\n                                              5.Excel\n" )

    try:
        # Salve a escolha do usuario.
        iEscolha = int( input( "" ) )

        match iEscolha:
            # Sair do Script.
            case 0:
                Utils.LimparConsole( )
                break

            # Adicionar livro na livraria.
            case 1:
                Utils.LimparConsole( )
                AdicionarLivroNaLivraria( )

            # Remover livro na livraria.
            case 2:
                Utils.LimparConsole( )
                RemoverLivroNaLivraria( )

            # Emprestar livro na livraria.
            case 3:
                Utils.LimparConsole( )
                EmprestarLivroNaLivraria( )

            # Devolver livro na livraria.
            case 4:
                Utils.LimparConsole( )
                DevolverLivroNaLivraria( )

            # Sistema de exportacao.
            case 5:
                Utils.LimparConsole( )
                OperacoesEmExcel( )

            # Caso se o numero nao for nenhum dos anteriores.
            case _:
                # braia: por o default: do python e case _ que porra e essa.
                print( "Numero invalido tente novamente" )
                tm.sleep( 1 )

    except Exception as e:
        if KeyboardInterrupt == e:
            break
        
        #Utils.LimparConsole( )
        #print( "Digite um numero por favor" )

        #DEBUG;
        print( f"erro: {e}")
        input( "Aperte 'ENTER' para continuar" )
