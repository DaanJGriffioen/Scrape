from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re

OutputFile = open("iPrice.txt", "w")
OutputFile.writelines('\n'+ datetime.today().strftime('%Y-%m-%d') + '\n')
url = ["https://www.refurbed.nl/p/iphone-12/", "https://www.refurbed.nl/p/iphone-12-pro/", "https://www.refurbed.nl/p/iphone-13/", "https://www.refurbed.nl/p/iphone-13-pro/"]
name = ["iphone-12", "iphone-12-pro", "iphone-13", "iphone-13-pro"]

for i in range(len(url)):
  # Initialize minimal value array
  minval = [999, 999, 999, 999, 999, 999]
  # Print name of iphone
  OutputFile.writelines("===" + name[i] + "===" + '\n')
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
  
  # Output lowest prices to text file
  for j in range(6):
    text = minval[j]
    OutputFile.writelines(str(text))
    OutputFile.writelines(" ")
    print(str(text))
  OutputFile.writelines('\n')

OutputFile.close()