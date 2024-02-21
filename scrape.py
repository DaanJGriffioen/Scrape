from os import write
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
from bokeh.io import output_file
from bokeh.plotting import figure, show

tw = []
twp = []
th = []
thp = []
fo = []
fop = []


#Query refurbed website and extract cheapest prices from it
def getData():
  cheapest = []
  url = ["https://www.refurbed.nl/p/iphone-12/", "https://www.refurbed.nl/p/iphone-12-pro/", "https://www.refurbed.nl/p/iphone-13/", "https://www.refurbed.nl/p/iphone-13-pro/", "https://www.refurbed.nl/p/iphone-14/", "https://www.refurbed.nl/p/iphone-14-pro/"]
  name = ["iphone-12", "iphone-12-pro", "iphone-13", "iphone-13-pro", "iphone-14", "iphone-14-pro"]

  output_file("file.html")

  for i in range(len(url)):
    # Initialize minimal value array
    minval = [999, 999, 999, 999, 999, 999]
    # Print name of iphone
    #  Request url and find price information
    data = requests.get(url[i])
    soup = BeautifulSoup(data.text, 'html.parser')
    price = soup.find_all('div', class_='mt-1.5 mr-2 text-sm text-right text-emphasize-03', string=True)
    
    # Format text
    for p in range(len(price)):
      text = price[p].get_text().strip("€ \n").replace(",",".")
      text = int(float(text))
      
      # Get the 6 lowest values of the phone
      # (Not all 6 values are used right now, maybe later)
      for j in range(6):
        if text < minval[j]:
          minval[j] = text
          break
    
    #Give the values of the cheapest to a list
    cheapest.append(minval[0])
  
  #Write cheapest prices to a csv
  OutputFile = open("prices.csv", "a")
  for i in range(6):
    OutputFile.writelines(str(cheapest[i]) + ",")
  OutputFile.writelines("\n")
  OutputFile.close()

def makeGraph():
  today = datetime.today().strftime('%Y-%m-%d')
  data = pd.read_csv("prices.csv", encoding='utf8')

  x = list(range(len(data.Iphone12)))
  p = figure(title="Iphone Prices 21-2-2024 to " + today, x_axis_label='x', y_axis_label='y',y_range=(0, 1000))
  p.line(x, data.Iphone12, legend_label="Iphone-12", line_color="red" , line_width=2)
  p.line(x, data.Iphone12Pro, legend_label="Iphone-12-pro", line_color="green", line_width=2)
  p.line(x, data.Iphone13, legend_label="Iphone-13", line_color="blue", line_width=2)
  p.line(x, data.Iphone13Pro, legend_label="Iphone-13-pro", line_color="orange", line_width=2)
  p.line(x, data.Iphone14, legend_label="Iphone-14", line_color="purple", line_width=2)
  p.line(x, data.Iphone14Pro, legend_label="Iphone-14-pro", line_color="grey", line_width=2)

  #Append the graph to the html file
  p.legend.background_fill_alpha = 0.3
  show(p)

#Main function because convention and neat
if __name__ == '__main__':
  getData()
  makeGraph()