#!/usr/bin/env python3
# coding: utf-8

import requests
import json
from bs4 import BeautifulSoup

USER='username'
PASS='password'
IP='192.168.1.1'

with requests.Session() as s:

    params = {
        'user': USER,
        'user1': USER,
        'pws': PASS,
    }

    r = s.post('http://'+IP+'/cgi-bin/login.exe', params)
    r = s.get('http://'+IP+'/adsl_status.stm')

    soup = BeautifulSoup(r.content, 'lxml')

    tds = [row.findAll('td') for row in soup.findAll("a", {"name": "rate_i"})[0].findAll('tr')]
    rate = { td[0].string: td[1].string for td in tds }

    defects = dict()
    tds = soup.findAll("a", {"name": "defect_i"})[0].findAll('td')
    for i in range(0,len(tds),3):
        defects[tds[i].text] = (tds[i+1].text ,tds[i+2].text)

r = s.get('http://'+IP+'/cgi-bin/logout.exe')
s.close()

f = open("/var/log/netfaster3.data", "w")
jdata={"rate" :rate, "defects": defects}
#f.write(json.dumps(jdata, sort_keys=True, indent=4, ensure_ascii=False))
f.write(json.dumps(jdata))
f.close()
