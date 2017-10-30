import time
import onionGpio

trigObj = onionGpio.OnionGpio(17)
echoObj = onionGpio.OnionGpio(15)

# trigObj._freeGpio()
# echoObj._freeGpio()

# set to output
# trigObj.setOutputDirection()
# set to input
# echoObj.setInputDirection()


# triggering sensor
trigObj.setValue(1)
time.sleep(0.01)
trigObj.setValue(0)
# reading result
value = echoObj.getValue()
print 'GPIO%d input value: %d'%(13, int(value))

time.sleep(0.01)