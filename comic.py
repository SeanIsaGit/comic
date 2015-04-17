import urllib
import urllib2
import time
from bs4 import BeautifulSoup
import os
import re

def get_comic(url):
    com_site = urllib2.urlopen(url)
    
    page_data = com_site.read()
    soup = BeautifulSoup(page_data, 'html.parser')
    
    images = []
    
    
    for link in soup.findAll('img'):
        
        images.append(link.get('src'))
        
        
    comic = images[1]
    file_name = fil = re.match(r'.*/(.*\.(jpg|png|gif))', comic).group(1)
    urllib.urlretrieve("http:"+comic, directory+file_name)
    print file_name + " retrieved"
    time.sleep(.5)
    
    
comic = None
page_data = None
comic_num = 0
try_num = 0
os.makedirs('C:\\Users\\Owner\\Desktop\\Comics\\')
directory = "C:\\Users\\Owner\\Desktop\\Comics\\"

while comic_num <=5000:
    comic_num += 1
    url = "http://www.xkcd.com/" + str(comic_num)
    try:
        get_comic(url)
        try_num = 0
    except:
        print 'Comic number ' + str(comic_num) + ' does not exist'
        try_num += 1
    if try_num == 5:
        break
    if try_num == 0:
        print "**********"











