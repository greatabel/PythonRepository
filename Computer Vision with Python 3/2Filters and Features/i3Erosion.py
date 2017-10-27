from skimage import morphology
from skimage import io

img = io.imread('images/image.jpg')
eroded_img = morphology.binary_erosion(img)

io.imshow(eroded_img)
io.show()