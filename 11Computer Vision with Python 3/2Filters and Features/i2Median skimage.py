from skimage import io, data
from skimage import filters
from skimage.morphology import disk


# img = io.imread("images/image.jpg")
img = data.camera()
# print('img:', img.shape)
out = filters.median(img, disk(7))
io.imshow(out)
io.show()