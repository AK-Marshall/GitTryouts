import time
import numpy as np
import RPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont

# Thresholds for flood prediction
RAIN_THRESHOLD = 64.5  # mm in 24 hours (Heavy Rainfall)
WIND_THRESHOLD = 50  # km/h (Strong Winds)
FLOW_RATE_THRESHOLD = 500  # cumecs (cubic meters per second)
WATER_LEVEL_THRESHOLD = 5.0  # meters (Danger Level)

# SNN Parameters (simplified)
SNN_INPUT_NEURONS = 4  # Rainfall, Wind Speed, Flow Rate, Water Level
SNN_OUTPUT_NEURONS = 1  # Flood Alert
spike_threshold = 0.8  # Probability threshold for alert (0.8 for 80%)
learning_rate = 0.1  # Learning rate for weight adjustment

# Initialize weights randomly for SNN
weights = np.random.rand(SNN_INPUT_NEURONS)

# Variables for sensors
rain_sensor_pin = 27
wind_sensor_pin = 17
flow_sensor_pin = 22
water_level_pin = 23  # Placeholder pin for water level sensor (add actual sensor)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(rain_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(wind_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(flow_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(water_level_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# OLED Display Setup
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, width=128, height=64)

# Function to read sensors (for demonstration, we'll simulate values)
def read_sensors():
    # Simulate readings
    rainfall = np.random.uniform(50, 150)  # Simulate rainfall between 50 and 150 mm
    wind_speed = np.random.uniform(40, 80)  # Simulate wind speed between 40 and 80 km/h
    flow_rate = np.random.uniform(400, 1500)  # Simulate flow rate between 400 and 1500 cumecs
    water_level = np.random.uniform(3, 10)  # Simulate water level between 3 and 10 meters
    
    return rainfall, wind_speed, flow_rate, water_level

# SNN model
def snn_flood_predictor(sensor_inputs, weights):
    # Calculate weighted input to output neuron
    weighted_sum = np.dot(sensor_inputs, weights)
    
    # Sigmoid activation function to simulate spike probability
    output = 1 / (1 + np.exp(-weighted_sum))
    
    return output >= spike_threshold  # Return True if spike occurs

# Function to update weights based on prediction error
def update_weights(weights, sensor_inputs, error):
    return weights + learning_rate * error * sensor_inputs

# Display function
def display_data(rainfall, wind_speed, flow_rate, water_level, flood_alert):
    # Create image with mode '1' for 1-bit color
    image = Image.new('1', (device.width, device.height))
    draw = ImageDraw.Draw(image)
    
    # Draw the text
    draw.text((0, 0), f"Rain: {rainfall:.2f} mm", fill=255)
    draw.text((0, 16), f"Wind: {wind_speed:.2f} km/h", fill=255)
    draw.text((0, 32), f"Flow: {flow_rate:.2f} cumecs", fill=255)
    draw.text((0, 48), f"Level: {water_level:.2f} m", fill=255)
    if flood_alert:
        draw.text((64, 0), "FLOOD ALERT!", fill=255)

    # Display the image
    device.display(image)

# Main loop
try:
    while True:
        # Read sensors
        rainfall, wind_speed, flow_rate, water_level = read_sensors()
        
        # Normalize sensor inputs to range [0, 1] for the SNN
        rain_input = rainfall / RAIN_THRESHOLD
        wind_input = wind_speed / WIND_THRESHOLD
        flow_input = flow_rate / FLOW_RATE_THRESHOLD
        water_level_input = water_level / WATER_LEVEL_THRESHOLD
        
        # Prepare input vector for the SNN
        sensor_inputs = np.array([rain_input, wind_input, flow_input, water_level_input])
        
        # Predict flood alert using SNN
        flood_alert = snn_flood_predictor(sensor_inputs, weights)
        
        # Display sensor data and flood alert status
        display_data(rainfall, wind_speed, flow_rate, water_level, flood_alert)
        
        # Simulate error adjustment (optional, for learning)
        actual_flood_status = 1 if (rainfall > RAIN_THRESHOLD or wind_speed > WIND_THRESHOLD or
                                    flow_rate > FLOW_RATE_THRESHOLD or water_level > WATER_LEVEL_THRESHOLD) else 0
        prediction_error = actual_flood_status - flood_alert
        weights = update_weights(weights, sensor_inputs, prediction_error)
        
        time.sleep(1)  # Small delay for next reading

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO pins on exit

    