# -*- coding:utf-8 -*-

import urllib
import json
import unicodedata

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

q = u'{query}'
q2 = unicodedata.normalize('NFC', q)
q3 = urllib.quote(q2.encode('utf-8'))

unparsed = urllib.urlopen(u'http://ac.dict.naver.com/enedict/ac?q=%s&q_enc=utf-8&st=11001&r_format=json&r_enc=utf-8&r_lt=10001&r_unicode=0&r_escape=1' % q3).read()
obj = json.loads(unparsed)

elems = []
i = 0

for item in obj["items"][0]:
    if len(item) < 2:
        continue

    en = item[0][0]
    ko = item[1][0]
    ko = ko.replace('<b>', '') 
    ko = ko.replace('</b>', '') 

    word = u'%s: %s' %(en, ko) 

    s = u'<item uid="%s_%d" arg="%s"><title>%s</title><subtitle>네이버 영어 사전에서 &quot;%s&quot; 검색</subtitle><icon>icon.png</icon></item>' % (en, i, en, word, en)
    elems.append(s)
    i += 1

if len(elems) == 0:
    s = u'<item uid="%s_%d" arg="%s"><title>%s</title><subtitle>네이버 영어 사전에서 &quot;%s&quot; 검색</subtitle><icon>icon.png</icon></item>' % (q3, 0, q3, q3, q3)
    elems.append(s)

print "<items>"

for elem in elems:
    print elem

print "</items>"
