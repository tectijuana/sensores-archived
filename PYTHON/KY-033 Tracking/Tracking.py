# Revisado por Daniel Aquino Villegas 18212144
# No es el sensor correcto 

from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C

# Importar biblioteca utime para implementar retraso
import utime, time

# Conexión Oled I2C
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Conexión UART del módulo GPS
gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Imprimir detalles de conexión del módulo gps
print(gps_module)

# Se utiliza para almacenar sentencias NMEA
buff = bytearray(255)

TIMEOUT = False

# Almacenar el estado del satélite es fijo o no
FIX_STATUS = False

# Almacenar coordenadas GPS
latitude = ""
longitude = ""
satellites = ""
gpsTime = ""


# Función para obtener coordenadas gps
def getPositionData(gps_module):
    global FIX_STATUS, TIMEOUT, latitude, longitude, satellites, gpsTime
    
    # Ejecutar while loop para obtener datos gps
    # o terminar el ciclo while después de 5 segundos de tiempo de espera
    timeout = time.time() + 8   # 8 segundos a partir de ahora
    while True:
        gps_module.readline()
        buff = str(gps_module.readline())
        # Analizar el término $ GPGGA
        # b'$GPGGA,094840.000,2941.8543,N,07232.5745,E,1,09,0.9,102.1,M,0.0,M,,*6C\r\n'
        # print(buff)
        parts = buff.split(',')
        
        # si no se muestra ningún gps, elimine "y len (partes) == 15" de abajo si la condición
        if (parts[0] == "b'$GPGGA" and len(parts) == 15):
            if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]):
                print(buff)
                # print("Message ID  : " + parts[0])
                # print("UTC time    : " + parts[1])
                # print("Latitude    : " + parts[2])
                # print("N/S         : " + parts[3])
                # print("Longitude   : " + parts[4])
                # print("E/W         : " + parts[5])
                # print("Position Fix: " + parts[6])
                # print("n sat       : " + parts[7])
                
                latitude = convertToDigree(parts[2])
                # Las partes [3] contienen 'N' o 'S'
                if (parts[3] == 'S'):
                    latitude = -latitude
                longitude = convertToDigree(parts[4])
                # Las partes [5] contienen 'E' o 'W'
                if (parts[5] == 'W'):
                    longitude = -longitude
                satellites = parts[7]
                gpsTime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                FIX_STATUS = True
                break
                
        if (time.time() > timeout):
            TIMEOUT = True
            break
        utime.sleep_ms(500)
        
# Función para convertir latitud y longitud sin procesar
# a la latitud y longitud reales
def convertToDigree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) #degrees
    nexttwodigits = RawAsFloat - float(firstdigits*100) #minutes
    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) # to 6 decimal places
    return str(Converted)
    
    
while True:
    
    getPositionData(gps_module)

    # Si se encuentran datos gps, imprímalos en lcd
    if(FIX_STATUS == True):
        print("fix......")
        oled.fill(0)
        oled.text("Lat: "+latitude, 0, 0)
        oled.text("Lng: "+longitude, 0, 10)
        oled.text("No of Sat: "+satellites, 0, 20)
        oled.text("Time: "+gpsTime, 0, 30)
        oled.show()
        print(latitude)
        print(longitude)
        print(satellites)
        print(gpsTime)
        
        FIX_STATUS = False
        
    if(TIMEOUT == True):
        print("Request Timeout: No GPS data is found.")
        TIMEOUT = False
