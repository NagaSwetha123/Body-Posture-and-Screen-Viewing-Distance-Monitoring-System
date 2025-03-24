from machine import Pin, ADC
import utime, time

# Define pins
trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)
flx = ADC(26)
sw = Pin(9, Pin.OUT)
buz = Pin(8, Pin.OUT)

def ultra():
    """Function to measure distance using ultrasonic sensor."""
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    signaloff, signalon = 0, 0
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

while True:
    try:
        dist = ultra()
    except:
        dist = 30  # Default distance if an error occurs
    
    fv = flx.read_u16()
    sv = sw.value()
    
    print(f'Flex Sensor Value: {fv}')
    print(f'Distance: {dist} cm')
    print(f'Switch Value: {sv}')
    
    if sv == 1 and (fv > 56000 or dist < 30):
        buz.value(1)
        time.sleep(0.1)
        buz.value(0)
        time.sleep(0.1)
    
    utime.sleep(0.2)
