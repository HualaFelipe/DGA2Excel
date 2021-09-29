

import datetime

from UnidadTemporalDiaria import UnidadTemporalDiaria


class DatosEstacion:

    def __init__(self, hojaDatosDGA):
        self.estacion = hojaDatosDGA.estacion
        self.codigoBNA = hojaDatosDGA.codigoBNA
        self.cuenca = hojaDatosDGA.cuenca
        self.subcuenca = hojaDatosDGA.subcuenca
        self.altitud = hojaDatosDGA.altitud
        self.latitud = hojaDatosDGA.latitud
        self.longitud = hojaDatosDGA.longitud
        self.UTMNorte = hojaDatosDGA.UTMNorte
        self.UTMEste = hojaDatosDGA.UTMEste
        self.areaDrenaje = hojaDatosDGA.areaDrenaje
        self.serieTiempo = hojaDatosDGA.serieTiempo
        self.hojasDatosDGA = [hojaDatosDGA]


    def agregarHojaDatos(self,nuevaHojaDatoDGA):
        unDia = datetime.timedelta(days=1)
        serieTiempoNueva = nuevaHojaDatoDGA.serieTiempo
        contAct = 0
        contNuevo = 0
        serieTiempoFinal = []

        while contAct < len(self.serieTiempo) or contNuevo<len(serieTiempoNueva):
            if contAct >= len(self.serieTiempo):
                if(serieTiempoFinal[-1].dt+unDia < serieTiempoNueva[contNuevo].dt):
                    ##Agregar un día
                    tiempoNuevoExtraVacio = serieTiempoFinal[-1].dt + unDia
                    unidadTemporalExtra = UnidadTemporalDiaria(tiempoNuevoExtraVacio.day,
                                                               tiempoNuevoExtraVacio.month,
                                                               tiempoNuevoExtraVacio.year, "")
                    serieTiempoFinal.append(unidadTemporalExtra)

                elif serieTiempoFinal[-1].dt+unDia >= serieTiempoNueva[contNuevo].dt:
                    serieTiempoFinal.append(serieTiempoNueva[contNuevo])
                    contNuevo = contNuevo + 1

            elif contNuevo >= len(serieTiempoNueva):
                if serieTiempoFinal[-1].dt+unDia < self.serieTiempo[contAct].dt:
                    ##Agregar un día

                    tiempoNuevoExtraVacio = serieTiempoFinal[-1].dt+unDia
                    unidadTemporalExtra = UnidadTemporalDiaria(tiempoNuevoExtraVacio.day,
                                                               tiempoNuevoExtraVacio.month,
                                                               tiempoNuevoExtraVacio.year,"")
                    serieTiempoFinal.append(unidadTemporalExtra)

                elif serieTiempoFinal[-1].dt+unDia >= self.serieTiempo[contAct].dt:
                    serieTiempoFinal.append(self.serieTiempo[contAct])
                    contAct = contAct + 1


            elif contAct < len(self.serieTiempo) and contNuevo<len(serieTiempoNueva):
                if serieTiempoNueva[contNuevo].dt < self.serieTiempo[contAct].dt and contNuevo < len(serieTiempoNueva):
                    serieTiempoFinal.append(serieTiempoNueva[contNuevo])
                    contNuevo = contNuevo+1

                elif self.serieTiempo[contAct].dt < serieTiempoNueva[contNuevo].dt and contAct < len(self.serieTiempo):
                    serieTiempoFinal.append(self.serieTiempo[contAct])
                    contAct = contAct+1
                elif self.serieTiempo[contAct].dt == serieTiempoNueva[contNuevo].dt and contAct < len(self.serieTiempo) and contNuevo < len(serieTiempoNueva):

                    if self.serieTiempo[contAct].valor == ""  and serieTiempoNueva[contNuevo].valor == "":
                        serieTiempoFinal.append(self.serieTiempo[contAct])

                    elif self.serieTiempo[contAct].valor != "":
                        serieTiempoFinal.append(self.serieTiempo[contAct])

                    elif serieTiempoNueva[contNuevo].valor != "":
                        serieTiempoFinal.append(serieTiempoNueva[contNuevo])

                    else:
                        serieTiempoFinal.append(self.serieTiempo[contAct])


                    contAct = contAct + 1
                    contNuevo = contNuevo + 1

        self.serieTiempo = serieTiempoFinal

    def imprimir(self):

        print(self.estacion)
        print(self.codigoBNA)
        print(self.cuenca)
        print(self.subcuenca)
        print(self.altitud)
        print(self.latitud)
        print(self.longitud)
        print(self.UTMNorte)
        print(self.UTMEste)
        print(self.areaDrenaje)


        for x in self.serieTiempo:
            print("-> ",x.dia,"/",x.mes,"/",x.ano,"---",x.valor)






