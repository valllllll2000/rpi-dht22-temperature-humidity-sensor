# rpi-dht22-temperature-humidity-sensor


Inspired by: https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4
Using code from: https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup

Using raspberry pi zero W

Hardware diagram

<img src="https://github.com/valllllll2000/rpi-dht22-temperature-humidity-sensor/assets/923280/e84a83f1-f40b-4d82-8147-69f80e6a1c4d" width="400" />
<img src="https://github.com/valllllll2000/rpi-dht22-temperature-humidity-sensor/assets/923280/4eb62396-b247-4ce6-a1ea-80a7e29f1075" width="400" />

to run it:
`pgrep -f dht22.py || nohup python3 /home/user/dht22/dht22.py > test.out`
