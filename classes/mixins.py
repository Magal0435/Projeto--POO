class ManutenivelMixin:
    """
    Define a capacidade de um objeto possuir e registrar
    informações relacionadas a manutenções.
    """

    def registrar_manutencao(self):
        """
        Registra uma manutenção para o objeto.
        """
        pass


class AbastecivelMixin:
    """
    Define a capacidade de um objeto possuir e registrar
    informações relacionadas a abastecimentos.
    """

    def abastecer(self):
        """
        Registra um abastecimento para o objeto.
        """
        pass
