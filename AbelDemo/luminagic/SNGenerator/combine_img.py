import os
from PIL import Image

# https://gist.github.com/glombard/7cd166e311992a828675

files =  [
    'sns/M0BGDK15000101PLOWCHD52329b30.jpg', 
    'sns/M0BGDK15000301ST9VEMKZUV41ca4.jpg',
    'sns/M0BGDK15000401MGWCC5NKLPdc207.jpg',
    'sns/M0BGDK15000501YJHQGEFWQE8769d.jpg',
    'sns/M0BGDK15000701YOINHTDLKJ93641.jpg',
    'sns/M0BGDK15000801YG5EVA4ZK1b3569.jpg',
    'sns/M0BGDK15000101PLOWCHD52329b30.jpg', 
    'sns/M0BGDK15000301ST9VEMKZUV41ca4.jpg',
    'sns/M0BGDK15000401MGWCC5NKLPdc207.jpg',
    'sns/M0BGDK15000501YJHQGEFWQE8769d.jpg',
    'sns/M0BGDK15000701YOINHTDLKJ93641.jpg',
    'sns/M0BGDK15000801YG5EVA4ZK1b3569.jpg'
    ]

result = Image.new("RGB", (1200, 1600))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((400, 400), Image.ANTIALIAS)
  print('index=', index)
  x = index // 4 * 400
  y = index % 4 * 400
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save('sns/image.jpg')