import random
import datetime as dt

ESTAGIOPADRAO = 0
ESTAGIOMOSTRARSOMENTEEMPRESTAVEL = 1
ESTAGIOMOSTRARESCOLHIDO = 2
ESTAGIOMOSTRAREMPRESTADOS = 3

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

def TempoAtual( ):
    agora = dt.date.today( )
    horas = dt.datetime.now( ).time( )
    horas1 = horas.strftime( "%H:%M" )
    return f"as:{ horas1 } do dia: { agora }"

class Livro:
    def __init__( self, NomeDoLivro: str, Genero: str, IdadeMinima: int, Restricao: str, Prateleira: int , Livraria: list ):
        self.strNomeDoLivro: str = NomeDoLivro
        self.strGenero: str = Genero
        self.bEmprestado: bool = False
        self.strQuemAdquiriu: str = "-"
        self.strDataEmprestada: str = "-"
        self.strCodigoDoLivro: str = GerarCodigoUnico( Livraria, 6 )
        self.iIdadeMinima: int = IdadeMinima
        self.strRestricao: str = Restricao
        self.iPrateleira: int = Prateleira

    def Emprestar( self, NomeDeQuemAdquiriu: str, IdadeDeQuemAdquiriu: int ):
        if not self.bEmprestado and IdadeDeQuemAdquiriu >= self.iIdadeMinima and self.strRestricao != "Vermelho":
            self.strQuemAdquiriu: str = NomeDeQuemAdquiriu
            self.strDataEmprestada: str = TempoAtual( )
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
            self.strQuemAdquiriu: str = "-"
            self.bEmprestado: bool = False
            return True

        elif self.strQuemAdquiriu != NomeDeQuemAdquiriu:
            print( "Não foi esse aluno que pegou emprestado." )
            return False

        # Debug
        print( "Esse livro ja foi devolvido." )
        return False

def MostrarLivrosNaLivraria( Livraria: list, Estagio: int = ESTAGIOPADRAO, IndiceDoEscolhido: int = 0 ):
    iTamanhoDaLivraria = len( Livraria )
    if iTamanhoDaLivraria <= 0:
        return

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
        
        # Nao mostre aqueles que nao foram emprestados
        if Estagio == ESTAGIOMOSTRAREMPRESTADOS and not LivroAtual.bEmprestado:
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

def TemLivrosParaEmprestar( Livraria: list ):
    iTamanhoDaLivraria = len( Livraria )
    if iTamanhoDaLivraria <= 0:
        return False

    # Vamos percorrer a lista agora se ela nao esta vazia.
    for i in range( iTamanhoDaLivraria ):

        # Pegue a classe dentro da lista.
        LivroAtual: Livro = Livraria[ i ]

        # Verifique se tem algum livro para emprestar.
        if not LivroAtual.bEmprestado:
            return True

    return False

def TemLivrosParaDevolver( Livraria: list ):
    iTamanhoDaLivraria = len( Livraria )
    if iTamanhoDaLivraria <= 0:
        return False

    # Vamos percorrer a lista agora se ela nao esta vazia.
    for i in range( iTamanhoDaLivraria ):

        # Pegue a classe dentro da lista.
        LivroAtual: Livro = Livraria[ i ]

        # Verifique se tem algum livro para devolver.
        if LivroAtual.bEmprestado:
            return True

    return False