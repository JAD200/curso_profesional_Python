from datetime import date, datetime
import pytz


def timezone(ciudad):
    timezon_city = pytz.timezone('America/' + ciudad)
    timezon_date = datetime.now(timezon_city)
    print(ciudad,': ', timezon_date.strftime('%d/%m/%Y, %H:%M:%S'))

def run():
    while True:
        try:
            print('*\tQuieres saber que hora es en otro lugar?\t*')
            ciudad = str(input('Introduzca una ciudad capital por favor: ')).replace(' ', '_').capitalize()
            timezone(ciudad)
            break
        except Exception:
            print('Lo sentimos pero la ciudad ', ciudad,' no existe. \nIntente de nuevo' )


if __name__ == '__main__':
    run()