from machine import Pin, I2C
from time import sleep
from bme680 import *

i2c = I2C(0)

bme = BME680_I2C(i2c=i2c)

while True:
  try:
    temperature = str(round(bme.temperature, 2)) + ' C'
    #temp = (bme.temperature) * (9/5) + 32
    #temp = str(round(temp, 2)) + 'F'
    
    humidity = str(round(bme.humidity, 2)) + ' %'
    
    pressure = str(round(bme.pressure, 2)) + ' hPa'
    
    gas = str(round(bme.gas/1000, 2)) + ' KOhms'

    print('Temperatur:', temperature)
    print('Feuchte:', humidity)
    print('Luftdruck:', pressure)
    print('Luftqualität:', gas)
    print('-------')
  except OSError as e:
    print('Sensorfehler!')
 
  sleep(6)