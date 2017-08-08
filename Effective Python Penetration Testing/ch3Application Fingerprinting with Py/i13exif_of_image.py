import os, sys
from PIL import Image
from PIL.ExifTags import TAGS

for (i, j) in Image.open('image.jpeg')._getexif().items():
    print('%s = %s' % (TAGS.get(i), j) )