import pandas as pd
from bs4 import BeautifulSoup
import requests

occ1='Medical'
occ2='Assistants'
area='Dallas'
state='TX'
page='1'
web_page="https://www.careeronestop.org/Toolkit/Training/find-local-training.aspx?keyword="+occ1+"%20"+occ2+"&persist=true&location="+area+",%20"+state+"&ajax=0&post=y&lang=en&pnfillall=y&pagesize=500&currentpage="+page
# print(web_page)
dfs=pd.read_html(web_page)
# print(len(dfs))
df=dfs[0]
name=occ1+occ2+area+state+page+'.xlsx'
df.to_excel(name)


# Make a GET request to fetch the raw HTML content, Parse the html content
# html_content = requests.get(web_page).text
# soup = BeautifulSoup(html_content, "lxml")
# print(soup.prettify()) # print the parsed data of html