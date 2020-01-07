import RPi.GPIO as gpio
import time

config = {
	"pump_1": {
		"name": "Pump 1",
		"pin": 17,
		"value": "vodka"
	},
	"pump_2": {
		"name": "Pump 2",
		"pin": 27,
		"value": "whiskey"
	},
	"pump_3": {
		"name": "Pump 3",
		"pin": 22,
		"value": "lej"
	},
	"pump_4": {
		"name": "Pump 4",
		"pin": 23,
		"value": "oj"
	},
	"pump_5": {
		"name": "Pump 5",
		"pin": 24,
		"value": "grenadine"
	},
	"pump_6": {
		"name": "Pump 6",
		"pin": 25,
		"value": "cj"
	}
}

gpio.setmode(gpio.BCM)
gpio.setup(config, gpio.OUT)

while True:
	for i in config:
		gpio.output(i, gpio.LOW)
		time.sleep(2);
		gpio.output(i, gpio.HIGH)
		time.sleep(2);

