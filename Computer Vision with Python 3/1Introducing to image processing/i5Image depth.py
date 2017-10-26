from PIL import Image


img = Image.open('images/image.jpg')
grayscale = img.convert("L")
grayscale.show()