-- Sensor De Temperatura --

Los sensores de temperatura son componentes eléctricos y electrónicos que, en calidad de sensores, 
permiten medir la temperatura mediante una señal eléctrica determinada. Dicha señal puede enviarse 
directamente o mediante el cambio de la resistencia. También se denominan sensores de calor o termosensores. 
Un sensor de temperatura se usa, entre otras aplicaciones, para el control de circuitos. Los sensores de temperatura también se llaman sensores de calor,
detectores de calor o sondas térmicas.

[![img-0019.jpg](https://i.postimg.cc/zvGMMr5n/img-0019.jpg)](https://postimg.cc/62FY2F83)


¿Qué materiales detecta un sensor de temperatura?

La detección del material depende del tipo y diseño del sensor de temperatura. Esto es especialmente válido para sensores de temperatura que muestran el
cambio de temperatura mediante el cambio de otra magnitud o propiedad física.

Existen muchas clasificaciones, sin embargo una de las más usadas es la que clasifica a este tipo de sensores en seis categorías, estas son:

1.  Sensores de temperatura termopar
2.  Dispositivos de temperatura resistivos RTD y termistores
3.  Dispositivos bimetálicos
4.  Dispositivos de dilatación de líquido
5.  Radiadores infrarrojos
6.  Dispositivos de cambio de estado

-- Esquema -- 

[![144663210-ebafd3d1-2ded-43ed-899c-532ff14702b1.png](https://i.postimg.cc/V6LDsWTw/144663210-ebafd3d1-2ded-43ed-899c-532ff14702b1.png)](https://postimg.cc/XZmwQd41)

-- Diagrama De Conexion -- 

[![144663289-df008797-e99d-4f7f-94a0-84b14f659197.png](https://i.postimg.cc/W1wy2z3M/144663289-df008797-e99d-4f7f-94a0-84b14f659197.png)](https://postimg.cc/Bjtppq26)

Codigo 


import machine
import onewire
import ds18x20
import time

pin_modulo = machine.Pin(26)
sensor = ds18x20.DS18X20(onewire.OneWire(pin_modulo))

roms = sensor.scan()
print("Buscando sensor!!")

while True:
    sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(sensor.read_temp(rom))
    time.sleep(2)


