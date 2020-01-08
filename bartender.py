# original imports
import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import sys
import RPi.GPIO as GPIO
import json
import traceback
import threading

# additional imports to handle i2c displays
from lib_oled96 import ssd1306
import logging
from pip._vendor.distlib.compat import raw_input
from smbus import SMBus
from PIL import ImageFont, ImageDraw, Image
from multiprocessing import Process
# paho mqtt library for mqtt communication
import paho.mqtt.client as paho
import json

FONT = ImageFont.truetype("FreeMono.ttf", 15)
I2CBUS = SMBus(1)

from dotstar import Adafruit_DotStar
from menu import MenuItem, Menu, Back, MenuContext, MenuDelegate
from drinks import drink_list, drink_options

# Use the Broadcom counting system on the gpio pins
GPIO.setmode(GPIO.BCM)

# screen size
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# TODO correct button pins
LEFT_BTN_PIN = 6
LEFT_PIN_BOUNCE = 200

RIGHT_BTN_PIN = 5
RIGHT_PIN_BOUNCE = 600

OLED_RESET_PIN = 15
OLED_DC_PIN = 16

# TODO check the flow rate
FLOW_RATE = 60.0 / 100.0

# mqtt-connection related global variables
mqttHost = "broker.mqttdashboard.com"
mqttPort = 1883
mqttTopic = "bartender"
mqttQos = 1

# initialization of a global mqtt-client
mqtt_client = paho.Client()


# mqtt on_connect
def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + rc)
	logging.info("Connected with result code " + rc)


# mqtt on_subscribe
def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))
	logging.info("Subscribed: " + str(mid) + ", QoS: " + str(granted_qos))


# mqtt on_message
def on_message(client, userdata, msg):
	# lists to store keys and values of the ingredients dictionary inside
	keys = []
	values = []
	# initialization of empty ingredients dictionary and drink name
	ingredients = {}
	drink_name = ""
	print("Received message with topic " + str(msg.topic) + ": " + str(msg.payload))
	for drink in drink_list:
		# incoming message matches drink in local drink-list
		if drink["name"] == msg.payload:
			drink_name = drink["name"]
			print("Found " + str(drink["name"]) + " in drinks_list")
			# loop through the drink's ingredient's keys and add them to their list
			for key in drink["ingredients"].keys():
				print(key)
				keys.append(key)
			# loop through the drink's ingredient's values and add them to their list
			for value in drink["ingredients"].values():
				print(value)
				values.append(value)
			# Combine the ingredient's keys and values to a local dictionary
			ingredients = dict(zip(keys, values))
			print("Final dictionary: " + str(ingredients))
			# run the make_drink method using the local drink and ingredients variables
			Bartender().make_drink(drink_name, ingredients)


class Bartender(MenuDelegate):

	def make_drink(self, drink, ingredients):
		# cancel any button presses while the drink is being made
		self.running = True

		# Parse the drink ingredients and create pouring data
		pump_times = []
		for ing in ingredients.keys():
			for pump in self.pump_configuration.keys():
				if ing == self.pump_configuration[pump]["value"]:
					wait_time = ingredients[ing] * FLOW_RATE
					pump_times.append([self.pump_configuration[pump]["pin"], wait_time])

		# Put the drinkjs in the order they'll stop pouring
		pump_times.sort(key=lambda x: x[1])

		# Note the total time required to pour the drink
		total_time = pump_times[-1][1]

		# Change the times to be relative to the previous not absolute
		for i in range(1, len(pump_times)):
			pump_times[i][1] -= pump_times[i - 1][1]

		print(pump_times)

		self.start_progressbar()
		start_time = time.time()
		print("starting all")
		GPIO.output([p[0] for p in pump_times], GPIO.LOW)
		for p in pump_times:
			pin, delay = p
			if delay > 0:
				self.sleep_and_progress(start_time, delay, total_time)
			GPIO.output(pin, GPIO.HIGH)
			print("stopping {}".format(pin))

		# show the main menu
		self.menuContext.showMenu()

		# sleep for a couple seconds to make sure the interrupts don't get triggered
		time.sleep(2)

	def __init__(self):

		# set state to inactive / not pouring a drink
		self.running = False

		print("Bartender booting up")

		# set the oled screen height
		self.set_screen()

		# set the button pins
		self.set_button_pins()

		# configure interrupts for buttons
		self.set_button_interrupts()

		# creating a global reference for the i2c-connected display using the variable 'led'
		self.led = ssd1306(I2CBUS)

		# show a boot logo on startup
		# TODO zeit anpassen
		self.show_boot_logo(1)

		# load the pump configuration from the project file 'pump_config.json'
		self.pump_configuration = Bartender.read_pump_configuration()

		# configure pumps
		self.configure_pumps()

		# setting up mqtt's callback methods
		mqtt_client.on_subscribe = on_subscribe
		mqtt_client.on_message = on_message
		mqtt_client.on_connect = on_connect

		# connect to the mqtt broker and subscribe to the topic 'bartender'
		mqtt_client.connect(mqttHost, mqttPort)
		mqtt_client.subscribe(mqttTopic, qos=mqttQos)

		print("Initialization complete")

	# setting up buttons using corresponding global variables
	def set_button_pins(self):
		self.btn2Pin = RIGHT_BTN_PIN
		self.btn1Pin = LEFT_BTN_PIN

	# setting up the screen size using corresponding global variables
	def set_screen(self):
		self.screen_height = SCREEN_HEIGHT
		self.screen_width = SCREEN_WIDTH

	# configuration of pumps based on the previously imported config in .json format
	def configure_pumps(self):
		for pump in self.pump_configuration.keys():
			# print("Pump: "+[pump]["pin"])
			GPIO.setup(self.pump_configuration[pump]["pin"], GPIO.OUT, initial=GPIO.HIGH)

	# setup of button interrupts
	# assign GPIO pins as input
	def set_button_interrupts(self):
		print("Setting up button interrupts")
		GPIO.setup(self.btn1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.btn2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	# presentation of a custom boot logo when first booting up
	def show_boot_logo(self, seconds):
		print("Showing boot logo")
		logo = Image.open('pi_logo.png')
		self.led.canvas.bitmap((32, 0), logo, fill=1)
		self.led.display()

		# sleep for n seconds to show the raspberry logo
		time.sleep(seconds)

	# import of pump-configuration in .json format
	@staticmethod
	def read_pump_configuration():
		return json.load(open('pump_config.json'))

	# possible edit of the pump_configuration
	@staticmethod
	def write_pump_configuration(configuration):
		with open("pump_config.json", "w") as jsonFile:
			json.dump(configuration, jsonFile)

	# button interrupts -> handling of button clicks
	def start_interrupts(self):
		self.running = True
		GPIO.add_event_detect(self.btn1Pin, GPIO.FALLING, callback=self.left_btn, bouncetime=LEFT_PIN_BOUNCE)
		GPIO.add_event_detect(self.btn2Pin, GPIO.FALLING, callback=self.right_btn, bouncetime=RIGHT_PIN_BOUNCE)
		time.sleep(1)
		self.running = False

	# instantiation of a display-menu using menu.py
	def build_menu(self, drink_list, drink_options):
		# create a new main menu
		m = Menu("Main Menu")

		# add drink options
		drink_opts = []
		for d in drink_list:
			drink_opts.append(MenuItem('drink', d["name"], {"ingredients": d["ingredients"]}))

		configuration_menu = Menu("Configure")

		# add pump configuration options
		pump_opts = []
		for p in sorted(self.pump_configuration.keys()):
			config = Menu(self.pump_configuration[p]["name"])
			# add fluid options for each pump
			for opt in drink_options:
				# star the selected option
				selected = "*" if opt["value"] == self.pump_configuration[p]["value"] else ""
				config.addOption(
					MenuItem('pump_selection', opt["name"], {"key": p, "value": opt["value"], "name": opt["name"]}))
			# add a back button so the user can return without modifying
			config.addOption(Back("Back"))
			config.setParent(configuration_menu)
			pump_opts.append(config)

		# add pump menus to the configuration menu
		configuration_menu.addOptions(pump_opts)
		# add a back button to the configuration menu
		configuration_menu.addOption(Back("Back"))
		# adds an option that cleans all pumps to the configuration menu
		configuration_menu.addOption(MenuItem('clean', 'Clean'))
		configuration_menu.setParent(m)

		m.addOptions(drink_opts)
		m.addOption(configuration_menu)
		# create a menu context
		self.menuContext = MenuContext(m, self)

	# Removes any drinks out of the local stack that can't be handled by the pump configuration
	def filter_drinks(self, menu):
		for i in menu.options:
			if i.type == "drink":
				i.visible = False
				ingredients = i.attributes["ingredients"]
				present_ing = 0
				for ing in ingredients.keys():
					for p in self.pump_configuration.keys():
						if ing == self.pump_configuration[p]["value"]:
							present_ing += 1
				if present_ing == len(ingredients.keys()):
					i.visible = True
			elif i.type == "menu":
				self.filter_drinks(i)

	def select_configurations(self, menu):
		# Adds a selection star to the pump configuration option
		for i in menu.options:
			if i.type == "pump_selection":
				key = i.attributes["key"]
				if self.pump_configuration[key]["value"] == i.attributes["value"]:
					i.name = "%s %s" % (i.attributes["name"], "*")
				else:
					i.name = i.attributes["name"]
			elif i.type == "menu":
				self.select_configurations(i)

	def prepare_for_render(self, menu):
		self.filter_drinks(menu)
		self.select_configurations(menu)
		return True

	def menu_item_clicked(self, menuItem):
		if (menuItem.type == "drink"):
			self.make_drink(menuItem.name, menuItem.attributes["ingredients"])
			return True
		elif (menuItem.type == "pump_selection"):
			self.pump_configuration[menuItem.attributes["key"]]["value"] = menuItem.attributes["value"]
			Bartender.write_pump_configuration(self.pump_configuration)
			return True
		elif (menuItem.type == "clean"):
			self.clean()
			return True
		return False

	def clean(self):
		pins = []

		for pump in self.pump_configuration.keys():
			pins.append(self.pump_configuration[pump]["pin"])

		self.start_progressbar()
		GPIO.output(pins, GPIO.LOW)
		self.sleep_and_progress(time.time(), 20, 20)
		GPIO.output(pins, GPIO.HIGH)

		# show the main menu
		self.menuContext.showMenu()

		# sleep for a couple seconds to make sure the interrupts don't get triggered
		time.sleep(2);

	# display the current menu item on the i2c-display
	def display_menu_items(self, menuItem):
		print(menuItem.name)
		self.led.cls()
		self.led.canvas.text((0, 20), menuItem.name, font=FONT, fill=1)
		self.led.display()

	# def pour(self, pin, waitTime):
		# GPIO.output(pin, GPIO.LOW)
		# time.sleep(waitTime)
		# GPIO.output(pin, GPIO.HIGH)

	# initial display of a progressbar during pour process
	def start_progressbar(self, x=15, y=20):
		start_time = time.time()
		self.led.cls()
		self.led.canvas.text((10, 20), "Dispensing...", font=FONT, fill=1)

	# animated processing of a progress bar
	def sleep_and_progress(self, startTime, waitTime, totalTime, x=15, y=35):
		localStartTime = time.time()
		height = 10
		width = self.screen_width - 2 * x

		while time.time() - localStartTime < waitTime:
			progress = (time.time() - startTime) / totalTime
			p_loc = int(progress * width)
			self.led.canvas.rectangle((x, y, x + width, y + height), outline=255, fill=0)
			self.led.canvas.rectangle((x + 1, y + 1, x + p_loc, y + height - 1), outline=255, fill=1)
			try:
				self.led.display()
			except IOError:
				print("Failed to talk to screen")
			time.sleep(0.2)

	# handle a left button press -> cycle through the menu
	def left_btn(self, ctx):
		print("LEFT_BTN pressed")
		if not self.running:
			self.running = True
			self.menuContext.advance()
			print("Finished processing button press")
		self.running = False

	# handle a right button press -> select the current item
	def right_btn(self, ctx):
		print("RIGHT_BTN pressed")
		if not self.running:
			self.running = True
			self.menuContext.select()
			print("Finished processing button press")
			self.running = 2
			print("Starting button timeout")

	# main loop running indefinitely
	def run(self):
		self.start_interrupts()
		# main loop
		try:
			while True:
				# every 0.1 seconds, loop and listen for new mqtt input
				mqtt_client.loop()
				time.sleep(0.1)

		# clear the GPIO pins on manual CTR+C exit
		except KeyboardInterrupt:
			GPIO.cleanup()  # clean up GPIO on CTRL+C exit
		GPIO.cleanup()  # clean up GPIO on normal exit

		traceback.print_exc()

# main program part


# initialize a bartender object
bartender = Bartender()
# build it's menu
bartender.build_menu(drink_list, drink_options)
# run the bartender
Process(target=bartender.run).start()
