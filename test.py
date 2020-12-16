# code for micropython 1.10 on esp8266

import random

import time
import machine
import st7789py as st7789
from machine import Pin
import gfx
from gc import mem_free, collect

def main():
    spi = machine.SPI(1, baudrate=8000000, polarity=1, phase=1, sck=Pin(18, Pin.OUT, Pin.PULL_DOWN), mosi=Pin(23, Pin.OUT, Pin.PULL_UP), miso=Pin(19,Pin.IN, Pin.PULL_UP))
    display = st7789.ST7789(spi, 240, 240, reset=Pin(2, machine.Pin.OUT, Pin.PULL_UP), dc=Pin(4, machine.Pin.OUT, Pin.PULL_UP),)
    display.init()
    display.fill(st7789.color565(128,128,255))
    graphics = gfx.GFX(240, 240, display.pixel)
    graphics.fill_rect(50, 50, 50, 50, st7789.color565(0,0,0))
    print(mem_free())
    collect()
    print(mem_free())   
    while True:
        display.fill(st7789.color565(random.getrandbits(8), random.getrandbits(8), random.getrandbits(8),),)
        # Pause 2 seconds.
        time.sleep(0.5)

if __name__ == "__main__":
    main()