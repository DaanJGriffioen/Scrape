from os import write
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
from bokeh.io import output_file
from bokeh.plotting import figure, show



url = ["https://www.refurbed.nl/p/iphone-12/", "https://www.refurbed.nl/p/iphone-12-pro/", "https://www.refurbed.nl/p/iphone-13/", "https://www.refurbed.nl/p/iphone-13-pro/", "https://www.refurbed.nl/p/iphone-14/", "https://www.refurbed.nl/p/iphone-14-pro/"]
name = ["iphone-12", "iphone-12-pro", "iphone-13", "iphone-13-pro", "iphone-14", "iphone-14-pro"]

tw = []
twp = []
th = []
thp = []
fo = []
fop = []

today = datetime.today().strftime('%Y-%m-%d')
output_file("IphonePrices.txt")

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
    
    #Get the 6 lowest values of the phone 
    for j in range(6):
      if text < minval[j]:
        minval[j] = text
        break
  
  # Output lowest prices to appropriate arrays
    if i == 0:
      tw = minval
    elif i == 1:
      twp = minval
    elif i == 2:
      th = minval
    elif i == 3:
      thp = minval
    elif i == 4:
      fo = minval
    elif i == 5:
      fop = minval
  
x = [1,2,3,4,5,6]
print("Iphone-12: ", tw)
print("Iphone-12-pro: ", twp)
print("Iphone-13: ", th)
print("Iphone-13-pro: ", thp)
print("Iphone-14: ", fo)
print("Iphone-14-pro: ", fop)

p = figure(title="Iphone Prices " + today, x_axis_label='x', y_axis_label='y',y_range=(0, 1000))
p.line(x, tw, legend_label="Iphone-12", line_color="red" , line_width=2)
print("Iphone-12: ", tw)
p.line(x, twp, legend_label="Iphone-12-pro", line_color="green", line_width=2)
print("Iphone-12-pro: ", twp)
p.line(x, th, legend_label="Iphone-13", line_color="blue", line_width=2)
print("Iphone-13: ", th)
p.line(x, thp, legend_label="Iphone-13-pro", line_color="orange", line_width=2)
print("Iphone-13-pro: ", thp)
p.line(x, fo, legend_label="Iphone-14", line_color="purple", line_width=2)
print("Iphone-14: ", fo)
p.line(x, fop, legend_label="Iphone-14-pro", line_color="grey", line_width=2)
print("Iphone-14-pro: ", fop)

#Append the graph to the html file
p.legend.background_fill_alpha = 0.3
show(p)

#Append the prices to a text file for archiving
OutputFile = open("file.txt", "a")
OutputFile.write(today + '\n')
OutputFile.writelines('\n' + "Iphone-12: " + str(tw) + '\n')
OutputFile.writelines("Iphone-12-pro: " + str(twp) + '\n')
OutputFile.writelines("Iphone-13: " + str(th) + '\n')
OutputFile.writelines("Iphone-13-pro: " + str(thp) + '\n')
OutputFile.writelines("Iphone-14: " + str(fo) + '\n')
OutputFile.writelines("Iphone-14-pro: " + str(fop) + '\n')
OutputFile.write('\n' + "==============" + '\n')
OutputFile.close()

#append the bokeh output to the html file
with open('IphonePrices.txt','r') as firstfile, open('file.html','a') as secondfile: 
    # read content from first file 
    for line in firstfile: 
             # append content to second file 
             secondfile.write(line)