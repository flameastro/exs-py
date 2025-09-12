# ex161: Classe Agenda: parâmetros -> dono; Funções -> adicionar_compromisso(), listar_crompromissos()
class Agenda:
    def __init__(self, dono):
        self.dono = dono
        self.compromissos = []

    def adicionar_compromisso(self, compromisso, data):
        self.compromissos.append([compromisso, data])
        print("Compromisso adicionado com sucesso")

    def listar_compromissos(self):
        for lista_compromisso in self.compromissos:
            print(", ".join(lista_compromisso))


if __name__ == "__main__":
    agenda = Agenda("Gabriel")
    agenda.adicionar_compromisso("Ir à NASA", "14:30")
    agenda.listar_compromissos()
