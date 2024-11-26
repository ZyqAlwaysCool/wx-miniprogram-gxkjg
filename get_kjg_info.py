'''
Author: zyq
Date: 2024-11-25 14:57:46
LastEditors: zyq
LastEditTime: 2024-11-26 09:02:26
FilePath: /project/wx-miniprogram-gxkjg/get_kjg_info.py
Description: 
获取科技馆页面信息的原始json数据, 存放在raw_json_data中
需先通过抓包工具获取请求api信息, 使用的是fiddler抓包

Copyright (c) 2024 by zyq, All Rights Reserved. 
'''
import requests
import json
from tqdm import tqdm
import time
import os
from config import *

def get_exhibit_locate(exhibits_id):
    '''
    通过展品的id获取展品的具体位置
    '''
    data = {
        "exhibitsId": "",
        "reqInfo": {
            "activityId": "",
            "activityType": "",
            "adminId": "",
            "businessGroup": "",
            "interfaceType": "",
            "password": "",
            "requestType": "",
            "userId": "",
            "userName": "",
            "venueId": "",
            "volunteerId": "",
            "entryType": "6",
            "accessModule": "2"
        }
    }
    
    headers = EXHIBITS_INFO_HEADERS
    
    url =EXHIBITS_INFO_URL #展品详情页面
    
    data['exhibitsId'] = exhibits_id
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        res = response.json()
        return res['ExhibitsInfo']['mapCoordinates']
    else:
        return ""


def get_all_info():
    total_page = 38
    data = {
        "areaCode": "450000",
        "pageInfo": {
            "currentPage": 1,
            "pageSize": 20,
            "totalCount": 0,
            "totalPage": 0
        },
        "userId": ""
    }
    for i in tqdm(range(total_page)):
        current_page = i + 1
        print('=====start page {}====='.format(current_page))
        data['pageInfo']['currentPage'] = current_page
        response = requests.post(EXHIBITS_LIST_URL, headers=EXHIBITS_LIST_HEADERS, json=data)
        if response.status_code == 200:
            res = response.json()
            for i in res['activityExhibitsList']:
                if i['mapCoordinates'] == '':
                    i['mapCoordinates'] = get_exhibit_locate(i['exhibitsId'])
            if not os.path.exists('./raw_json_data'):
                os.mkdir('./raw_json_data')
            fpath = './raw_json_data/page_{}_res_new.json'.format(current_page)
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(res, f, ensure_ascii=False, indent=4)
            print('=====write to json file, page {} done====='.format(current_page))
        else:
            print(response.status_code)
        print('=====end page {}====='.format(current_page))
        time.sleep(1)

if __name__ == '__main__':
    get_all_info()