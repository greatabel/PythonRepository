from PIL import Image


img = Image.open('images/image.jpg')
rbg = img.getpixel((100,100))
print('rbg=>', rbg)
grayscale = img.convert("L").getpixel((100,100))
print('grayscale=>', grayscale)