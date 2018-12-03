from errbot import BotPlugin, botcmd, botmatch
import pymongo

class FilmesBot(BotPlugin):
    'Programacao de filmes'

    @botcmd
    def start(self, msg, args):
        yield "Em qual shopping?"
        yield "/Continente_Park_Shopping"
        yield "/Shopping_Itaguacu"
        yield "/Shopping_Via_Catarina"
        yield "/Beira_Mar_Shopping"
        yield "/Floripa_Shopping"
        yield "/Shopping_Iguatemi"

    @botcmd
    def filmes(self, msg, args):
        yield "Em qual shopping?"
        yield "/Continente_Park_Shopping"
        yield "/Shopping_Itaguacu"
        yield "/Shopping_Via_Catarina"
        yield "/Beira_Mar_Shopping"
        yield "/Floripa_Shopping"
        yield "/Shopping_Iguatemi"

    @botcmd
    def Continente_Park_Shopping(self, msg, args):
        yield "Os filmes disponiveis neste shopping sao:"
        yield "/O_Grinch"
        yield "/Bohemian_Rhapsody"
        yield "/Parque_do_inferno"

    @botcmd
    def Shopping_Itaguacu(self, msg, args):
        yield "Os filmes disponiveis neste shopping sao:"
        yield "/O_Grinch"
        yield "/De_repente_uma_familia"
        yield "/Parque_do_inferno"

    @botcmd
    def Shopping_Via_Catarina(self, msg, args):
        yield "Os filmes disponiveis neste shopping sao:"
        yield "/O_Grinch"
        yield "/Animais_Fantasticos_os_crimes_de_Grindelwald"
        yield "/Bohemian_Rhapsody"

    @botcmd
    def Beira_Mar_Shopping(self, msg, args):
        yield "Os filmes disponiveis neste shopping sao:"
        yield "/Sueno_Florianopolis"
        yield "/Bohemian_Rhapsody"
        yield "/Entrevista_com_Deus"

    @botcmd
    def Floripa_Shopping(self, msg, args):
        yield "Os filmes disponiveis neste shopping sao:"
        yield "/Bohemian_Rhapsody"
        yield "/Animais_Fantasticos_os_crimes_de_Grinderlwald"
        yield "/O_Grinch"

    @botcmd
    def Shopping_Iguatemi(self, msg, args):
        yield "Os filmes disponiveis neste shopping sao:"
        yield "/Nasce_uma_estrela"
        yield "/Animais_Fantasticos_os_crimes_de_Grinderlwald"
        yield "/Entrevista_com_Deus"

    @botcmd
    def O_Grinch(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "O Grinch"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_O_Grinch'

    @botcmd
    def Sinopse_O_Grinch(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "O Grinch"})
        yield resultado['sinopse']

    @botcmd
    def Parque_do_inferno(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Parque do inferno"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_Parque_do_inferno'

    @botcmd
    def Sinopse_Parque_do_inferno(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Parque do inferno"})
        yield resultado['sinopse']
    
    @botcmd
    def De_repente_uma_familia(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "De repente uma família"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_De_repente_uma_familia' 

    @botcmd
    def Sinopse_De_repente_uma_familia(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "De repente uma família"})
        yield resultado['sinopse']

    @botcmd
    def Bohemian_Rhapsody(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Bohemian Rhapsody"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_Bohemian_Rhapsody'

    @botcmd
    def Sinopse_Bohemian_Rhapsody(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Bohemian Rhapsody"})
        yield resultado['sinopse']

    @botcmd
    def Animais_Fantasticos_os_crimes_de_Grindelwald(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Animais Fantásticos: os crimes de Grindelwald"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_Animais_Fantasticos_os_crimes_de_Grindelwald'

    @botcmd
    def Sinopse_Animais_Fantasticos_os_crimes_de_Grindelwald(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Animais Fantásticos: os crimes de Grindelwald"})
        yield resultado['Sinopse']

    @botcmd
    def Sueno_Florianopolis(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Sueño Florianópolis"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_Sueno_Florianopolis'

    @botcmd
    def Sinopse_Sueno_Florianopolis(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Sueño Florianópolis"})
        yield resultado['Sinopse']

    @botcmd
    def Entrevista_com_Deus(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Entrevista com Deus"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_Entrevista_com_Deus'

    @botcmd
    def Sinopse_Entrevista_com_Deus(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Entrevista com Deus"})
        yield resultado['Sinopse']

    @botcmd
    def Nasce_uma_estrela(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Nasce Uma Estrela"})
        yield 'Nome: ' + resultado['nome']
        yield 'Genero: ' + resultado['genero']
        yield 'Classificacao: ' + resultado['classificacao']
        yield 'Duracao: ' + resultado['duracao']
        yield 'Elenco: ' + resultado['elenco']
        yield 'Trailer: ' + resultado['trailer']
        yield '/Sinopse_Nasce_uma_estrela'

    @botcmd
    def Sinopse_Nasce_uma_estrela(self, msg, args):
        cliente = pymongo.MongoClient().filmes_db.Filmes
        resultado = cliente.find_one({"nome": "Nasce Uma Estrela"})
        yield resultado['Sinopse']

