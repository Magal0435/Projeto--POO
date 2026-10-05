class PessoaBase:
    """
    Classe base para representar uma pessoa no sistema.

    Possui informações básicas que podem ser utilizadas por
    diferentes tipos de pessoas.
    """

    def __init__(self, nome, cpf, funcao):
        self.__nome = nome
        self.__cpf = cpf
        self.__funcao = funcao

    # =========================
    # nome
    # =========================

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("O nome não pode ser vazio.")

        self.__nome = valor

    # =========================
    # cpf
    # =========================

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        if not valor:
            raise ValueError("O CPF não pode ser vazio.")

        self.__cpf = valor

    # =========================
    # funcao
    # =========================

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, valor):
        if not valor:
            raise ValueError("A função não pode ser vazia.")

        self.__funcao = valor

class Motorista(PessoaBase):
    """
    Representa um motorista da frota.

    Herda os dados básicos de PessoaBase e adiciona informações
    específicas relacionadas à habilitação, experiência e
    disponibilidade do motorista.
    """

    def __init__(
        self,
        nome,
        cpf,
        funcao,
        categoria_cnh,
        experiencia_anos,
        disponibilidade,
        historico_viagens
    ):
        super().__init__(nome, cpf, funcao)

        self.__categoria_cnh = categoria_cnh
        self.__experiencia_anos = experiencia_anos
        self.__disponibilidade = disponibilidade
        self.__historico_viagens = historico_viagens

    @property
    def categoria_cnh(self):
        return self.__categoria_cnh

    @categoria_cnh.setter
    def categoria_cnh(self, valor):
        if not valor:
            raise ValueError("A categoria da CNH não pode ser vazia.")

        self.__categoria_cnh = valor

    @property
    def experiencia_anos(self):
        return self.__experiencia_anos

    @experiencia_anos.setter
    def experiencia_anos(self, valor):
        if valor < 0:
            raise ValueError(
                "A experiência não pode ser negativa."
            )

        self.__experiencia_anos = valor

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, valor):
        self.__disponibilidade = bool(valor)

    @property
    def historico_viagens(self):
        return self.__historico_viagens

    @historico_viagens.setter
    def historico_viagens(self, valor):
        self.__historico_viagens = valor

