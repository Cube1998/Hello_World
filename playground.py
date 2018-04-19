
#!/usr/bin/env python
# encoding=utf-8
import codecs
import urllib
import urllib2
import re
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'http://book.douban.com/top250/'


def download_page(url):
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')

def getContents(html):
	soup = BeautifulSoup(html, "html.parser")
	re_contents = re.compile(r'<a href=".*?" onclick=.*?title="(.*?)".*?<p class="pl">(.*?)</p>.*?<span class="inq">(.*?)</span>',re.S)
	next_pattern = re.compile(r'<a href="(.*?)">',re.S)
	#re_author = re.compile(r'<p class="pl">(.*?)</p>',re.S)
	#re_quote = re.compile(r'<span class="inq">(.*?)</span>',re.S)
	name_results = re.findall(re_contents,html)
	next_page = soup.find('span', attrs={'class': 'next'}).find('a')

	if next_page:
		#a = re.findall(next_pattern,next_page[''])
		DOWNLOAD_URL = next_page['href']
		return name_results,DOWNLOAD_URL
	else:
		return name_results,None
def main():
	url = DOWNLOAD_URL
	with codecs.open('book_list', 'wb', encoding='utf-8') as fp:
		while url:
			html = download_page(url)
			books, url = getContents(html)
			
			fp.write(u'{books}\n'.format(books='\n'.join(['\n'.join(elems) for elems in books])))
			#for x in books:
				#print  x[0],'\n',x[1],'\n',x[2],'\n'
main()
