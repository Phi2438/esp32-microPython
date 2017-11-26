import machine
import time

pin13 = machine.Pin(13, machine.Pin.OUT)
for i in range(15):
    pin13.value(1)
    time.sleep_ms(400)
    pin13.value(0)
    time.sleep_ms(500)