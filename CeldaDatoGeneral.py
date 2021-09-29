class CeldaDatoGeneral:

    def __init__(self, lectorCelda):
        self.LC = lectorCelda

    def actualizaHoja(self):
        colSig = self.LC.buscarColDatoSiguiente()
        if self.LC.celdaActual == "Estación:":
            self.LC.hojaDatosDGA.estacion = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))
        elif self.LC.celdaActual == "Codigo BNA:":
            self.LC.hojaDatosDGA.codigoBNA = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "Cuenca:":
            self.LC.hojaDatosDGA.cuenca = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "SubCuenca:":
            self.LC.hojaDatosDGA.subcuenca = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "Altitud (msnm):":
            self.LC.hojaDatosDGA.altitud = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "Latitud S:":
            self.LC.hojaDatosDGA.latitud = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "Longitud W:":
            self.LC.hojaDatosDGA.longitud = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "UTM Norte (mts):":
            self.LC.hojaDatosDGA.UTMNorte = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "UTM Este (mts):":
            self.LC.hojaDatosDGA.UTMEste = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))

        elif self.LC.celdaActual == "Área de Drenaje (km2):":
            self.LC.hojaDatosDGA.areaDrenaje = self.LC.sheet.cell_value(rowx=self.LC.rowActual, colx=(colSig))
        else:
            print("Error Celda Dato General");


