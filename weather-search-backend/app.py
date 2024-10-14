from flask import Flask, request, jsonify, Response
import requests
import re
from translate import Translator
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# 从环境变量获取 API 密钥
ACCESS_KEY = "b2b481e0c75c88ab9696d3816dfc1fec"

# API URL
RESOURCE_URL = "http://api.weatherstack.com/current"

res = {
    "data": None,
    "msg": "success",
    "success": True
}

@app.route('/weather', methods=["POST"])
def get_weather():
    try:
        if request.method != "POST":
            return jsonify({"success": False, "msg": "Method Not Allowed"}), 405
        # 获取请求数据
        obj = request.get_json(force=True)
        city = obj.get("city", None)
        if not city:
            res.update(msg="Bad Request, city is required")
            return jsonify(res), 400

        # 检查传过来的中是否存在其他参数
        for key in obj:
            if key not in ["city"]:
                res.update({"success": False, "msg": "Unauthorized, does not support this API params: {}".format(key)})
                return jsonify(res), 401

        # 将中文转化为英文再请求 数据源不支持中文查询
        if re.match(r"^[\u4e00-\u9fa5]+$", city):
            translator = Translator(from_lang="zh", to_lang="en")
            city = translator.translate(city)

        # 构造请求参数
        params = {
            "access_key": ACCESS_KEY,
            "query": city,
            # "language": "zh"
        }

        # 发送请求
        # response = requests.get(RESOURCE_URL, params=params)
        response = {'request': {'type': 'City', 'query': 'Guangzhou, China', 'language': 'en', 'unit': 'm'}, 'location': {'observation_time': '下午05:46', 'weather_descriptions': ['清除'], 'country': '中國', 'region': '广东', 'name': '广州'}, 'current': {'observation_time': '下午05:46', 'weather_descriptions': ['清除'], 'country': '中國', 'region': '广东', 'name': '广州'}}

        # response.raise_for_status()  # 检查请求是否成功
        # 数据源返回的数据英文，先将英文翻译成中文
        translator = Translator(from_lang="en", to_lang="zh")
        # q = 1/0
        # print(response.json())
        # if response.json().get("success") is False:
        #     res.update({"success": False, "msg": f"{translator.translate(response.json().get('error',{}).get('info', '未知错误'))}"})
        #     return jsonify(res), 400
        data = response
        # data = response.json()

        # 获取当前天气信息
        current_weather = data.get("current", {})
        location_info = data.get("location", {})

        # 翻译特定字段
        translated_data = {
            "observation_time": translator.translate(current_weather.get("observation_time", "")),
            "weather_descriptions": [translator.translate(desc) for desc in
                                     current_weather.get("weather_descriptions", [])],
            "country": translator.translate(location_info.get("country", "")),
            "region": translator.translate(location_info.get("region", "")),
            "name": translator.translate(location_info.get("name", ""))
        }

        # 更新原始数据
        data.update(current=translated_data)
        data.update(location=translated_data)
        # current_weather.update(translated_data)
        # location_info.update(translated_data)
        # print(response.json())
        print(data)
        res.update(data=data)
        return jsonify(res), 200
    except requests.RequestException as e:
        res.update({"success": False, "msg": f"{str(e)}"})
        # 处理请求异常
        return jsonify(res), 500


if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), port=8443, debug=True)

