

appid = 'ffec6dfe848985bc655b3f0d282df939'
# Define a simple function tool that the agent can use.
# For this example, we use a fake weather tool for demonstration purposes.
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    dict = get_weather_json(city)
    weatherObj = extract_weather_data(dict)

    return f"The weather in {city} is {weatherObj.temperature} degrees and Sunny."


####
# URL  : https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22

from pydantic import BaseModel

class WeatherData(BaseModel):
    temperature: float
    description: str
    humidity: int
    wind_speed: float

def extract_weather_data(json_data: dict) -> WeatherData:
    """
    从JSON数据中提取天气信息并返回WeatherData对象
    """
    return WeatherData(
        temperature=json_data["main"]["temp"],
        description=json_data["weather"][0]["description"],
        humidity=json_data["main"]["humidity"],
        wind_speed=json_data["wind"]["speed"]
    )


import requests

def get_weather_json(location: str) -> dict:
    """
    从OpenWeatherMap API获取天气数据
    
    Args:
        location: 城市名称，如"London,uk"
        appid: OpenWeatherMap API key
    
    Returns:
        包含天气信息的JSON数据
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units":"metric",
        "appid": appid
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # 如果请求失败会抛出异常
    return response.json()

if __name__ == "__main__":
    json = get_weather_json('Hongkong')
    print(json)