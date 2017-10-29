from skimage import data, segmentation, color
from skimage.io import imread
from skimage import data
from skimage.future import graph
from matplotlib import pyplot as plt


img = data.astronaut()

img_segments = segmentation.slic(img, compactness=30, n_segments=200)
out1 = color.label2rgb(img_segments, img, kind='avg')

segment_graph = graph.rag_mean_color(img, img_segments, mode='similarity')
img_cuts = graph.cut_normalized(img_segments, segment_graph)
normalized_cut_segments = color.label2rgb(img_cuts, img, kind='avg')

fig, ax = plt.subplots(nrows=1, ncols=2, sharex=True, sharey=True, figsize=(6, 8))

ax[0].imshow(img)
ax[1].imshow(normalized_cut_segments)

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()