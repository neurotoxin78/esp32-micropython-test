# This file is executed on every boot (including wake-boot from deepsleep)
import esp
from machine import freq, RTC
import ntptime
from utime import sleep_ms
from sys import path

esp.osdebug(None)
freq(160000000)
path[1] = '/lib'

ssid_ = "Neurotoxin2"
wp2_pass = "Mxbb2Col"

def do_connect(ssid, passwd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def set_time():
    """
    docstring
    """
    print("Synchronize time from NTP server ...")
    ntptime.host = 'ua.pool.ntp.org'
    ntptime.settime()
    sleep_ms(100)

do_connect(ssid_, wp2_pass)
set_time()