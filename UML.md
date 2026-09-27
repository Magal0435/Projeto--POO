```mermaid
classDiagram
    direction LR

    class VeiculoBase {
        <<Base>>
        +placa: str
        +marca: str
        +modelo: str
        +tipo: str
        +ano: int
        +quilometragem: float
        +consumo_medio: float
        +status: str
        --
        +atualizar_quilometragem()
        +alterar_status()
        +registrar_evento()
        +__str__()
        +__repr__()
        +__eq__()
        +__lt__()
        +__iter__()
    }

    class PessoaBase {
        <<Base>>
        +nome: str
        +cpf: str
        +funcao: str
    }

    class Motorista {
        +categoria_cnh: str
        +experiencia_anos: int
        +disponibilidade: bool
        +historico_viagens: list
    }

    class Carro {
    }

    class Moto {
    }

    class Caminhao {
    }

    class Viagem {
        +motorista: Motorista
        +veiculo: VeiculoBase
        +origem: str
        +destino: str
        +distancia: float
        +data: datetime
    }

    class ManutenivelMixin {
        <<Mixin>>
        --
        +registrar_manutencao()
    }

    class AbastecivelMixin {
        <<Mixin>>
        --
        +abastecer()
    }

    class Manutencao {
        +data: datetime
        +tipo: str
        +custo: float
        +descricao: str
        +veiculo: VeiculoBase
        +status: str
    }

    class Abastecimento {
        +data: datetime
        +tipo_combustivel: str
        +litros: float
        +valor_pago: float
        +veiculo: VeiculoBase
        +quilometragem: float
    }

    Carro --|> VeiculoBase
    Moto --|> VeiculoBase
    Caminhao --|> VeiculoBase
    Motorista --|> PessoaBase

    VeiculoBase --> ManutenivelMixin : herda funcionalidades
    VeiculoBase --> AbastecivelMixin : herda funcionalidades

    VeiculoBase --> Manutencao : possui relação
    VeiculoBase --> Abastecimento : possui relação
    VeiculoBase --> Viagem : possui relação

    Motorista --> Viagem : realiza

    Manutencao --> ManutenivelMixin : usa
    Abastecimento --> AbastecivelMixin : usa
