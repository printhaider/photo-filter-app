from PIL import Image, ImageEnhance

def apply_sepia(image):
    """
    Apply a sepia filter to the given image.
    """
    width, height = image.size
    pixels = image.load()  # create the pixel map

    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px, py))

            # Calculate new values
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            # Reassign new values keeping in mind the maximum value
            pixels[px, py] = (min(tr, 255), min(tg, 255), min(tb, 255))

    return image

def apply_vintage(image):
    """
    Apply a vintage filter to the given image.
    """
    # You can adjust these values for different effects
    converter = ImageEnhance.Color(image)
    image = converter.enhance(0.7)  # Adjust color balance

    converter = ImageEnhance.Brightness(image)
    image = converter.enhance(1.3)  # Adjust brightness

    converter = ImageEnhance.Contrast(image)
    image = converter.enhance(1.5)  # Adjust contrast

    return image
