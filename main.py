# imports
import bokeh
import requests
from requests.exceptions import RequestException
# from bokeh.plotting import figure, output_notebook, show

try:
    url = "https://www.npr.org/sections/music-news/"
    response = requests.get(url)
    html = response.text
    print(html)
except RequestException as e:
    print(e)

# output_notebook()

# p = figure(plot_width=400,plot_height=400)

# show(p)