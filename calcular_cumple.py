from datetime import datetime
def calcularCumple(año,mes,dia):
    tiempo_actual=datetime.now()
    mi_cumple=datetime(año,mes,dia)
    tiempo_falta=mi_cumple-tiempo_actual
    resultado=tiempo_falta.days *60*60*24 + tiempo_falta.seconds
    return resultado