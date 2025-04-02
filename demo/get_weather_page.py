import requests
import json

def get_city_data(url):
    # 设置请求头
    headers = {
        "Referer": "https://www.weather.com.cn/",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"
    }

    # 发送HTTP请求获取页面内容
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 设置编码为UTF-8
    js_content = response.text
    
    # 提取JSON数据
    # 由于返回的内容以 "var city_data=" 开头，我们需要去掉这部分
    json_data = js_content.replace("var city_data =", "")
    
    # 解析JSON
    city_data = json.loads(json_data)
    return city_data

# 示例URL
url = 'https://j.i8tq.com/weather2020/search/city.js'
city_data = get_city_data(url)
print(city_data)
# 打印部分城市数据
for province, cities in city_data.items():
    print(f"省份: {province}")
    if province not in ['北京','上海','重庆','天津']:
        for city, info in cities.items():
            info = info[city]
            print(f"城市: {city}, 区域ID: {info['AREAID']}, 中文名: {info['NAMECN']}")
        break  # 仅打印一个省份的示例
    # else :
    #     cities = cities[province]
    #     for city, info in cities.items():
    #         print(f"城市: {city}, 区域ID: {info['AREAID']}, 中文名: {info['NAMECN']}")
    #     break 



def get_temperature(url):
    # 设置请求头
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "f_city=%E9%93%9C%E4%BB%81%7C101260601%7C",
        "Host": "d1.weather.com.cn",
        "Referer": "https://www.weather.com.cn/",
        "Sec-Fetch-Dest": "script",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    # 发送HTTP请求获取页面内容
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # 设置编码为UTF-8
    json_content = response.text

    print(json_content)
    # 提取JSON数据
    # 由于返回的内容以 "var dataSK=" 开头，我们需要去掉这部分
    json_data = json_content.replace("var dataSK=", "")

    # 解析JSON
    import json
    data = json.loads(json_data)

    # 获取温度值
    temperature = data.get("temp")
    return temperature

# 示例URL
import time

# 获取当前时间戳（毫秒级）
timestamp = int(time.time() * 1000)
print(f"当前时间戳（毫秒）: {timestamp}")

url = f'https://d1.weather.com.cn/sk_2d/101010100.html?_={timestamp}'
temperature = get_temperature(url)
print(f"当前温度: {temperature}")

# 示例URL