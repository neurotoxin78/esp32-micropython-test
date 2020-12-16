from st7789 import ST7789, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
from sysfont import sysfont #sysfont for drawing text
from time import sleep

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
        self.display.inversion_mode(1)
        self.display._set_mem_access_mode(4, 0, 0, 1)
        self.fixed_font = XglcdFont('/fonts/FixedFont5x8.c', 5, 8)
        self.neato = XglcdFont('/fonts/Neato5x7.c', 5, 7, letter_count=223)
        self.unispace = XglcdFont('/fonts/Unispace12x24.c', 12, 24)
        self.f18x24 = XglcdFont('/fonts/EspressoDolce18x24.c', 18, 24)
        self.f7x11 = XglcdFont('fonts/Robotron7x11.c', 7, 11)

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
    def draw(self):
        """
        docstring
        """
        self.display.draw_text(0, 0, 'Booting UI', self.unispace, color565(255, 32, 64), landscape=False)
        sleep(2)