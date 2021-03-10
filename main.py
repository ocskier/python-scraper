# imports
import bokeh
import pandas, requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
# from bokeh.plotting import figure, output_notebook, show

try:
    url = "https://www.century21.com/real-estate/raleigh-nc-27613/LZ27613/"
    response = requests.get(url)
    html = response.text

except RequestException as e:
    print(e)

if html.strip():
    soup = BeautifulSoup(html, features="html.parser")
    prices = []
    for card in soup.find_all('div', {'class': ['infinite-item', 'property-card']}):
        if card.find('a') is not None:
            sale_price = card.find('a').contents
            for price in sale_price:
                prices.append(price.strip())
print(prices)

# output_notebook()

# p = figure(plot_width=400,plot_height=400)

# show(p)