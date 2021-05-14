#!/usr/bin/env python
# coding=utf-8

import sys
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")


def cleanup():
    '''释放资源，不然下次运行是可能会收到警告
    '''
    print('clean up')
    GPIO.cleanup()


def cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", 'r') as f:
        return float(f.read())/1000


def main():
    pin_fan = 13
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # close air fan first
    GPIO.setup(pin_fan, GPIO.OUT, initial=GPIO.LOW)
    is_close = True
    try:
        while True:
            temp = cpu_temp()
            if is_close:
                if temp > 45.0:
                    print time.ctime(), temp, 'open air fan'
                    GPIO.output(pin_fan, GPIO.HIGH)
                    is_close = False
            else:
                if temp < 40.0:
                    print time.ctime(), temp, 'close air fan'
                    GPIO.output(pin_fan, GPIO.LOW)
                    is_close = True

            time.sleep(2.0)
            print time.ctime(), temp
    except KeyboardInterrupt:
        print('User press Ctrl+c ,exit;')
    finally:
        cleanup()


if __name__ == '__main__':
    main()
