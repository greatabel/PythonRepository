# Importing required modules
import requests  
from bs4 import BeautifulSoup  
import urllib.parse


response = requests.get('http://www.freeimages.co.uk/galleries/food/breakfast/index.htm')  
parse = BeautifulSoup(response.text)

# Get all image tags
image_tags = parse.find_all('img')

# Get urls to the images
images = [ url.get('src') for url in image_tags]

# If no images found in the page
if not images:  
    sys.exit("Found No Images")

# Convert relative urls to absolute urls if any
images = [urllib.parse.urljoin(response.url, url) for url in images]  
print( 'Found %s images' % len(images) )


# Download images to downloaded folder
for url in images:  
    r = requests.get(url)
    f = open('downloaded/%s' % url.split('/')[-1], 'wb')
    f.write(r.content)
    f.close()
    print( 'Downloaded %s' % url )

