import numpy as np

from skimage.transform import (hough_line, probabilistic_hough_line)
from skimage.feature import canny
from skimage import io, data

from skimage import draw

#Read an image
# image =  io.imread("images/image.jpg")
image = data.camera()

#Apply your favorite edge detection algorithm. We use 'canny' for this example.
edges = canny(image, 2, 1, 25)

#Once you have the edges, run the hough transform over the image
lines = hough_line(image)
probabilistic_lines = probabilistic_hough_line(edges, threshold=10, line_length=5, line_gap=3)


def line_image(shape, lines):
    image = np.zeros(shape, dtype=bool)
    for end_points in lines:
        end_points = np.asarray(end_points)[:, ::-1]
        image[draw.line(*np.ravel(end_points))] = 1
    return image

image = line_image(image.shape, probabilistic_lines)
io.imshow(image)
io.show()