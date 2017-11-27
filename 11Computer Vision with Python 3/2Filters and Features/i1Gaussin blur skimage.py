from skimage import io
from skimage import filters


img = io.imread("images/image.jpg")
out = filters.gaussian(img, sigma=5)
io.imshow(out)
io.show()