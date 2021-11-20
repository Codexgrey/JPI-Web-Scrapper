from datetime import datetime as dt
from bs4 import BeautifulSoup as BS
import requests
import csv

#--- Setting up writer object to write data into csv file
newfile = open("C:/Users/user/Desktop/DATA - SCIENCE/Assignments/Solutions/Week 8/ASM7B2 - Articles.csv", mode = "w", encoding = "utf-8", newline = "")
pen = csv.writer(newfile)
pen.writerow(["S|N", "source", "article", "date"])
articles_data = []
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
    condiments = BS(res.content, features="lxml")
    recipe = condiments.find("div", attrs={"class": "entries-grid row"})
    soupslist = recipe.find_all("div", attrs={"class": "grid-item"})
        # print(len(soupslist))


    #--- Cooking soups, to find url for news data
    for soup in soupslist:
        # getting into each article's url 
        soup_url = soup.find("a").get("href")
        soup_res = requests.get(soup_url, headers)
            # print(soup_res, soup_url)

        # preparing (n)ews (a)rticle soup
        na_condiments = BS(soup_res.content, features="lxml")
        na_recipe = na_condiments.find("main", attrs={"class": "site-main"})
        na_soup = na_recipe.find("div", attrs={"class": "entry-content"})

        # setting article source 
        source = "Punch Newspapers"

        # getting news article from paragraphs
        try:
            ptags = na_soup.find_all("p")

            # unifying all paragraphs
            paragraphs = []
            for ptag in ptags:
                paragraphs.append(ptag.text)
                string = " * ".join(paragraphs)

            newsarticle = string
        except:
            ptags = None
            paragraphs = None
            string = None
            newsarticle = None

        # getting article date
        try:
            datediv = na_soup.find("span", attrs={"class": "entry-date"})
            newsdate = datediv.find("span").text
        except:
            datediv = None
            newsdate = None

        # writing into csv
        articles_data.append([index, source, newsarticle, newsdate])
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
    condiments = BS(res.content, features="lxml")
    recipe = condiments.find("div", attrs={"class": "td-ss-main-content"})
    soupslist = recipe.find_all("div", attrs={"class": "td_module_16 td_module_wrap td-animation-stack"})
        # print(len(soupslist))


    #--- Cooking soups, to find url for blog data
    for soup in soupslist:
        # getting into each article's url
        soup_url = soup.find("a").get("href")
        soup_res = requests.get(soup_url, headers)
            # print(soup_res, soup_url)

        # preparing (b)log (a)rticle soup
        ba_condiments = BS(soup_res.content, features="lxml")
        ba_recipe = ba_condiments.find("div", attrs={"class": "td-ss-main-content"})
        ba_soup = ba_recipe.find("article")

        # setting blog article source
        blogsource = "Information Nigeria Blog"

        # getting blog article from paragraphs
        try:
            ba_div = ba_soup.find("div", attrs={"class": "theiaPostSlider_preloadedSlide"}) 
            ptags = ba_div.find_all("p")
            
            # unifying all paragraphs
            paragraphs = []
            for ptag in ptags:
                paragraphs.append(ptag.text)
                string = " * ".join(paragraphs)

            blogarticle = string
        except:
            ba_div = None
            ptags = None
            paragraphs = None
            string = None
            blogarticle = None

        # getting blog article date
        try:
            ba_datespan = ba_soup.find("span", attrs={"class": "td-post-date"})
            blogdate = ba_datespan.find("time").text
        except:
            ba_datespan = None
            blogdate = None

        # writng into csv
        articles_data.append([index, blogsource, blogarticle, blogdate])
        index += 1
      
        
#--- Writing all rows into and closing csv file
pen.writerows(articles_data)
newfile.close()
