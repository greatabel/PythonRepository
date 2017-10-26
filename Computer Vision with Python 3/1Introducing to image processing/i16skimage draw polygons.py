import numpy as np
from skimage import io, draw

img = np.zeros((200, 200), dtype=np.uint8)

# x, y = draw.circle(100, 100, 50)

# x, y = draw.ellipse(100, 100, 20, 40)
r = np.array([10, 25, 80, 50])
c = np.array([10, 60, 40, 10])
x, y = draw.polygon(r, c)

# img[x, y] = 1
# io.imshow(img)
# io.show()

img[x, y] = 1
io.imshow(img)
io.show()