# imports
import bokeh
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
# from bokeh.plotting import figure, output_notebook, show

try:
    url = "https://www.century21.com/real-estate/raleigh-nc-27613/LZ27613/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, features="html.parser")
    for card in soup.find_all('div', 'infinite-item', 'property-card'):
        print(card.prettify())

except RequestException as e:
    print(e)

# output_notebook()

# p = figure(plot_width=400,plot_height=400)

# show(p)