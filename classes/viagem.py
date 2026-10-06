from datetime import datetime

class Viagem:
    """
    Representa uma viagem realizada pela frota.

    Mantém a relação entre um motorista e um veículo,
    além das informações referentes à origem, destino,
    distância e data da viagem.
    """

    def __init__(
        self,
        motorista,
        veiculo,
        origem,
        destino,
        distancia,
        data
    ):
        self.__motorista = motorista
        self.__veiculo = veiculo
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia
        self.__data = data

    @property
    def motorista(self):
        return self.__motorista

    @motorista.setter
    def motorista(self, valor):
        self.__motorista = valor

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, valor):
        self.__veiculo = valor

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, valor):
        self.__origem = valor

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, valor):
        self.__destino = valor

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, valor):
        if valor < 0:
            raise ValueError("A distância não pode ser negativa.")

        self.__distancia = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor
