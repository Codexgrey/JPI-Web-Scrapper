import requests
from bs4 import BeautifulSoup as BS
import csv


#--- Setting up writer object to write data into csv file
newfile = open("C:/Users/user/Desktop/DATA - SCIENCE/Assignments/Solutions/Week 8/ASM7A - Jumia Smartphones.csv", mode = "w", encoding = "utf-8", newline = "")
pen = csv.writer(newfile)
pen.writerow(["S|N", "brand", "specifications", "old price", "discount", "new price", "ratings"])
phones_data = []
index = 1


#--- Scraping multiple pages
for num in range(1, 51):
    #--- Getting urls from pagination
    url = ""
    if num == 1:
        url = "https://www.jumia.com.ng/smartphones/"
    else:
        url = f"https://www.jumia.com.ng/smartphones/?viewType=grid&page={num}#catalog-listing"
    print(url)
    

    #--- Establishing connection to desired weblink
    headers = requests.utils.default_headers()
    headers.update({
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Mobile Safari/537.36"
    }) 
    res = requests.get(url, headers) 
        # print(res) - checking connection


    #--- Preparing soups
    condiments = BS(res.content, features = "lxml")
    recipe = condiments.find("div", attrs = {"class": "-paxs row _no-g _4cl-3cm-shs"})
    soupslist = recipe.find_all("article")
        # soupslist = recipe.select("article.prd._fb") - using select, allows us to use CSS selectors
        # print(len(soupslist))


    #--- Cooking soups for smartphones data
    for soup in soupslist:
        phone_details = soup.find('a')

        # Brand
        try:
            phone_brand = phone_details.get("data-brand")
        except:
            phone_brand = None

        # Specifications
        try:
            phone_spec = phone_details.get("data-name")
        except:
            phone_spec = None

        # Old price
        try:
            op_div = soup.find("div", attrs = {"class": "old"})
            op_raw = op_div.text
            oldPrice = int(op_raw.lstrip("₦ ").replace(",", ""))
        except:
            oldPrice = None

        # Discount
        try:
            dc_div = soup.find("div", attrs = {"class": "tag _dsct _sm"})
            discount = dc_div.text
        except:
            discount = None

        # New price
        try:
            np_div = soup.find("div", attrs = {"class": "prc"})
            np_raw = np_div.text
            newPrice = int(np_raw.lstrip("₦ ").replace(",", ""))
        except:
            newPrice = None

        # Ratings
        try:
            rt_div = soup.find("div", attrs = {"class": "stars _s"})
            rt_raw = rt_div.text
            phone_rating = float(rt_raw.split(" ")[0])
        except:
            phone_rating = None

        # Writing into csv
        phones_data.append([index, phone_brand, phone_spec, oldPrice, discount, newPrice, phone_rating])
        index += 1


pen.writerows(phones_data)
newfile.close()



