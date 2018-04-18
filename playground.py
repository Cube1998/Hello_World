
#!/usr/bin/env python
# encoding=utf-8
import codecs
import urllib
import urllib2
import re


DOWNLOAD_URL = 'http://movie.douban.com/top250/'


def download_page(url):
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')

def getContents(html):
	pattern = re.compile(r'<span class="title">(.*?)</span>.*?<span class="inq">(.*?)</span>',re.S)
	results = re.findall(pattern,html)
	for x in results :
		print x[0],'\n',x[1]


getContents(download_page(DOWNLOAD_URL))
