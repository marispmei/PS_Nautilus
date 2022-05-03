class campeonato:
    def __init__(self):
        self.nome1 = "Britney Spares"
        self.pontos1 = 221
        self.jogada1 = 10 #número de jogadas
        self.strike1 = 4 #número de strikes
        self.spare1 = 4 #número de spares
        self.zerada1 = 0 #número de jogadas zeradas (sem acertar nada)

        self.nome2 = "Time Strike"
        self.pontos2 = 201
        self.jogada2 = 10 #número de jogadas
        self.strike2 = 5 #número de strikes
        self.spare2 = 3 #número de spares
        self.zerada2 = 0 #número de jogadas zeradas (sem acertar nada)
        
    def time1(self):
        return print("Nome do time: ", self.nome1, "\nNúmero final de pontos: ", self.pontos1, "\nNúmero de jogadas dadas: ", self.jogada1, "\nNúmero de Strikes dados: ", self.strike1, "\nNúmero de Spares dados: ", self.spare1, "\nNúmero de jogadas zeradas: ", self.zerada1)
    def time2(self):
        return print("Nome do time: ", self.nome2, "\nNúmero final de pontos: ", self.pontos2, "\nNúmero de jogadas dadas: ", self.jogada2, "\nNúmero de Strikes dados: ", self.strike2, "\nNúmero de Spares dados: ", self.spare2, "\nNúmero de jogadas zeradas: ", self.zerada2)
    def resultado(self):
        return "Time 1 - Britney Spares ganhou!"
    def __add__(self):
        return campeonato(self.pontos1 + self.pontos2)
    def __sub__(self):
        return campeonato(self.pontos1 - self.pontos2)
