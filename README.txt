*** PROJECT STRUCTURE ***
> I've written this to enable you find your way around easily...

ASM7A = Assignment 7A Jumia Smartphones
ASM7B1 = Assignment 7B Article links on Punch & Infomation Nigeria Blog related to {banditry, kidnappings}
ASM7B2 = Assignment 7B Articles on Punch & Infomation Nigeria Blog related to {banditry, kidnappings}

ASM7B1 = {
    LINE 006 = Setting up writer object to write data into csv file,

    LINE 014 = Article links WebScraper, Punch Newspapers 
               LINE 030 = Weblink Connection Established
               LINE 041 = Scraping [source, link, date]
               LINE 068 = Writing into csv

    LINE 074 = Article links WebScraper, Information Nigeria Blog
               LINE 089 = Weblink Connection Established
               LINE 100 = Scraping [source, link, date]
               LINE 119 = Writing into csv
 
    
    LINE 124 = Writing all rows into and closing csv file
}


ASM7B2 = {
    LINE 006 = Setting up writer object to write data into csv file

    LINE 014 = Articles WebScraper, Punch Newspapers
               LINE 030 = Weblink Connection Established
               LINE 041 = Cooking soups, to find url for news data

               LINE 045 = Soup Weblink Connection Established
                          >>> Naming Convention
                              "na": abbrv for news article
                              "condiments, recipe": blocks of code housing required data
                              "string": all article paragraphs joined

               LINE 053 = Scraping [source, article, date]
               LINE 081 = Writing into csv

    LINE 087 = Articles WebScraper, Information Nigeria Blog
               LINE 102 = Weblink Connection Established
               LINE 113 = Cooking soups, to find url for blog data

               LINE 117 = Soup Weblink Connection Established
                          >>> Naming Convention
                              "ba": abbrv for blog article
                             
               LINE 125 = Scraping [source, article, date]
               LINE 155 = Writing into csv


    LINE 160 = Writing all rows into and closing csv file
}


----------------------------------- With love from Codexgrey;
----------------------------------- ENJOY! Mes amies.