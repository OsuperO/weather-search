from flask import Flask, request, jsonify
import requests
import re
from translate import Translator
from flask_cors import CORS
from flasgger import Swagger, swag_from
from source_config import ACCESS_KEY, RESOURCE_URL


app = Flask(__name__)
CORS(app)   # 允许跨域



# 用于封装返回数据
res = {
    "data": None,
    "msg": "success",
    "success": True
}

# 未奏效，报错'NoneType' object has no attribute 'Dict'
# class WeatherResponse(Schema):
#     data = fields.Dict(required=False, allow_none=True)
#     msg = fields.String()
#     success = fields.Boolean()

# 配置swagger
app.config['SWAGGER'] = {
    'title': 'Weather API',
    'uiversion': 3,
    # 'definitions': {
    #     'WeatherResponse': WeatherResponse
    # }
}
swagger = Swagger(app)

@app.route('/weather', methods=["POST"])
@swag_from({
    'tags': ['Weather'],
    'description': '城市天气查询',
    'parameters': [
        {
            'name': 'city',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'city': {
                        'type': 'string',
                        'description': '城市名称'
                    }
                }
            }
        }
    ],
    'responses': {
        '200': {
            'description': 'Success',
            'schema': {
                '$ref': '#/definitions/WeatherResponse'
            }
        },
        '400': {
            'description': '错误请求'
        },
        '401': {
            'description': '无权限'
        },
        '405': {
            'description': '该方法不被允许'
        },
        '500': {
            'description': '服务器错误'
        }
    }
})
def get_weather():
    try:
        if request.method != "POST":
            return jsonify({"success": False, "msg": "Method Not Allowed"}), 405
        # 获取请求数据
        obj = request.get_json(force=True)
        city = obj.get("city", None)
        if not city:
            res.update(msg="错误请求，city参数是必须的")
            return jsonify(res), 400

        # 检查传过来的中是否存在其他参数
        for key in obj:
            if key not in ["city"]:
                res.update({"success": False, "msg": "无权限使用以下参数: {}".format(key)})
                return jsonify(res), 401

        # 将中文转化为英文再请求 数据源不支持中文查询
        if re.match(r"^[\u4e00-\u9fa5]+$", city):
            translator = Translator(from_lang="zh", to_lang="en")
            city = translator.translate(city)

        # 构造请求参数
        params = {
            "access_key": ACCESS_KEY,
            "query": city,
            # "language": "zh"  //订阅的key没有权限使用中文查询
        }

        # 发送请求获取天气数据
        response = requests.get(RESOURCE_URL, params=params)
        translator = Translator(from_lang="en", to_lang="zh")
        # 如果请求失败，则将错误信息进行翻译并返回
        if response.json().get("success") is False:
            res.update({"success": False, "msg": f"{translator.translate(response.json().get('error',{}).get('info', '未知错误'))}"})
            return jsonify(res), 400

        data = response.json()

        # 由于翻译模块很慢，所以只针对位置信息进行翻译
        location_info = data.get("location", {})

        # 翻译特定字段
        translated_data = {
            "country": translator.translate(location_info.get("country", "")),
            "region": translator.translate(location_info.get("region", "")),
            "name": translator.translate(location_info.get("name", ""))
        }

        # 更新到原始数据
        data.update(location=translated_data)

        res.update(data=data)
        return jsonify(res), 200
    except requests.RequestException as e:
        res.update({"success": False, "msg": f"{str(e)}"})
        # 请求异常，返回服务器错误
        return jsonify(res), 500


if __name__ == '__main__':
    # 使用https协议传输数据
    app.run(ssl_context=('cert.pem', 'key.pem'), port=8443, debug=True)
    # app.run(debug=True)


