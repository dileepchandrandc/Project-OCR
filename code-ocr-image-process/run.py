from PIL import Image
from tesseract import image_to_string


def find(image_path):
	print(image_to_string(Image.open(image_path)))
	print(image_to_string(Image.open(image_path), lang='eng'))

