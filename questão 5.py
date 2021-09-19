import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL,'pt_BR')

def retornar_data_porextenso(data_string):
    try:
        datetime.strptime(data_string,"%d/%m/%Y")
    except ValueError:
        print("Inválido. Tente novamente")
        return None 
    else: 
        data_datetime = datetime.strptime(data_string,"%d/%m/%Y")
        return datetime.strftime(data_datetime,"%d de %B de %Y")
    

data = input("Digite uma data no formato DD/MM/AAAA:  ")
data_porextenso = retornar_data_porextenso(data)

if data_porextenso is not None:
    print(data_porextenso)





