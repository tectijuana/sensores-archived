
![cooltext399335322948702](https://user-images.githubusercontent.com/84939760/144688840-36fd0fd0-7520-4ec9-832f-42d9a91aba05.png)

# Datos técnicos 
### Descripción.

El módulo de sensor de temperatura para Arduino Keyes KY-001 permite la medición de la temperatura ambiente entregando datos mediante un bus serie digital.

#### Imagen 2. Sensor
![KY-001](https://user-images.githubusercontent.com/84939760/144689319-44c2afce-084f-49cd-ad2e-e952edb6968b.png)

## Especificaciones.

| Descripcion | Valor |
| --- | --- |
| Fabricante| Dallas 18B20 |
| Voltaje de funcionamiento | 3V a 5.5V |
| Rango de medición de temperatura | -55 ° C a 125 ° C |
| Rango de precisión de medición | ± 0.5 ° C |
| Dimensiones | 18.5mm x 15mm |
| Resolución en Modo Termómetro | 9 a 12 bits |
| Interfaz | 1-Wire (OneWire) |
| Peso | 2 gr |
| Pines | GND, VCC y Señal |

#### Imagen 2. Pines del sensor
![image](https://user-images.githubusercontent.com/84939760/144693689-b554dc31-3c78-4b22-bbac-46e9f54e507b.png)

## Circuito.
Ya que este sensor es "simple" por decirlo de alguna forma, su implementación también es simple.
En este caso se puede conectar a un Arduino los conectores de energía y el puerto DATA a una conexión digital.

Materiales:
- KY-001 18B20
- R pi pico

Si bien en la imagen 3 se muestra un protoboard no es necesario.

#### Imagen 3. Circuito en Tinkercad
 ![Diagrama](https://user-images.githubusercontent.com/84939760/145498921-46443096-3312-4319-bf41-e3c07906ccc8.png)

```python
#
# Por: ERIK URIEL ESCOBAR PEREZ
#
    import machine, onewire, ds18x20, time
    
    ds_pin = machine.Pin(4)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    
    roms = ds_sensor.scan()
    print('Found DS devices: ', roms)
    
    while True:
      ds_sensor.convert_temp()
      time.sleep_ms(750)
      for rom in roms:
        print(rom)
        print(ds_sensor.read_temp(rom))
      time.sleep(5)                      
```
