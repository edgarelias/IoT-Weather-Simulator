import paho.mqtt.client as paho


class MQTT():
    """Wrapper for the Paho MQTT Client
    """
    def __init__(self, address, port, topic,username = None, password = None):
        self.address = address
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password
        self.mqtt_client = paho.Client(self.topic)

    def __del__(self):
        self.mqtt_client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        """Callback function that gets called when the MQTT client connects
        """
        if rc==0:
            client.connected_flag=True #set flag
            print("Connected OK - Returned code=",rc)
        else:
            print("Bad connection - Returned code=",rc) 

    def connect(self):
        """Connects to the MQTT Broker
        """
        if self.username != None and self.password != None:
            self.mqtt_client.username_pw_set(username=self.username, password=self.password)
        
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.connect(self.address, self.port, keepalive=80)

    def disconnect(self):
        """Disconnects from the MQTT Broker
        """
        self.mqtt_client.disconnect()

class MQTTPublisher(MQTT):
    """Inherits from the MQTT class wrapper

    Args:
        MQTT (MQTT): Class
    """
    
    def __init__(self, address, port, topic, username = None, password = None):
        super().__init__(address, port, topic, username=username, password=password)

    def on_publish(self,client,userdata,result):
        """Callback function that gets called when a message gets published
        """
        print("Publish Result: ",result)

    def publish(self, data):
        """Publishes a message to the MQTT Broker

        Args:
            data (str): data to publish
        """
        self.mqtt_client.on_publish = self.on_publish
        self.mqtt_client.publish(self.topic,data)
