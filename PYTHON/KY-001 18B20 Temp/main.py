import machine, onewire, ds18x20, time

ds_pin = machine.Pin(16)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scam()
print('Temperatura')

while True:
    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        tnum = round ( ds_sensor.read_temp(rom),2)
        print(tnum,'Celcius')
    time.sleep(1)