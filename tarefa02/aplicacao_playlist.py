from datetime import datetime
class PlayList:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    def getDescricao(self):
        return self.descricao
    def setDescricao(self, descricao):
        self.descricao = descricao
    def tempoTotal(self, itens, musicas):
        total = 0
        for item in itens:
            if item.getIdPlaylist() == self.id:
                for musica in musicas:
                    if musica.getId() == item.getIdMusica():
                        total += musica.getDuracao()
        return total
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao}"
class Musica:
    def __init__(self, id, titulo, artista, album, duracao):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo
    def getArtista(self):
        return self.artista
    def setArtista(self, artista):
        self.artista = artista
    def getAlbum(self):
        return self.album
    def setAlbum(self, album):
        self.album = album
    def getDuracao(self):
        return self.duracao
    def setDuracao(self, duracao):
        self.duracao = duracao
    def __str__(self):
        minutos = int(self.duracao // 60)
        segundos = int(self.duracao % 60)
        return (
            f"ID: {self.id} | {self.titulo} - {self.artista} | "
            f"Álbum: {self.album} | Duração: {minutos}:{segundos:02d}"
        )
class PlayListItem:
    def __init__(self, id, id_playlist, id_musica, data_inclusao, sequencia):
        self.id = id
        self.id_playlist = id_playlist
        self.id_musica = id_musica
        self.data_inclusao = data_inclusao
        self.sequencia = sequencia
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getIdPlaylist(self):
        return self.id_playlist
    def setIdPlaylist(self, id_playlist):
        self.id_playlist = id_playlist
    def getIdMusica(self):
        return self.id_musica
    def setIdMusica(self, id_musica):
        self.id_musica = id_musica
    def getDataInclusao(self):
        return self.data_inclusao
    def setDataInclusao(self, data_inclusao):
        self.data_inclusao = data_inclusao
    def getSequencia(self):
        return self.sequencia
    def setSequencia(self, sequencia):
        self.sequencia = sequencia
    def __str__(self):
        return (
            f"ID: {self.id} | Playlist: {self.id_playlist} | "
            f"Música: {self.id_musica} | Data: {self.data_inclusao} | "
            f"Sequência: {self.sequencia}"
        )
class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []
    def InserirPlaylist(self):
        print("INSERIR PLAYLIST")
        id = int(input("ID: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        playlist = PlayList(id, nome, descricao)
        self.playlists.append(playlist)
        print("Playlist inserida com sucesso!")
    def ListarPlaylists(self):
        print("PLAYLISTS")
        if len(self.playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return
        for playlist in self.playlists:
            tempo = playlist.tempoTotal(self.itens, self.musicas)
            minutos = int(tempo // 60)
            segundos = int(tempo % 60)
            print(f"{playlist} | Tempo total: {minutos}:{segundos:02d}")
    def AtualizarPlaylist(self):
        print("ATUALIZAR PLAYLIST")
        id = int(input("ID da playlist: "))
        for playlist in self.playlists:
            if playlist.getId() == id:
                playlist.setNome(input("Novo nome: "))
                playlist.setDescricao(input("Nova descrição: "))
                print("Playlist atualizada com sucesso!")
                return
        print("Playlist não encontrada.")
    def ExcluirPlaylist(self):
        print("EXCLUIR PLAYLIST")
        id = int(input("ID da playlist: "))
        for playlist in self.playlists:
            if playlist.getId() == id:
                self.playlists.remove(playlist)
                self.itens = [item for item in self.itens if item.getIdPlaylist() != id]
                print("Playlist excluída com sucesso!")
                return
        print("Playlist não encontrada.")
    def InserirMusica(self):
        print("INSERIR MÚSICA")
        id = int(input("ID: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        duracao = int(input("Duração em segundos: "))
        musica = Musica(id, titulo, artista, album, duracao)
        self.musicas.append(musica)
        print("Música inserida com sucesso!")
    def ListarMusicas(self):
        print("MÚSICAS")
        if len(self.musicas) == 0:
            print("Nenhuma música cadastrada.")
            return
        for musica in self.musicas:
            print(musica)
    def AtualizarMusica(self):
        print("ATUALIZAR MÚSICA")
        id = int(input("ID da música: "))
        for musica in self.musicas:
            if musica.getId() == id:
                musica.setTitulo(input("Novo título: "))
                musica.setArtista(input("Novo artista: "))
                musica.setAlbum(input("Novo álbum: "))
                musica.setDuracao(int(input("Nova duração em segundos: ")))
                print("Música atualizada com sucesso!")
                return
        print("Música não encontrada.")
    def ExcluirMusica(self):
        print("EXCLUIR MÚSICA ")
        id = int(input("ID da música: "))
        for musica in self.musicas:
            if musica.getId() == id:
                self.musicas.remove(musica)
                self.itens = [item for item in self.itens if item.getIdMusica() != id]
                print("Música excluída com sucesso!")
                return
        print("Música não encontrada.")
    def InserirItem(self):
        print("ADICIONAR MÚSICA À PLAYLIST")
        id = int(input("ID do item: "))
        id_playlist = int(input("ID da playlist: "))
        id_musica = int(input("ID da música: "))
        data_inclusao = input("Data de inclusão (dd/mm/aaaa): ")
        sequencia = int(input("Sequência da música: "))
        playlist_existe = False
        musica_existe = False
        for playlist in self.playlists:
            if playlist.getId() == id_playlist:
                playlist_existe = True
        for musica in self.musicas:
            if musica.getId() == id_musica:
                musica_existe = True
        if not playlist_existe:
            print("Playlist não encontrada.")
            return
        if not musica_existe:
            print("Música não encontrada.")
            return
        item = PlayListItem(id, id_playlist, id_musica, data_inclusao, sequencia)
        self.itens.append(item)
        print("Música adicionada à playlist com sucesso!")
    def ListarItens(self):
        print("ITENS DAS PLAYLISTS")

        if len(self.itens) == 0:
            print("Nenhum item cadastrado.")
            return
        for item in self.itens:
            print(item)
    def ListarItensDePlaylist(self):
        print(" MÚSICAS DE UMA PLAYLIST ")
        id_playlist = int(input("ID da playlist: "))
        encontrou = False
        for item in self.itens:
            if item.getIdPlaylist() == id_playlist:
                encontrou = True
                for musica in self.musicas:
                    if musica.getId() == item.getIdMusica():
                        print(f"{item.getSequencia()} - {musica}")
        if not encontrou:
            print("Nenhuma música encontrada nessa playlist.")
    def AtualizarItem(self):
        print("ATUALIZAR ITEM")
        id = int(input("ID do item: "))
        for item in self.itens:
            if item.getId() == id:
                item.setIdPlaylist(int(input("Novo ID da playlist: ")))
                item.setIdMusica(int(input("Novo ID da música: ")))
                item.setDataInclusao(input("Nova data (dd/mm/aaaa): "))
                item.setSequencia(int(input("Nova sequência: ")))
                print("Item atualizado com sucesso!")
                return
        print("Item não encontrado.")
    def ExcluirItem(self):
        print("EXCLUIR ITEM")
        id = int(input("ID do item: "))
        for item in self.itens:
            if item.getId() == id:
                self.itens.remove(item)
                print("Item excluído com sucesso!")
                return
        print("Item não encontrado.")
    def Menu(self):
        while True:
            print(" MENU PLAYLIST ")
            print("1 - Inserir playlist")
            print("2 - Listar playlists")
            print("3 - Atualizar playlist")
            print("4 - Excluir playlist")
            print("5 - Inserir música")
            print("6 - Listar músicas")
            print("7 - Atualizar música")
            print("8 - Excluir música")
            print("9 - Adicionar música à playlist")
            print("10 - Listar itens")
            print("11 - Listar músicas de uma playlist")
            print("12 - Atualizar item")
            print("13 - Excluir item")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.InserirPlaylist()
            elif opcao == "2":
                self.ListarPlaylists()
            elif opcao == "3":
                self.AtualizarPlaylist()
            elif opcao == "4":
                self.ExcluirPlaylist()
            elif opcao == "5":
                self.InserirMusica()
            elif opcao == "6":
                self.ListarMusicas()
            elif opcao == "7":
                self.AtualizarMusica()
            elif opcao == "8":
                self.ExcluirMusica()
            elif opcao == "9":
                self.InserirItem()
            elif opcao == "10":
                self.ListarItens()
            elif opcao == "11":
                self.ListarItensDePlaylist()
            elif opcao == "12":
                self.AtualizarItem()
            elif opcao == "13":
                self.ExcluirItem()
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida.")
if __name__ == "__main__":
    app = UI()
    app.Menu()
