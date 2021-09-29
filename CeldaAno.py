class CeldaAno:

    def __init__(self, lectorCelda):
        self.LC = lectorCelda

    def actualizaHoja(self):
        ano = int(self.LC.celdaActual.replace("AÑO", "").replace(" ","").replace(":",""))
        self.LC.ano = ano
