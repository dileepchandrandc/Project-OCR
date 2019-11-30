from PIL import Image, ImageDraw
import PIL
import run

def findLines(image_name):
	image = Image.open(image_name)
	image_size = image.size
	pixels = image.load()
	f = 1
	k = 1
	for w in range(0, image_size[0]):
		k += 1
		black_count = 0
		for h in range(0, image_size[1]):
			if pixels[w, h] != 255:
				black_count += 1
			else:
				if black_count > 10 and black_count < 30:
					image_temp = Image.open(image_name)
					image_temp = image_temp.crop((0, h - black_count, image_size[0], h))
					image_temp.save("\\test\\image_" + str(f) + ".jpg")
					run.find("\\test\\image_" + str(f) + ".jpg")
					f += 1
				black_count = 0
	print(f, k)
	return image



if __name__ == "__main__":
	image = "croped.jpg"
	image = findLines(image)
	image.save("ruled.jpg")