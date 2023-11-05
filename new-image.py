from PIL import Image

# Create a red 250 by 250 pixels image
img = Image.new("RGBA", (250, 250), (250, 0, 0))
img.show()

# Save the image in img folder
img.save("img/red-250.png")
