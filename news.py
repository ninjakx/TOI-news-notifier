from bs4 import BeautifulSoup
import subprocess
import time
from urllib.request import urlopen
  
def bsoup_get_html():
    global list_headline
    get_url = "http://timesofindia.indiatimes.com/"
    url = urlopen(get_url)
    content = url.read()
    soup = BeautifulSoup(content,"lxml")
    list_headline = soup.find('ul',attrs={'class':'list9'}) #get all the text under ul tag

def main():
    bsoup_get_html()
    list_headline
    match='new_latest#'
    for news in list_headline.findAll("li"):    
        content=news.find('a')
        if content.has_attr('pg') and content['pg'].startswith(match):
            notifyme(*content.contents)
            time.sleep(10)
  
def notifyme(msg):
    subprocess.Popen(['notify-send',msg])
    return

while(1):
    main()
    time.sleep(1800)        #every half an hour will scrap the page
      


