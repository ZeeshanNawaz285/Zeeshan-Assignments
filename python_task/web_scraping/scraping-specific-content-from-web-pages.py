#this code downloads a web page's HTML content, extracts the text within all <p> tags using regular expressions, and saves these paragraphs into a text file named "scrap_file.txt". 
#This approach is commonly used for scraping specific content from web pages for further processing or analysis.


import re
import requests

web_content  = requests.get("https://propakistani.pk/2021/05/03/fbr-raises-customs-of-mg-vehicles-by-14-5-percent/").text

pattern = '<p>(.*?)</p>'

text = "\n".join(re.findall(pattern, web_content))

with open("scrap_file.txt", "w") as file:
    file.write(text)

print("Text successfully write")



'''
import requests
from bs4 import BeautifulSoup

web = requests.get("https://propakistani.pk/2021/05/03/fbr-raises-customs-of-mg-vehicles-by-14-5-percent/")

soup = BeautifulSoup(web.content, "html.parser")
line = soup.find_all("p")

   #print(l.text)
with open ("scrap_file22.txt", "w") as file :
    for l in line :
       file.write(l.text)  '''
