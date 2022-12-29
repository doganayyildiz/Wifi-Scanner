from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import network
from machine import Pin
import utime

wlan = network.WLAN(network.STA_IF) 
wlan.active(True) 

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
oled.fill(0)



while True:

    
    liste = []
    liste2 = []

    accessPoints = wlan.scan()

    for ap in accessPoints:
        oled.fill(0) 
        if ap[0] not in liste:
            liste.append(ap[0])
            if len(liste) == 1:
                #print(liste[0])
                #print("------------------")
                oled.text("--WIFI LIST--",10,0)
                oled.text(liste[0],0,15)
                oled.show()
                
            elif len(liste) == 2:
                #print(liste[0])
                #print(liste[1])
                #print("------------------")
                oled.text("--WIFI LIST--",10,0)
                oled.text(liste[0],0,15)
                oled.text(liste[1],0,30)
                oled.show()
                
            elif len(liste) == 3:
                #print(liste[0])
                #print(liste[1])
                #print(liste[2])
                #print("------------------")
                oled.text("--WIFI LIST--",10,0)
                oled.text(liste[0],0,15)
                oled.text(liste[1],0,30)
                oled.text(liste[2],0,45)
                oled.show()
                
    utime.sleep(5)