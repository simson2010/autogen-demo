import json
from pathlib import Path

full_data = None

def read_location_mapping() -> dict:
    """
    从../mapping/location_mapping.json读取文件内容
    
    Returns:
        解析后的JSON数据
    """
    print("getting addresss map")
    file_path = Path(__file__).parent.parent / "mapping" / "location_mapping.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

async def map_address(city: str) -> str :
    global full_data

    if full_data is None:
        full_data = read_location_mapping()
    
    print(f"in param: {city}")
    city = 'mo' if city == "Macau" else 'fr'
    
    if city in full_data:
        return full_data[city]
    return ""
    

