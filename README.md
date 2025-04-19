# pico-w-mqtt-weather

## Prerequisites:
-  Raspberry Pi Pico W
-  install umqtt.simple on your Pico
-  create an account at `https://io.adafruit.com`
-  create an account at `https://www.weatherapi.com/`

## First Steps:
-  fill in your WiFi details and your Free Weather Api Key in `/lib/env.py`
-  add the highlighted missing values in `main.py` according to your Adafruit IO credentials
-  apply the location you want the temperature to be logged from in `main.py`

## Goal:
-  every 15 minutes, the current temperature of your set location is logged to your Adafruit IO dashboard
