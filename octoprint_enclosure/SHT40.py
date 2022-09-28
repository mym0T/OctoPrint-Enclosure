import time
import sys
import board
import adafruit_sht4x


i2c = board.I2C() # uses board.SCL and board.SDA
sht = adafruit_sht4x.SHT4x(i2c)
sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
# Can also set the mode to enable heater
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
cTemp, humidity = sht.measurements

print('{0:0.1f} | {1:0.1f}'.format(cTemp, humidity))
