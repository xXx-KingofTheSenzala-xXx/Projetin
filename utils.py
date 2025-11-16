import os
import wx

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

def BusqueOArquivo( ):
   # Initialize the wx application
    app = wx.App( False )

    # Open a file dialog
    wxFileDialog = wx.FileDialog( None, "Select a file", wildcard="*.xlsx", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST )

    strCaminhoDoArquivo = ""
    if wxFileDialog.ShowModal( ) == wx.ID_OK:
        strCaminhoDoArquivo = wxFileDialog.GetPath( )

    wxFileDialog.Destroy( )

    return strCaminhoDoArquivo