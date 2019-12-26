#! python3
# xkcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4


url = 'http://xkcd.com'                 # starting url
os.makedirs('xkcd', exist_ok=True)      # store comics in ./xkcd
iteration = 0
number = 'test'
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    if iteration > 0:
        number = url.split('/')[3:4]
        number = number[0] + '_'

    soup = bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exception.MissingSchema:
            # skip this comic
            # prevLink = soup.select('a[rel^="prev"]')[0]
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            iteration += 1
            continue
        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', number + os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    iteration += 1
print('Done.')