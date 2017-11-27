# 图片对比度
# https://baike.baidu.com/item/%E5%9B%BE%E5%83%8F%E5%AF%B9%E6%AF%94%E5%BA%A6
# 
from PIL import Image, ImageEnhance


img = Image.open('images/image.jpg')
enhancer = ImageEnhance.Contrast(img)
enhancer.enhance(2).show()
enhancer.enhance(0.9).show()