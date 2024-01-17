# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
from urllib.request import urlopen

myAPI = "api_key"
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI 

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature, humidity
            )
        )
        RH = str(round(humidity, 1))
        T = str(round(temperature, 1))
        print(RH)
        print(T)
        f = urlopen(baseURL + 
                               "&field1=%s&field2=%s" % (RH, T)) 
        print(f.read()) 
        f.close() 

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(50)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(300)
