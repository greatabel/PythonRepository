from PIL import Image, ImageEnhance


img = Image.open('images/image.jpg')
rbg = img.getpixel((100,100))
print(rbg)

img.putpixel((100,100), (20,230,145))
rbg = img.getpixel((100,100))
print(rbg)
