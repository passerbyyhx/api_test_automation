from common.base_classes.base_api import BaseDomain
from api_data.weather_open_api_data import WeatherOpenAPIData

class WeatherOpenAPI(BaseDomain):
    def __init__(self):
        BaseDomain.__init__(self, "https://data.weather.gov.hk/weatherAPI/opendata")
        self.api_data = WeatherOpenAPIData()
        self.data = self.api_data.data
        self.params = self.api_data.params

        # ================================= APIs does not require additional arguments =================================
        self.nine_day_weather = self.sub_path("weather.php", data=self.data, params=self.params)


