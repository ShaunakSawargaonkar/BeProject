from PIL import Image  # Import Image class from library.

image = Image.open("example.jpg")  # Load image.
cropped_image = image.crop((100, 100, 250, 250))  # Crop the image.
cropped_image.save("example_cropped.jpg")  