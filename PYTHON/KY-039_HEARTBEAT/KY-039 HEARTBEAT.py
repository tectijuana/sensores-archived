import machine
import time

factor = 0.75
maximo = 0.0
minimoEntreLatidos = 300
valorAnterior = 500
valorverdadero = 0

sensor = machine.ADC(27)

print('iniciando mediciones')

while True:
    valorticks = time.ticks_ms()
    valorverdadero =  valorverdadero + (time.ticks_ms() - (valorticks - 1))
    
    
    tiempoLPM = valorverdadero
    entreLatidos = valorverdadero
    
    valorLeido = sensor.read_u16()
    
    valorFiltrado = factor * valorAnterior + (1 - factor) * valorLeido
    cambio = valorFiltrado - valorAnterior
    
    valorAnterior = valorFiltrado
    

     
    if((cambio >= maximo) & (valorverdadero > entreLatidos + minimoEntreLatidos)):
        maximo = cambio
        entreLatidos = valorverdadero
        latidos = latidos + 1

    
    
    maximo = maximo *0.97
    
    if (valorverdadero >= tiempoLPM + 15000):
        print('Latidos por minuto: ')
        print(latidos * 4)
        latidos = 0;
        tiempoLMP = valorverdadero
        
    time.sleep_ms(50)