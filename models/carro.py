# models/carro.py

from models.base import BaseModel

class Carro(BaseModel):
    """
    Classe que representa um Carro.
    Ela HERDA a BaseModel, por isso consegue:
    - salvar no JSON
    - carregar dados do JSON
    """

    # arquivo onde os carros serão salvos
    arquivo = "carros.json"

    def __init__(self, marca, modelo, ano):
        # atributos privados (encapsulamento)
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # GETTERS
    def get_marca(self): return self.__marca
    def get_modelo(self): return self.__modelo
    def get_ano(self): return self.__ano

    # SETTERS
    def set_marca(self, marca): self.__marca = marca
    def set_modelo(self, modelo): self.__modelo = modelo
    def set_ano(self, ano): self.__ano = ano

    def salvar_carro(self):
        """
        Prepara os dados do carro e envia para BaseModel.salvar()
        """

        dados = {
            "marca": self.__marca,
            "modelo": self.__modelo,
            "ano": self.__ano
        }

        super().salvar(dados)  # chama método da classe mãe

