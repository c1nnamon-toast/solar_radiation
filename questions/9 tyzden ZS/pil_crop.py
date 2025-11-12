from PIL import Image

if __name__ == "__main__":
    image = Image.open("Sajin_sad.png")

    Sajin =         image.crop((0, 0, 640, 360))
    Sajin_smaller = image.crop((0, 0, 639, 359))

    Sajin.save("Sajin.png")
    Sajin_smaller.save("Sajin_smaller.png")

# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.crop
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#coordinate-system
