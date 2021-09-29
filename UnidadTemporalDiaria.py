import time
import datetime

class UnidadTemporalDiaria():

    def __init__(self,dia,mes,ano,valor):
        self.valor = valor
        self.ano = ano
        self.mes = mes
        self.dia = dia

        self.dt = datetime.datetime(year=self.ano , month=self.mes, day=self.dia)


