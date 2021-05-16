Useful scripts for raspberry pi.

## fan.py
Use GPIO.13 (BCM) for fan control. Run when CPU temp is above 45°C and stop when below 40°C.
The current of raspberry pi pins is not enough for powering the fan so a triode is used to amplify the current.


## shutdown.py
Use GPIO.19 for shutdown & reboot button, use GPIO.26 for LED indicator.
Press the button and the script will countdown from 10 before reboot.
Press again to switch between reboot/shutdown/cancel mode.
|Mode|LED|
|reboot|blink|
|shutdown|on|
|cancel|off|

![example](./wiring.jpg)

## Run

Add execute permission
```bash
chmod 775 fan.py
```
### Run at background
nohup ./fan.py &

### Terminate
Find the PID of the process
```bash
ps auxf | fan.py
```
End the process
```bash
kill PID
```

### Run at startup

Open the *rc.local* file
```bash
sudo nano /etc/rc.local
```

Add the following two lines:
```bash
python /home/pi/scripts/shutdown.py &
python /home/pi/scripts/fan.py &
```
Save and exit.

## References
<https://shumeipai.nxez.com/2017/07/13/raspberry-pi-to-achieve-temperature-monitoring-and-control-fan-cooling.html>
<https://shumeipai.nxez.com/2014/09/01/add-raspberry-pi-sent-to-reboot-off-button.html>
