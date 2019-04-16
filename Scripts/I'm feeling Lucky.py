#! python 3

import sys, webbrowser, requests, bs4

print('Googling...') # display text while downloading the Google page
wyszukiwanie = str(input("What are You looking for? "))
"""
if len(sys.argv) > 0:
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()
else:
    res = requests.get('https://www.google.com/search?q=%20dupa')
    res.raise_for_status()
"""
# Retrieve top search result links.
res = requests.get('http://google.com/search?q=' + wyszukiwanie)
soup = bs4.BeautifulSoup(res.text, features='html.parser')
# Open a browser tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))