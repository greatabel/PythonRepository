from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
# img = Image.open("sns_test/M0BGDD05000601647BAMGXUQeed76.jpg")
# draw = ImageDraw.Draw(img)
# # font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("/System/Library/Fonts/Helvetica.dfont", 15)
# # draw.text((x, y),"Sample Text",(r,g,b))
# draw.text((0, 0),"M0BGDD05000601647BAMGXUQeed76",(255,255,255),font=font)
# img.save('sample-out.jpg')


import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
font = ImageFont.truetype("/System/Library/Fonts/Helvetica.dfont", 20)
img = Image.open("sns_test/M0BGDD05000601647BAMGXUQeed76.jpg")
draw = ImageDraw.Draw(img)
draw.text((45,5), "S/N:M0BGDD05000601647BAMGXUQeed76", (10), font=font)
draw = ImageDraw.Draw(img)
img.save("a_test.png")

for i in range(10):
    print(i)