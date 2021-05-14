Useful scripts for raspberry pi.

## fan.py

## shutdown.py

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
