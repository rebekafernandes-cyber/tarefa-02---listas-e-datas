from datetime import datetime, timedelta
class Treino:
    def __init__(self, id, data, distancia, tempo):
        self._id = id
        self._data = data
        self._distancia = distancia
        self._tempo = tempo
    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id
    def get_data(self):
        return self._data
    def set_data(self, data):
        self._data = data
    def get_distancia(self):
        return self._distancia
    def set_distancia(self, distancia):
        self._distancia = distancia
    def get_tempo(self):
        return self._tempo
    def set_tempo(self, tempo):
        self._tempo = tempo
    
    def pace(self):
        if self._distancia <= 0:
            return timedelta(0)
        tempo_medio = self._tempo.total_seconds() / self._distancia
        return timedelta(seconds=tempo_medio)
    def __str__(self):
        pace = self.pace()
        total_seconds = int(pace.total_seconds())
        pace_min = total_seconds // 60
        pace_sec = total_seconds % 60
        data_str = self._data.strftime("%d/%m/%Y %H:%M")
        return (
            f"ID: {self._id} | "
            f"Data: {data_str} | "
            f"Distância: {self._distancia:.2f} km | "
            f"Tempo: {self._tempo} | "
            f"Pace: {pace_min:02d}:{pace_sec:02d} min/km"
        )
class TreinoUI:
    def __init__(self):
        self.treinos = []
    def Menu(self):
        while True:
            print("MENU TREINO")
            print("1 - Inserir novo treino")
            print("2 - Listar todos os treinos")
            print("3 - Listar treino por ID")
            print("4 - Atualizar treino")
            print("5 - Excluir treino")
            print("6 - Treino mais rápido (menor pace)")
            print("0 - Sair")
            opcao =(input("Escolha uma opção: "))
            if opcao == "1":
                self.Inserir()
            elif opcao == "2":
                self.Listar()
            elif opcao == "3":
                self.Listar_Id()
            elif opcao == "4":
                self.Atualizar()
            elif opcao == "5":
                self.Excluir()
            elif opcao == "6":
                self.MaisRapido()
            elif opcao == "0":
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida.")
    def Inserir(self):
        print("INSERIR TREINO")
        id = int(input("ID: "))
        data = input("Data (dd/mm/aaaa HH:MM): ")
        data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        distancia = float(input("Distância em km: "))
        tempo = float(input("Tempo em minutos: "))
        tempo = timedelta(minutes=tempo)
        treino = Treino(id, data, distancia, tempo)
        self.treinos.append(treino)
        print("Treino inserido com sucesso!")
    def Listar(self):
        print(" TODOS OS TREINOS")
        if len(self.treinos) == 0:
            print("Nenhum treino cadastrado.")
            return
        for treino in self.treinos:
            print(treino)
    def Listar_Id(self):
        print("BUSCAR TREINO")
        id = int(input("Digite o ID do treino: "))
        for treino in self.treinos:
            if treino.get_id() == id:
                print(treino)
                return
        print("Treino não encontrado.")
    def Atualizar(self):
        print("ATUALIZAR TREINO")
        id = int(input("Digite o ID do treino: "))
        for treino in self.treinos:
            if treino.get_id() == id:
                nova_data = input("Nova data (dd/mm/aaaa HH:MM): ")
                nova_data = datetime.strptime(
                    nova_data,
                    "%d/%m/%Y %H:%M"
                )
                nova_distancia = float(
                    input("Nova distância em km: ")
                )
                novo_tempo = float(
                    input("Novo tempo em minutos: ")
                )
                novo_tempo = timedelta(minutes=novo_tempo)
                treino.set_data(nova_data)
                treino.set_distancia(nova_distancia)
                treino.set_tempo(novo_tempo)
                print("Treino atualizado com sucesso!")
                return
        print("Treino não encontrado.")
    def Excluir(self):
        print("EXCLUIR TREINO")
        id = int(input("Digite o ID do treino: "))
        for treino in self.treinos:
            if treino.get_id() == id:
                self.treinos.remove(treino)
                print("Treino excluído com sucesso!")
                return
        print("Treino não encontrado.")
    def MaisRapido(self):
        print("TREINO MAIS RÁPIDO")
        if len(self.treinos) == 0:
            print("Nenhum treino cadastrado.")
            return
        mais_rapido = self.treinos[0]
        for treino in self.treinos:
            if treino.pace() < mais_rapido.pace():
                mais_rapido = treino
        print(mais_rapido)
if __name__ == "__main__":
    app = TreinoUI()
    app.Menu()
