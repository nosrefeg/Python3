class Carro:
    def __init__(self, marca='Tesla', cor='azul', eletrico='Sim'):
        self.marca = marca
        self.cor = cor
        self.eletrico = eletrico
        self.velocidade = 0

    def ligar(self):
        print('Ligando o carro agora!')
        print('-' * 30)

    def controlarVelocidade(self, aumento=1):
        self.velocidade += aumento
        if aumento > 0:
            print(f'Acelerando... {self.velocidade} Km/H')
        elif aumento < 0:
            print(f'Reduzindo... {self.velocidade} Km/H')
        else:
            print(f'Velocidade constante de {self.velocidade} Km/H')
        print('-' * 30)

    def ativarAutoPilot(self, cmd=False):
        self.cmd = cmd
        if self.cmd:
            print('Piloto automático ativado!')
        else:
            print('Piloto automático desativado!')
        print('-' * 30)

    def info(self):
        print(
            f'Marca: {self.marca}\nCor: {self.cor}\nElétrico: {self.eletrico}')


car = Carro(cor='Preto')
car.ligar()
car.controlarVelocidade(2)
car.controlarVelocidade(4)
car.controlarVelocidade(2)
car.controlarVelocidade(8)
car.controlarVelocidade(10)
car.controlarVelocidade(5)
car.controlarVelocidade(0)
car.ativarAutoPilot(True)
car.info()
