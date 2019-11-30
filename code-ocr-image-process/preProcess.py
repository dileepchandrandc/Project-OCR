from PIL import Image, ImageEnhance
import PIL

def preProcess(image):
	image = image.rotate(-90, PIL.Image.NEAREST, expand = 1)
	image = image.convert("L")
	enhancer = ImageEnhance.Brightness(image)
	enhancer.enhance(4)
	pixels = image.load()
	image_size = image.size
	for w in range(0, image_size[0]):
		for h in range(0, image_size[1]):
			if pixels[w, h] < 75:
				pixels[w, h] = 0
			else:
				pixels[w, h] = 255
	return image


if __name__ == "__main__":
	image = Image.open("image.jpg")
	image = preProcess(image)
	image.save("preprocessed.jpg")