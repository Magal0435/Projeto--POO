from datetime import datetime

class Manutencao:
    """
    Representa uma manutenção realizada ou planejada para
    um veículo da frota.
    """

    def __init__(
        self,
        data,
        tipo,
        custo,
        descricao,
        veiculo,
        status
    ):
        self.__data = data
        self.__tipo = tipo
        self.__custo = custo
        self.__descricao = descricao
        self.__veiculo = veiculo
        self.__status = status

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, valor):
        if valor < 0:
            raise ValueError("O custo não pode ser negativo.")

        self.__custo = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, valor):
        self.__veiculo = valor

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        self.__status = valor


class Abastecimento:
    """
    Representa um abastecimento realizado em um veículo da frota.

    Armazena informações sobre data, combustível, quantidade,
    valor pago, veículo abastecido e quilometragem no momento
    do abastecimento.
    """

    def __init__(
        self,
        data,
        tipo_combustivel,
        litros,
        valor_pago,
        veiculo,
        quilometragem
    ):
        self.__data = data
        self.__tipo_combustivel = tipo_combustivel
        self.__litros = litros
        self.__valor_pago = valor_pago
        self.__veiculo = veiculo
        self.__quilometragem = quilometragem

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, valor):
        self.__data = valor

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, valor):
        self.__tipo_combustivel = valor

    @property
    def litros(self):
        return self.__litros

    @litros.setter
    def litros(self, valor):
        if valor < 0:
            raise ValueError("A quantidade de litros não pode ser negativa.")

        self.__litros = valor

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor):
        if valor < 0:
            raise ValueError("O valor pago não pode ser negativo.")

        self.__valor_pago = valor

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, valor):
        self.__veiculo = valor

    @property
    def quilometragem(self):
        return self.__quilometragem

    @quilometragem.setter
    def quilometragem(self, valor):
        if valor < 0:
            raise ValueError(
                "A quilometragem não pode ser negativa."
            )

        self.__quilometragem = valor