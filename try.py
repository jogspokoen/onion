from os import system
from time import sleep

left = 'fast-gpio pwm 11 50 2.5'
middle = 'fast-gpio pwm 11 50 7.5' 
right = 'fast-gpio pwm 11 50 12.5'
release = 'fast-gpio set 11 0'

for i in range(2):
    for c in [left, middle, right, middle]:
        system(c)
        sleep(1)
        system(release)    
