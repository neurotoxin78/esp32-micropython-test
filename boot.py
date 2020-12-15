# This file is executed on every boot (including wake-boot from deepsleep)

import test

import esp
import network
from machine import freq

esp.osdebug(None)

freq(160000000)

ssid_ = "Neurotoxin2"

wp2_pass = "Mxbb2Col"


sta_if = network.WLAN(network.STA_IF)

sta_if.active(True)

sta_if.connect(ssid_, wp2_pass)

print(sta_if.ifconfig())


test.main()
