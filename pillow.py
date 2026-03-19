from PIL import Image

img = Image.open('inputs/input.png')
img.save('outputs/pillow_output.png', optimize=True, quality=9)