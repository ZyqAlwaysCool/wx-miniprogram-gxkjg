'''
Author: zyq
Date: 2024-11-26 08:53:57
LastEditors: zyq
LastEditTime: 2024-11-26 09:01:14
FilePath: /project/wx-miniprogram-gxkjg/config.py
Description: config

Copyright (c) 2024 by zyq, All Rights Reserved. 
'''

#exhibits list
EXHIBITS_LIST_URL = 'https://zskjgxcx.cdstm.cn/adaptor/adaptor/activity/selectWeChatExhibitsList'
EXHIBITS_LIST_HEADERS = {
    #your request headers here
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': '',
    'Content-Type': 'application/json',
    'X-Tt-Request-Id': '',
    'clientType': ''
}

#exhibits detail info
EXHIBITS_INFO_URL = 'https://zskjgxcx.cdstm.cn/adaptor/adaptor/activity/selectExhibitsAppById'
EXHIBITS_INFO_HEADERS = {
    #your request headers here
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': '',
    'Content-Type': 'application/json',
    'clientType': ''
}
