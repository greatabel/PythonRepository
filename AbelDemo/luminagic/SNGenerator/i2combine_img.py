import os
from PIL import Image
import glob
# https://gist.github.com/glombard/7cd166e311992a828675
import cv2



def overlay(originalImg):
  s_img = cv2.imread(originalImg)
  l_img = cv2.imread("Resources/bg.jpg")
  x_offset=130
  y_offset=210
  l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
  cv2.imwrite(originalImg, l_img)

files = sorted(glob.glob("sns/*.jpg"))
# files.remove("sns/bg.jpg")

# sorted(mylist, key=lambda name: int(name[10:17]) if  name else -1 )
# print(mylist)
chunks = [files[x:x+12] for x in range(0, len(files), 12)]


for pageindex, files in enumerate(chunks):
  print(pageindex, files)
  scale = 400
  result = Image.new("RGB", (scale*3, scale*4))

  for index, file in enumerate(files):
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

  result.save('sns/'+str(pageindex) +'page.jpg')