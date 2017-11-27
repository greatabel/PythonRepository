from PIL import Image

# https://stackoverflow.com/questions/27445694/
# creating-image-through-input-pixel-values-with-the-python-imaging-library-pil



im = Image.new("RGB", (128, 128))
pix = im.load()
for x in range(128):
    for y in range(128):
        pix[x,y] = (255,0,0)

im.save("images/2test.png", "PNG")
