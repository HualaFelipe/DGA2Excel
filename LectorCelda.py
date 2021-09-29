from CeldaAno import CeldaAno
from CeldaDatoGeneral import CeldaDatoGeneral
from CeldaMes import CeldaMes
from CeldaNull import CeldaNull
from HojaDatosDGA import HojaDatosDGA
from UnidadTemporalDiaria import UnidadTemporalDiaria


class LectorCelda:

    def __init__(self, sheet):
        self.ano = None
        self.sheet = sheet
        self.rowActual = 0
        self.colActual = 0
        self.rowLimit = sheet.nrows
        self.colLimit = sheet.ncols
        self.celdaActual = self.sheet.cell_value(rowx=self.rowActual, colx=self.colActual)
        self.hojaDatosDGA = HojaDatosDGA()

    def evaluarHoja(self):
        while(True):
            if not self.leerCeldaActual():
                break

    def agregaDatoLineaTiempo(self,mes,dia,valor):

        unidadTemporal = UnidadTemporalDiaria(dia,mes,self.ano,valor)

        self.hojaDatosDGA.serieTiempo.append(unidadTemporal)


    def actCelda(self):
        self.celdaActual = self.sheet.cell_value(rowx=self.rowActual, colx=self.colActual)

    def leerCeldaActual(self):
        if self.celdaActual == "":
            celda = CeldaNull()
        elif (self.celdaActual == "Estación:"
              or self.celdaActual == "Codigo BNA:"
              or self.celdaActual == "Cuenca:"
              or self.celdaActual == "SubCuenca:"
              or self.celdaActual == "Altitud (msnm):"
              or self.celdaActual == "Latitud S:"
              or self.celdaActual == "Longitud W:"
              or self.celdaActual == "UTM Norte (mts):"
              or self.celdaActual == "UTM Este (mts):"
              or self.celdaActual == "Área de Drenaje (km2):"):

            celda = CeldaDatoGeneral(self)
        elif (self.celdaActual == "ENE"
              or self.celdaActual == "FEB"
              or self.celdaActual == "MAR"
              or self.celdaActual == "ABR"
              or self.celdaActual == "MAY"
              or self.celdaActual == "JUN"
              or self.celdaActual == "JUL"
              or self.celdaActual == "AGO"
              or self.celdaActual == "SEP"
              or self.celdaActual == "OCT"
              or self.celdaActual == "NOV"
              or self.celdaActual == "DIC"):

            celda = CeldaMes(self)
        elif isinstance(self.celdaActual, str):
            if("AÑO" in self.celdaActual):

                celda = CeldaAno(self)
            else:
                celda = CeldaNull()
        else:
            celda = CeldaNull()

        celda.actualizaHoja()


        bool = self.pasarSiguienteCelda()

        return bool

    def pasarSiguienteCelda(self):


        ##caso ultima celda
        if(self.rowActual == self.rowLimit-1 and self.colActual == self.colLimit-1):
            return False
        ##Caso ultima columna de la fila se aumenta row se devuelve col a 0
        elif(self.colActual == self.colLimit-1):
            self.colActual = 0
            self.rowActual = self.rowActual+1
        ##caso general (se aumenta col)
        else:
            self.colActual = self.colActual + 1

        self.actCelda()

        return True


    def buscarColDatoSiguiente(self):

        cont = 1
        while self.sheet.cell_value(rowx=self.rowActual, colx=(self.colActual + cont)) == "":
            cont = cont + 1

        return self.colActual + cont


    def imprimir(self):

        print(self.hojaDatosDGA.estacion)
        print(self.hojaDatosDGA.codigoBNA)
        print(self.hojaDatosDGA.cuenca)
        print(self.hojaDatosDGA.subcuenca)
        print(self.hojaDatosDGA.altitud)
        print(self.hojaDatosDGA.latitud)
        print(self.hojaDatosDGA.longitud)
        print(self.hojaDatosDGA.UTMNorte)
        print(self.hojaDatosDGA.UTMEste)
        print(self.hojaDatosDGA.areaDrenaje)


        for x in self.hojaDatosDGA.serieTiempo:
            print("-> ",x.dia,"/",x.mes,"/",x.ano,"---",x.valor)

