import requests
import json
import random

class hangang:
    def now():
        try:
            url = "https://api.hangang.msub.kr"
            res = json.loads(requests.get(url).text)
            color_code = {
                'coolest': 0x82f3ff,
                'cool': 0x40b2f5,
                'warm': 0xf79925,
                'hot': 0xfc5305
            }
            if res['status'] == 'success':
                temp = float(res['temp'])
                data = [
                    res['station'],
                    res['time']
                ]
                if temp <= 5.0:
                    color = color_code['coolest']
                elif temp <= 12.0:
                    color = color_code['cool']
                elif temp <= 20.0:
                    color = color_code['warm']
                else:
                    color = color_code['hot']
            else:
                temp = 99
                data = []
                color = -1
            return temp, data, color
        except Exception as e:
            return 99, e, -1

    def openapi():
        url = "http://openapi.seoul.go.kr:8088/{API_KEY}/json/WPOSInformationTime/1/5"
        color_code = {
            'coolest': 0x82f3ff,
            'cool': 0x40b2f5,
            'warm': 0xf79925,
            'hot': 0xfc5305
        }
        try:
            res = json.loads(requests.get(url).text)
            if res['WPOSInformationTime']['RESULT']['CODE'] == 'INFO-000':
                temp_num = random.randint(3, 4)
                temp = float(res['WPOSInformationTime']['row'][temp_num]['W_TEMP'])
                data_temp = res['WPOSInformationTime']['row'][temp_num]
                data = [
                    data_temp['SITE_ID'],
                    data_temp['MSR_TIME']
                ]
                if temp <= 5.0:
                    color = color_code['coolest']
                elif temp <= 12.0:
                    color = color_code['cool']
                elif temp <= 20.0:
                    color = color_code['warm']
                else:
                    color = color_code['hot']
                return temp, data, color
            else:
                temp = 99
                data = []
                color = -1
                return temp, data, color
        except Exception as e:
            return 99, e, -1

