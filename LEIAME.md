# PROJETO POO

# TEMA 2: SISTEMA DE GERENCIAMENTO DE FROTA DE VEÍCULOS
# Descrição do projeto
Projeto que busca criar um sistema de linha de comando para gerenciar veículos
# Objetivo
Desenvolver um sistema de linha de comando para gerenciar a frota de veículos de uma empresa de transporte.
# Funções
## 1. Cadastro de veículos
Criar, ler, atualizar e excluir (CRUD) veículos.\
Campos mínimos: placa, marca, modelo, tipo (carro, moto, caminhão), ano, quilometragem, consumo médio (km/l), status (ativo, manutenção, inativo).\
Registrar histórico de eventos: entrada, saída, manutenção, abastecimento, desativação.
## 2. Cadastro de motoristas
Criar, listar, editar e remover motoristas.\
Campos: nome, CPF, categoria da CNH, tempo de experiência (anos), disponibilidade, histórico de viagens.\
Validação automática: só pode dirigir veículos compatíveis com sua categoria.
## 3. Manutenções
Registrar manutenções: data, tipo (preventiva/corretiva), custo, descrição.\
Associar a um veículo e armazenar no histórico.\
Calcular custo médio de manutenção por tipo de veículo.\
Permitir marcar veículo como em manutenção e liberá-lo ao concluir o serviço.
## 4. Abastecimentos
Registrar abastecimentos: data, tipo de combustível, litros, valor pago.\
Calcular consumo médio por veículo (km/l).\
Exibir veículos com consumo fora do padrão definido.
## 5. Alocação de veículos
Associar veículo a um motorista e registrar viagem: origem, destino, distância percorrida.\
Atualizar quilometragem automaticamente após cada viagem.\
Bloquear alocação se o veículo estiver em manutenção ou inativo.
## 6. Relatórios
Custo total e médio de manutenção por tipo de veículo.\
Ranking de veículos por eficiência de combustível.\
Total de viagens por motorista.\
Quilometragem média por tipo de veículo.
## 7. Configurações
Arquivo settings.json com políticas e parâmetros como:\
Limite de quilometragem para revisão preventiva.\
Faixa aceitável de consumo médio (km/l).\
Custos por tipo de manutenção.\
Categoria mínima de CNH por tipo de veículo.

# Modelagem
## Classes
### Veículo: 
Atributos: Modelo, marca, placa, tipo, ano, quilometragem, consumo médio
### Pessoa: 
Atributos: Nome, CPF, função
### Motorista:
Atributo: Nome(herança de pessoa), função (herança de pessoa), categoria da CNH, tempo de experiência (anos), disponibilidade, veículo
### Manutenção:
Atributos: Status de manutenção, data, veículo, custo, tipo de manutenção  
### Relatório:
Atributos: Nome do relatório, data de criação, dados
