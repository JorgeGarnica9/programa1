from datetime import datetime
tiempo_actual=datetime.now()
mi_cumple=datetime(2024,5,2)
tiempo_falta=mi_cumple-tiempo_actual
print(tiempo_falta.days *60*60*24 + tiempo_falta.seconds)