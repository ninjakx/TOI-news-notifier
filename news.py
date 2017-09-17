from bs4 import BeautifulSoup
import subprocess
import time
from urllib.request import urlopen
import csv
import pandas as pd
import re
import sys
import os

global i 
i=0
  
def bsoup_get_html():
    global list_headline
    get_url = "http://timesofindia.indiatimes.com/"
    url = urlopen(get_url)
    content = url.read()
    soup = BeautifulSoup(content,"lxml")
    list_headline = soup.find('ul',attrs={'class':'list9'}) #get all the text under ul tag

filename = 'news.csv'

def main():
 
    bsoup_get_html()
    list_headline
    match='new_latest#'
    ln=0
    for news in list_headline.findAll("li"):    
        content=news.find('a')
        
        if content.has_attr('pg') and content['pg'].startswith(match):
           
            if os.path.exists(filename):
      
                flag=0
                with open(filename,'r') as csv_file:
                    reader=csv.reader(csv_file)
                    for row in reader:
                        row=((row[0])[2:-2]).replace(r"\xa0", " ")
           
                        if (content.contents[0]) ==(row):
                            ln=ln+1
                     
                            flag=1
                            break

                if flag==0:

                        with open('news.csv','a',newline='') as csv_file:
                                writer = csv.writer(csv_file)
                                writer.writerow([content.contents])
                                break
  
            else:        
           
                with open('news.csv','a',newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow([content.contents])
        if ln > 1:
           return
                         
def notifyme(msg):
    subprocess.Popen(['notify-send',msg])
    return

while(1):
  try:
    main()
    char1='['
    char2=']'
    with open(filename,'r') as csv_file:
        reader=csv.reader(csv_file)
        for row in reader:
            row=((row[0])[2:-2]).replace(r"\xa0", " ")
            lines = [line for line in csv_file][i:i+4]
            #print(lines)
            
            for news in lines:
                
                news=(news[news.find(char1)+1 : news.find(char2)])       
                news=news[1:-1]
                news=news.replace('"','') 
                #print(news)
                notifyme(news)
                    
            if len(lines)!=0:
                i=i+4
            time.sleep(20)
            
    time.sleep(1800)        #every half an hour will scrap the page
  except: 
      os.remove('news.csv')
      sys.exit()
