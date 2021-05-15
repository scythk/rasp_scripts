Useful scripts for raspberry pi.

## fan.py
Use GPIO.13 for fan control. Run when CPU temp is above 45°C and stop when below 40°C.
The current of raspberry pi pins is not enough for powering the fan so a triode is used to amplify the current.


## shutdown.py
Use GPIO.27 for shutdown & reboot button, use GPIO.17 for LED indicator.
Press once and the script will countdown from 10 before reboot and the LED starts blinking.
Press again will switch to shutdown and the LED fixes.
Press again to abort.

![example](./wiring.jpg)

## Run at startup

Open the *rc.local* file
```bash
sudo nano /etc/rc.local
```

Add the following two lines:
```bash
python /home/pi/scripts/shutdown.py &
python /home/pi/scripts/fan.py &
```

Test before add to startup.

## References
<https://shumeipai.nxez.com/2017/07/13/raspberry-pi-to-achieve-temperature-monitoring-and-control-fan-cooling.html>
<https://shumeipai.nxez.com/2014/09/01/add-raspberry-pi-sent-to-reboot-off-button.html>
