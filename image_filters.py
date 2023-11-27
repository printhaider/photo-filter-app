from PIL import Image, ImageOps, ImageEnhance

def apply_black_and_white(image):
    return image.convert("L")

def apply_sepia(image, intensity=1):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    width, height = image.size
    pixels = image.load()

    for py in range(height):
        for px in range(width):
            r, g, b = image.getpixel((px, py))

            tr = int((0.393 * r + 0.769 * g + 0.189 * b) * intensity)
            tg = int((0.349 * r + 0.686 * g + 0.168 * b) * intensity)
            tb = int((0.272 * r + 0.534 * g + 0.131 * b) * intensity)

            tr = min(255, max(0, tr))
            tg = min(255, max(0, tg))
            tb = min(255, max(0, tb))

            pixels[px, py] = (tr, tg, tb)

    return image


def apply_vintage(image):
    converter = ImageEnhance.Color(image)
    image = converter.enhance(0.7)

    converter = ImageEnhance.Brightness(image)
    image = converter.enhance(1.3)

    converter = ImageEnhance.Contrast(image)
    image = converter.enhance(1.5)

    return image
