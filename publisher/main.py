# Import Classes
from location import IPAddressLocation
from weather import Weather
from mqtt_wrappers import MQTTPublisher

# Import Libraries
import os
import json

# Import Environment Variables
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
MQTT_ADDRESS = os.getenv('BROKER_ADDRESS')
MQTT_PORT = int(os.getenv('BROKER_PORT'))
MQTT_TOPIC = os.getenv('TOPIC')

def main():

    # Get location coordinates of the machine's current IP Address
    l = IPAddressLocation()
    l.get_address()

    # Get the weather data using the location coordinates
    w = Weather(api_key=WEATHER_API_KEY)
    weather_data = w.get_weather(l.lattitude, l.longitude)

    # Publish data to the MQTT broker
    topic_name = f"{l.city}/{l.region}/{l.country}/weather"
    m = MQTTPublisher(MQTT_ADDRESS, MQTT_PORT, topic_name)
    m.connect()
    print(f"Publish at Topic: {topic_name}")
    m.publish(json.dumps(weather_data))
    m.disconnect()

if __name__ == "__main__":
    main()