import sys
from PIL import Image

images = map(Image.open, [
    'sns/M0BGDK15000101PLOWCHD52329b30.jpg', 
    'sns/M0BGDK15000101RNZSCLEOKU824ef.jpg', 
    'sns/M0BGDK15000301ST9VEMKZUV41ca4.jpg',
    'sns/M0BGDK15000401MGWCC5NKLPdc207.jpg'])
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test.jpg')