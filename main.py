from machine import Pin
from time import sleep
import neopixel
import network
import urequests
pixels = neopixel.NeoPixel(Pin(14, Pin.OUT), 64)
#Weather Conditions, these are the LEDS to light up on the Unicorn HAT
sun = [11,12,18,19,20,21,25,26,27,28,29,30,33,34,35,36,37,38,42,43,44,45,51,52]
cloudy = [4,5,6,9,10,11,12,19,20,21,22,25,26,27,28,29,30,33,34,35,36,37,38,41,42,43,44,52,53,54,57,58,59]
rain_cloud = [4,5,6,10,11,12,19,20,22,26,27,28,29,30,33,34,35,36,38,42,43,44,52,54,57,58,59]
rain = [7,9,21,23,25,37,39,41,53]
lightning_cloud = [4,5,6,9,10,11,12,19,21,25,27,28,29,30,33,34,35,36,37,38,42,44,52,54,57,58,59]
lightning = [8,20,22,26,39,41,43,53]
snow_ice = [1,4,7,9,11,13,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,50,52,54,56,59,62]
clear_sky = [2,3,4,5,10,11,12,13,16,17,18,19,20,21,26,27,28,29,30,31,32,33,34,35,36,37,42,43,44,45,46,47,48,49,50,51,52,53,58,59,60,61,62,63]
clear_sun = [0,1,14,15]
clear_gnd = [6,7,8,9,22,23,24,25,38,39,40,41,54,55,56,57]

#Setup WiFi
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("YOUR WIFI SSID", "WiFi Password")
print(sta.isconnected())

#setup the button
button = Pin(12, Pin.IN)

#Delay for showing image
delay = 10

#Clear the screen
def clear():
    for i in range(64):
        pixels[i] = (0x00, 0x00, 0x00)
        pixels.write()


while True:
    print(button.value())

        r = urequests.get("http://api.openweathermap.org/data/2.5/weather?q=<<WHERE DO YOU LIVE?>>&appid=API KEY").json()
        weather = r["weather"][0]["main"]
        print(weather)
        if weather == "Clear":
            for values in sun:
                pixels[values] = (0x4c, 0x99, 0x00)
                pixels.write()
            sleep(delay)
            clear()
        elif weather == "Clouds":
            for values in cloudy:
                pixels[values] = (0x99, 0x99, 0x99)
                pixels.write()
            sleep(delay)
            clear()
        elif weather == "Rain":
            for values in rain_cloud:
                pixels[values] = (0x55, 0x55, 0x55)
                pixels.write()
            for values in rain:
                pixels[values] = (0x00, 0x00, 0x99)
                pixels.write()
            sleep(delay)
            clear()
        elif weather == "Thunderstorm":
            for values in lightning_cloud:
                pixels[values] = (0x55, 0x55, 0x55)
                pixels.write()
            for values in lightning:
                pixels[values] = (0x4c, 0x99, 0x00)
                pixels.write()
            sleep(delay)
            clear()
        elif weather == "Snow":
            for values in snow_ice:
                pixels[values] = (0x00, 0x00, 0x99)
                pixels.write()
            sleep(delay)
            clear()
    sleep(1)
