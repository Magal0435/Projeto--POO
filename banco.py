import json
import os

class BancoDeDados:
    '''
    Classe responsável por armazenar dados no sistema e carrega-los depois
    Salva os dados no arquivo banco_de_dados.json
    '''
    def __init__ (self, arquivo="base_de_dados.json"):
        self.__arquivo = arquivo

    def carregar (self):
        '''
        carrega os dados existentes no banco de dados

        se não existir o arquivo, cria um arquivo de base de dados vazio
        '''
        if not os.self.exists(self.__arquivo):
            return.self.__estrutura_vazia()

        try with open(self.__arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            return dados

        except (json.JSONDecodeError, FileNotFoundError):

            return self.__estrutura_vazia()

    def salvar (self, dados):
        '''
        salva os arquivos no json
        '''
        with open(self.__arquivo,"w",encoding = "utf-8") as arquivo:
            json.dump(
                dados,
                arquivo,
                ensure_ascii = False,
                indent = 4
            ) 

    def adicionar(self, categoria, registro):
        '''
        adiciona uma nova categoria no banco de dados
        '''
        dados = self.carregar()
        if categoria not in dados:
            dados[categoria] = []
            dados [categoria].append(registro)
            self.salvar(dados)
    
    def _estrutura_vazia(self):
        '''
        Retorna a estrutura inicial do banco de dados.
        '''

        return {
            "veiculos": [],
            "motoristas": [],
            "viagens": [],
            "manutencoes": [],
            "abastecimentos": []
        }
