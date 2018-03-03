#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = 'yukun'

import requests
from requests.exceptions import ConnectionError


def parse_url(url, data=None):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	}
	try:
		resp = requests.get(url, headers=headers, params=data)
		if resp.status_code == 200:
			return resp.text
		return None
	except ConnectionError:
		print('Error.')
	return None
