import onionGpio

trigObj = onionGpio.OnionGpio(17)
echoObj = onionGpio.OnionGpio(13)

trigObj._freeGpio()
echoObj._freeGpio()