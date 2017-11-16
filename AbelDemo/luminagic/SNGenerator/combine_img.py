import os
from PIL import Image
import glob
# https://gist.github.com/glombard/7cd166e311992a828675
import cv2

# mylist = sorted(glob.glob("sns/*.jpg"))
# print(mylist)
# sorted(mylist, key=lambda name: int(name[10:17]))
# print(mylist)
def overlay(originalImg):
  s_img = cv2.imread(originalImg)
  l_img = cv2.imread("sns/bg.jpg")
  x_offset=130
  y_offset=210
  l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
  cv2.imwrite(originalImg, l_img)

files =  [
    'sns/M0BGDK16000101HVIMGWTTZN4ca56.jpg',
    'sns/M0BGDK160002014XR620EKNSa664e.jpg',
    'sns/M0BGDK160003016TYVE4QXFKa62aa.jpg',
    'sns/M0BGDK16000401WWZPTDLF7Lec8a0.jpg',
    'sns/M0BGDK16000501G24CPGSK3W06f11.jpg',
    'sns/M0BGDK16000601Z3UNSEG8E444515.jpg',
    'sns/M0BGDK160007010EYLS1YDMI3ab87.jpg',
    'sns/M0BGDK16000801CPEJT7ANYUa92da.jpg',
    'sns/M0BGDK16000901BOJUOETFTZc42c9.jpg',
    'sns/M0BGDK16001001UHT15VED3Je4ca8.jpg',
    'sns/M0BGDK16001101J9BOG3EET42e18a.jpg',
    'sns/M0BGDK16001201KVGUE3GAQO17b1d.jpg',
    'sns/M0BGDK16001301V3P4IZE2OB2d669.jpg',
    'sns/M0BGDK160014013BIP2R1MHL5571b.jpg',
    'sns/M0BGDK16001501I1YUPHFDK487f99.jpg',
    'sns/M0BGDK16001601A1XECWOD721cec3.jpg',
    'sns/M0BGDK16001701YLRCJOWUP91db0d.jpg',
    'sns/M0BGDK160018018VFTDD3XQL3af51.jpg',
    'sns/M0BGDK16001901YLKZJN0NVV2bea3.jpg',
    'sns/M0BGDK16002001YEWBR2R8A6cff9c.jpg'
    ]

scale = 400
result = Image.new("RGB", (scale*3, scale*4))

for index, file in enumerate(files):
  print()
  overlay(file)
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((scale, scale), Image.ANTIALIAS)
  print('index=', index)
  x = index // 4 * scale
  y = index % 4 * scale
  w, h = img.size
  print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
  result.paste(img, (x, y, x + w, y + h))

result.save('sns/image.jpg')