import requests

class Weather():
    """OpenWeather API Wrapper class
    """

    def __init__(self, api_key) -> None:
        self.url = "api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key


    def get_weather(self, lat, lon):
        """Makes a GET request

        Args:
            lat (str): lattitude
            lon (str): longitude

        Returns:
            dict: API Response
        """
        data = {}

        endpoint = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
        res = requests.get(endpoint)
        data = res.json()
        
        return data