from datetime import datetime as dt
from bs4 import BeautifulSoup as BS
import requests
import csv

#--- Setting up writer object to write data into csv file
newfile = open("C:/Users/user/Desktop/DATA - SCIENCE/Assignments/Solutions/Week 8/ASM7B1 - Article Links.csv", mode = "w", encoding = "utf-8", newline = "")
pen = csv.writer(newfile)
pen.writerow(["S|N", "source", "link", "date"])
links_data = []
index = 1


#-- NOTE - Punch Newspaper
for num in range(1, 65):
    # getting urls from pagination
    url = ""
    if num == 1:
        url = "https://punchng.com/?s=banditry+kidnapping"
    else:
        url = f"https://punchng.com/page/{num}/?s=banditry+kidnapping"
    print(f"PUNCH: {url}")


    #--- Establishing connection to desired weblink
    headers = requests.utils.default_headers()
    headers.update({
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }) 
    res = requests.get(url, headers) 
        # print(res) - checking connection

    
    #--- Preparing soups
    condiments = BS(res.content, features = "lxml")
    recipe = condiments.find("div", attrs = {"class": "entries-grid row"})
    soupslist = recipe.find_all("div", attrs = {"class": "grid-item"})
        # print(len(soupslist))


    #--- Cooking soups for news data
    for soup in soupslist:
        news_details = soup.find("img")

        # news source
        source = "Punch Newspapers"

        # news link
        try:
            newslink = soup.find("a").get("href")
        except:
            newslink = None
        
        # news date
        try:
            dt_str = news_details.get("data-src")
            year = dt_str.split("uploads")[1].split("/")[1]
            month = dt_str.split("uploads")[1].split("/")[2]
            day = (dt_str.split("uploads")[1].split("/")[3])[:2]
            newsdate = dt(int(year), int(month), int(day)).strftime("%Y %B %d")
        except:
            dt_str = None
            year = None
            month = None
            day = None
            newsdate = None
            
        # writing into csv
        links_data.append([index, source, newslink, newsdate])
        index += 1



#-- NOTE - Information Nigeria Blog
for num in range(1, 12):
    # getting urls from pagination
    url = ""
    if num == 1:
        url = "https://www.informationng.com/?s=banditry+kidnapping"
    else:
        url = f"https://www.informationng.com/page/{num}?s=banditry+kidnapping"
    print(f"BLOG: {url}")

    #--- Establishing connection to desired weblink
    headers = requests.utils.default_headers()
    headers.update({
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }) 
    res = requests.get(url, headers) 
        # print(res) - checking connection


    #--- Preparing soups
    condiments = BS(res.content, features = "lxml")
    recipe = condiments.find("div", attrs = {"class": "td-ss-main-content"})
    soupslist = recipe.find_all("div", attrs = {"class": "td_module_16 td_module_wrap td-animation-stack"})
        # print(len(soupslist))


    #--- Cooking soups for news data
    for soup in soupslist:
        # news source
        blogsource = "Information Nigeria Blog"

        # news link
        try:
            blogdiv = soup.find("div", attrs = {"class": "item-details"})
            bloglink = blogdiv.find("a").get("href")
        except:
            blogdiv = None
            bloglink = None

        # news date
        try:
            blogdate = soup.find("time").text
        except:
            blogdate = None

        # writng into csv
        links_data.append([index, blogsource, bloglink, blogdate])
        index += 1
        

#--- Writing all rows into and closing csv file
pen.writerows(links_data)
newfile.close()





