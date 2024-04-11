from PIL import Image

image_racket = Image.open('racket.png')
width, height = image_racket.size

left = (width / 5) * 2
top = 0
right = (width / 5) * 3
bottom = height

image_racket = image_racket.crop((left, top, right, bottom))

image_racket.save('racket.png')