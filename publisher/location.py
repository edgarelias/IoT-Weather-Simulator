import json
from urllib.request import urlopen

class IPAddressLocation():
    """Uses http://ipinfo.io/json to get the city, country, and region
    by using the machine's IP Address.
    """

    def __init__(self) -> None:
        self.ip=None
        self.city =None
        self.country=None
        self.region=None #state/province
        self.lattitude = None
        self.longitude = None

    def get_address(self):
        """Retrieves the IP, CITY, COUNTRY, and REGION
        from http://ipinfo.io/json and saves the values in
        the class attributes
        """
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        self.ip=data['ip']
        self.city = data['city']
        self.country=data['country']
        self.region=data['region']
        self.lattitude = self.get_lattitude(data['loc'])
        self.longitude = self.get_longitude(data['loc'])
        
    def get_lattitude(self, location):
        """Parses the lattitude from the ipinfo request

        Args:
            location ([str]): location in format: 20.6668,-103.3918
        Returns:
            [str]: [The lattitude (20.6668)]
        """
        return location.split(',')[0]
   
    def get_longitude(self, location):
        """Parses the longitude from the ipinfo request

        Args:
            location ([str]): location in format: 20.6668,-103.3918
        Returns:
            [str]: [The longitude (-103.3918)]
        """
        return location.split(',')[1]


    def display_attributes(self):
        """Displays class attributes
        """
        print(f"IP: {self.ip}")
        print(f"CITY: {self.city}")
        print(f"COUNTRY: {self.country}")
        print(f"REGION: {self.region}")
