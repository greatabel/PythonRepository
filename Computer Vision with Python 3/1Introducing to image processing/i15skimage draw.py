import numpy as np
from skimage import io, draw

img = np.zeros((200, 200), dtype=np.uint8)
x, y = draw.circle(100, 100, 50)
# print(x, y)
img[x, y] = 1
io.imshow(img)
io.show()