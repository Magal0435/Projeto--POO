# Projeto--POO
# TEMA 2: SISTEMA DE GERENCIAMENTO DE FROTA DE VEÍCULOS

## 1. Descrição do Projeto
Projeto que busca criar um sistema de linha de comando (CLI) ou uma API mínima (como FastAPI ou Flask) para gerenciar a frota de veículos de uma empresa de transporte. O sistema aplica conceitos de Programação Orientada a Objetos, como encapsulamento, herança (simples e múltipla), métodos especiais e regras de negócio configuráveis, utilizando persistência de dados em JSON ou SQLite com um repositório desacoplado do domínio.

## 2. Objetivo
Centralizar o cadastro e o controle de veículos e motoristas, permitindo registrar viagens, manutenções e abastecimentos, além de calcular custos médios e disponibilizar relatórios de desempenho.

## 3. Classes, Atributos e Métodos
#### Veiculo (Classe Base)
* **Atributos (privados com `@property`):** `_placa`, `_marca`, `_modelo`, `_tipo`, `_ano`, `_quilometragem`, `_consumo_medio`, `_status` (Enum: ATIVO, MANUTENCAO, INATIVO).
* **Métodos Principais:** `atualizar_quilometragem(distancia: float)`, `alterar_status(novo_status)`, `registrar_evento(evento)`.
* **Métodos Especiais:**
    * `__str__()` / `__repr__()`: Retorna um resumo legível do veículo.
    * `__eq__()`: Compara a igualdade de veículos utilizando a placa.
    * `__lt__()`: Permite ordenar os veículos pela quilometragem.
    * `__iter__()`: Permite iterar sobre o histórico de manutenções/eventos do veículo.

#### Especializações de Veículo (Herança Simples)
* **Carro(Veiculo)**
* **Moto(Veiculo)**
* **Caminhao(Veiculo)**

#### Mixins (Herança Múltipla)
* **AbastecivelMixin:**
    * **Atributos:** `_historico_abastecimentos`
    * **Métodos:** `abastecer(abastecimento: Abastecimento)`
* **ManutenivelMixin:**
    * **Atributos:** `_historico_manutencoes`
    * **Métodos:** `registrar_manutencao(manutencao: Manutencao)`

#### Pessoa e Motorista
* **Pessoa (Classe Base):**
    * **Atributos:** `_nome`, `_cpf`, `_funcao`
* **Motorista(Pessoa):**
    * **Atributos Adicionais:** `_categoria_cnh`, `_experiencia_anos`, `_disponibilidade`, `_historico_viagens`
    * **Métodos:** `adicionar_viagem(viagem: Viagem)`, `verificar_compatibilidade(tipo_veiculo)`

#### Entidades de Transação
* **Viagem:**
    * **Atributos:** `_motorista`, `_veiculo`, `_origem`, `_destino`, `_distancia`, `_data`
* **Manutencao:**
    * **Atributos:** `_data`, `_tipo` (Preventiva ou Corretiva), `_custo`, `_descricao`, `_veiculo`, `_status`
* **Abastecimento:**
    * **Atributos:** `_data`, `_tipo_combustivel`, `_litros`, `_valor_pago`, `_veiculo`, `_quilometragem_momento`

#### Exceções Customizadas
* `ManutencaoInvalidaError`, `AlocacaoInvalidaError`, `PoliticaNaoAtendidaError`, `RepositorioError`.

