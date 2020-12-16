from st7789 import ST7789, color565
from machine import Pin, SPI


class UI(object):
    def __init__(self):
        """
        docstring
        """
        # Display
        spi = SPI(1, baudrate=25000000, polarity=1, phase=0, sck=Pin(
            18, Pin.OUT, Pin.PULL_DOWN), mosi=Pin(23, Pin.OUT, Pin.PULL_UP), miso=Pin(19, Pin.IN, Pin.PULL_UP))
        self.display = ST7789(spi, 240, 240, rst=Pin(2, Pin.OUT, Pin.PULL_UP), dc=Pin(4, Pin.OUT, Pin.PULL_UP),cs=Pin(0))
        self.display.init()
    def fill_screen(self, color):
        """
        docstring
        """
        self.display.fill(color)
    def cls(self):
        """
        docstring
        """
        self.display.fill(0)
        self.display.pixel(10,10,color565(0, 255, 0))