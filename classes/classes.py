class ManutenivelMixin:
    """
    Define a capacidade de um veículo possuir e gerenciar
    informações relacionadas a manutenções.
    """
    pass


class AbastecivelMixin:
    """
    Define a capacidade de um veículo possuir e gerenciar
    informações relacionadas a abastecimentos.
    """
    pass


class PessoaBase:
    """
    Classe base para representar uma pessoa no sistema,
    servindo como estrutura comum para diferentes tipos de pessoas.
    """
    pass


class VeiculoBase(ManutenivelMixin, AbastecivelMixin):
    """
    Classe base para representar um veículo da frota.

    Reúne as características comuns aos diferentes tipos de veículos
    e utiliza os mixins ManutenivelMixin e AbastecivelMixin para
    representar as capacidades de manutenção e abastecimento.
    """
    pass


class Carro(VeiculoBase):
    """
    Representa um carro pertencente à frota.

    Herda as características e capacidades definidas pela classe
    VeiculoBase.
    """
    pass


class Moto(VeiculoBase):
    """
    Representa uma motocicleta pertencente à frota.

    Herda as características e capacidades definidas pela classe
    VeiculoBase.
    """
    pass


class Caminhao(VeiculoBase):
    """
    Representa um caminhão pertencente à frota.

    Herda as características e capacidades definidas pela classe
    VeiculoBase.
    """
    pass


class Motorista(PessoaBase):
    """
    Representa um motorista responsável por conduzir veículos
    e realizar viagens dentro do sistema de gerenciamento da frota.
    """
    pass


class Viagem:
    """
    Representa uma viagem realizada pela frota.

    Relaciona um motorista a um veículo e contém as informações
    necessárias para representar o deslocamento realizado.
    """
    pass


class Manutencao:
    """
    Representa um registro de manutenção realizada ou prevista
    para um veículo da frota.
    """
    pass


class Abastecimento:
    """
    Representa um registro de abastecimento realizado em um
    veículo da frota.
    """
    pass