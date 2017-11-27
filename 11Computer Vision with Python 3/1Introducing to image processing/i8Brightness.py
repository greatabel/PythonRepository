from PIL import Image, ImageEnhance


img = Image.open('images/image.jpg')
enhancer = ImageEnhance.Brightness(img)
enhancer.enhance(2).show()