# -*- coding: UTF-8 -*-
'''
Author: Superman
Date: 2024/10/14 10:06
LastEditTime: 2024/10/14 10:06
LastEditors: Superman
Description: 
dataSource: 
FilePath: test_api.py
'''
import requests


url = "http://127.0.0.1:5000"
data = {
    "city": "Shanghai",
}

result = requests.post(url,data=data)
print(result.text)