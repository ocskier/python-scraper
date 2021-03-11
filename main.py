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
    beds = []
    baths = []
    address = []
    links = []
    for card in soup.find_all('div', {'class': ['infinite-item', 'property-card']}):
        if card.find('div',{'class':'property-address'}) is not None:
            # add price
            sale_price = card.find('a').contents[0]
            prices.append(int(
                sale_price.replace(',','').replace("'", '').replace('$', '').strip())
            )
            # add if avail
            if card.find('div', {'class':'sale-pending'}) is not None:
                sale_pending = card.find('div', {'class':'sale-pending'}).contents[0]
                pending.append(True)
            else:
                pending.append(False)
            # of beds
            num_beds = card.find('div', {'class':'property-beds'}).contents[1].contents[0]
            beds.append(int(num_beds))
            # of baths
            num_baths = card.find('div', {'class':'property-baths'}).contents[1].contents[0]
            baths.append(int(num_baths))
            # add address
            where = card.find('div',{'class':'property-address'}).contents[0].strip()
            where += ', ' + card.find('div',{'class':'property-city'}).contents[0].strip()
            address.append(where)
            # add website link
            link = 'https://www.century21.com' + card.find('a')['href']
            links.append(link.replace("'", ''))

xl_links = []
for each in links:
    xl_links.append('=hyperlink("{url}","Go")'.format(url=each))

# output to csv and excel
df = pandas.DataFrame(data={
    "Sale Price": prices,
    "Sale Pending":pending,
    "Beds": beds,
    "Baths": baths,
    "Address":address,
    "Url": links})
df.to_csv("./file.csv", sep=',',index=False)
df["Url"] = xl_links
df.to_excel("./sheet.xlsx",index=False)

# output_notebook()

# p = figure(plot_width=400,plot_height=400)

# show(p)
