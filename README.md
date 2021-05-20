# MQTT Weather Simulator
IoT oriented solution that uses the MQTT protocol.

To simulate a weather sensor, the publisher gets the lattitude and longitude from the IP Address that the computer is connected to. Once the IP location zone has been retrieved, the publisher makes an API call to the OpenWeather API and then publishes the data to the MQTT Broker. The MQTT publisher was written in python. 
