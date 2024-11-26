'''
Author: zyq
Date: 2024-11-25 15:20:54
LastEditors: zyq
LastEditTime: 2024-11-26 08:53:32
FilePath: /project/wx-miniprogram-gxkjg/json_parser.py
Description: 
解析原始的展品列表json数据, 需要case by case修改
Copyright (c) 2024 by zyq, All Rights Reserved. 
'''
import json
import re
import os
import xml.etree.ElementTree as ET
import requests
from tqdm import tqdm

def extract_text_from_p_tag(xml_string):
    try:
        xml_string = xml_string.replace('&nbsp;', ' ')
        root = ET.fromstring(f'<root>{xml_string}</root>')
        result = ""
        for p_element in root.findall('p'):
            for span_element in p_element.findall('span'):
                if span_element.text:
                    result += span_element.text.strip()
            if p_element.text:
                result += p_element.text.strip()
            if p_element.tail:
                result += p_element.tail.strip()
        return result
    except ET.ParseError as e:
        print('err_xml_string=({})'.format(xml_string))
        
    
def parse_json(file_path):
    data_res = []
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        for exhibit in json_data['activityExhibitsList']:
            exhibit_info = {}
            exhibit_info['name'] = exhibit['exhibitsName']
            exhibit_info['intro'] = extract_text_from_p_tag(exhibit['exhibitsIntroduce'])
            exhibit_info['pic'] = exhibit['exhibitsPictures'][2:-2]
            exhibit_info['map_coord'] = exhibit['mapCoordinates']
            data_res.append(exhibit_info)
    return data_res
            

if __name__ == '__main__':
    all_exhibits = []
    dir_path = './raw_json_data'
    for fname in tqdm(os.listdir(dir_path)):
        real_fpath = dir_path + '/' + fname
        result = parse_json(real_fpath)
        
        for r in result:
            all_exhibits.append(r)
    
    export_json_path = './all_exhibits.json'
    with open(export_json_path, 'w', encoding='utf-8') as f:
        json.dump({'exhibits_info': all_exhibits}, f, ensure_ascii=False, indent=4)