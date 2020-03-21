try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def getCaptcha():
    captcha=pytesseract.image_to_string(Image.open('image.jpg'))
    #print(captcha)
    return captcha

#getCaptcha()