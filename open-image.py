from PIL import Image

# There are 2 ways of creating an image

# Using context method
with Image.open("img/image.jpg") as image1:
    image1.show()

# Using the traditional open method
image2 = Image.open("img/image.jpg")
image2.show()
