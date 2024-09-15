from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade_carga):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade_carga = capacidade_carga
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
 - Cap. carga: {self.__capacidade_carga}'''
    