#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = 'yukun'

import json
from datetime import datetime

from .utils import parse_url


def get_img_url():
    params = {
        'format': 'js',
        'idx': 0,
        'n': 1,
        'pid': 'hp'
    }
    base_url = 'https://www.bing.com/HPImageArchive.aspx'
    resp = parse_url(base_url, params)
    result = json.loads(resp)
    if result:
        bing_url = 'https://www.bing.com'
        img_url = bing_url + result['images'][0]['url']
        img_copyright = result['images'][0]['copyright']
        return {'url': img_url, 'copyright': img_copyright}

    return None


def get_img_info():
    url = 'https://cn.bing.com/cnhp/coverstory/'
    resp = parse_url(url)
    result = json.loads(resp)
    if result:
        date = datetime.now().strftime('%Y-%m-%d')
        title = result.get('title', '图片')
        attribute = result.get('attribute', '')
        para = result.get('para', '')
        country = result.get('Country', '')
        city = result.get('City', '')
        continent = result.get('Continent', '')
        return {
            'date': date,
            'title': title,
            'attribute': attribute,
            'para': para,
            'country': country,
            'city': city,
            'continent': continent
        }
    return None


def main():
    image = get_img_url()
    info = get_img_info()

    return {'image': image, 'info': info}


data = main()
print(data)
