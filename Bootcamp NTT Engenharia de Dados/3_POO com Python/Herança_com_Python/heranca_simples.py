class Veiculo:
    def __init__(self, cor, placa, numero_rodas, motor_ligado = False):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.motor_ligado = motor_ligado
    
    def ligar_motor(self):
        if self.motor_ligado:
            print("O motor ja esta ligado.")
        else:
            print("Ligando o motor.")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, motor_ligado=False, carregado=True):
        super().__init__(cor, placa, numero_rodas, motor_ligado)
        self.carregado = carregado
    
    def esta_carregado(self):
        if self.carregado:
            print("Carregado.")
        else:
            print("Descarregado.")


moto = Motocicleta("Prata", "csa458", 2)
moto.ligar_motor()

carro = Carro("Branco", "bge879", 4)
carro.ligar_motor()

caminhao = Caminhao("Vermelho", "gfr879", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto)
print(carro)
print(caminhao)