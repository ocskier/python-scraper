""" This is the main module for scraping real estate local data"""

# imports
# import bokeh
import pandas
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
# from bokeh.plotting import figure, output_notebook, show

try:
    URL = "https://www.century21.com/real-estate/raleigh-nc-27613/LZ27613/"
    URL += "?sn=5&sk=Y&pt=1%2C4%2C5&sf=3000&o=price-asc"
    response = requests.get(URL)
    html = response.text

except RequestException as _e:
    print(_e)

if html.strip():
    soup = BeautifulSoup(html, features="html.parser")
    prices = []
    pending = []
    for card in soup.find_all('div', {'class': ['infinite-item', 'property-card']}):
        if card.find('a') is not None:
            sale_price = card.find('a').contents
            prices.append(int(
                sale_price[0].replace(',','').replace("'", '').replace('$', '').strip())
            )
            if card.find('div', {'class':'sale-pending'}) is not None:
                sale_pending = card.find('div', {'class':'sale-pending'}).contents
                print(sale_pending[0])
                pending.append(True)
            else:
                pending.append(False)

print(prices,pending)
df = pandas.DataFrame(data={"Sale Price": prices,"Sale Pending":pending})
df.to_csv("./file.csv", sep=',',index=False)
df.to_excel("./sheet.xlsx",index=False)

# output_notebook()

# p = figure(plot_width=400,plot_height=400)

# show(p)
