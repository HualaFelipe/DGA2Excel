class CeldaMes:

    def __init__(self, lectorCelda):
        self.LC = lectorCelda

    def actualizaHoja(self):

        if(self.LC.celdaActual == "FEB"):
            ano = self.LC.ano
            if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):

                nDias = 29
            else:

                nDias = 28

        elif(self.LC.celdaActual == "ENE"
                or self.LC.celdaActual == "MAR"
                or self.LC.celdaActual == "MAY"
                or self.LC.celdaActual == "JUL"
                or self.LC.celdaActual == "AGO"
                or self.LC.celdaActual == "OCT"
                or self.LC.celdaActual == "DIC"):
            nDias = 31
        elif(self.LC.celdaActual == "ABR"
                or self.LC.celdaActual == "JUN"
                or self.LC.celdaActual == "SEP"
                or self.LC.celdaActual == "NOV"):
            nDias = 30
        else:
            print("Error CeldaMes")
            nDias = 0




        if self.LC.celdaActual == "ENE":
            mes = 1
        elif self.LC.celdaActual == "FEB":
            mes = 2
        elif self.LC.celdaActual == "MAR":
            mes = 3
        elif self.LC.celdaActual == "ABR":
            mes = 4
        elif self.LC.celdaActual == "MAY":
            mes = 5
        elif self.LC.celdaActual == "JUN":
            mes = 6
        elif self.LC.celdaActual == "JUL":
            mes = 7
        elif self.LC.celdaActual == "AGO":
            mes = 8
        elif self.LC.celdaActual == "SEP":
            mes = 9
        elif self.LC.celdaActual == "OCT":
            mes = 10
        elif self.LC.celdaActual == "NOV":
            mes = 11
        elif self.LC.celdaActual == "DIC":
            mes = 12
        else:
            print("Error mes")
            mes = 0


        cont = 1
        while cont <= nDias:
            dato = self.LC.sheet.cell_value(rowx=(self.LC.rowActual+cont), colx=self.LC.colActual)

            self.LC.agregaDatoLineaTiempo(mes, cont, dato)
            cont = cont+1