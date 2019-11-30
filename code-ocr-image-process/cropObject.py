from PIL import Image, ImageDraw
import PIL

def cropObject(image):
	#coordinate1__start
	image_size = image.size
	pixels = image.load()
	status = 1
	for w in range(1, image_size[0]):
		if status == 0:
			break
		list_value_width = image_size[0] - 1
		for h in range(1, image_size[1]):
			if pixels[w, h] == 255:
				continue
			else:
				list_value_width = w
				status = 0
				break
	coordinate1 = (w, h)
	#coordinate1__end
	#coordinate2__start
	status = 1
	for h in range(1, image_size[1]):
		if status == 0:
			break
		list_value_height = image_size[1] - 1
		for w in range(1, image_size[0]):
			if pixels[w, h] == 255:
				continue
			else:
				list_value_height = h
				status = 0
				break

	coordinate2 = (w, h)
	#coordinate2__end
	#coordinate3__start
	status = 1
	for w in range(image_size[0] - 1, 0, -1):
		if status == 0:
			break
		list_value_width = image_size[0] - 1
		for h in range(1, image_size[1]):
			if pixels[w, h] == 255:
				continue
			else:
				list_value_width = w
				status = 0
				break
	coordinate3 = (w, h)
	#coordinate3__end
	#coordinate4__start
	status = 1
	for h in range(image_size[1] - 1, 0, -1):
		if status == 0:
			break
		list_value_height = 1
		for w in range(1, image_size[0]):
			if pixels[w, h] == 255:
				continue
			else:
				list_value_height = h
				status = 0
				break
	coordinate4 = (w, h)
	#coordinate4__end
	draw = ImageDraw.Draw(image)
	point1 = (coordinate1[0], coordinate2[1])
	point2 = (coordinate3[0], coordinate4[1])
	point3 = (point1[0], point2[1])
	point4 = (point2[0], point1[1])
	draw.line((point1[0], point1[1], point3[0], point3[1]), fill = 150, width = 1)
	draw.line((point3[0], point3[1], point2[0], point2[1]), fill = 150, width = 1)
	draw.line((point2[0], point2[1], point4[0], point4[1]), fill = 150, width = 1)
	draw.line((point4[0], point4[1], point1[0], point1[1]), fill = 150, width = 1)
	image.save("bounded.jpg")
	image = image.crop((point1[0], point1[1], point2[0], point2[1]))
	image.save("croped_l1.jpg")
	image_size = image.size
	image = image.crop((int(image_size[0] * 0.10), int(image_size[0] * 0.35), image_size[0] - int(image_size[0] * 0.10), image_size[1] - int(image_size[1] * 0.15)))
	image_size = image.size
	scale = 0.4
	image.save("croped_l2.jpg")
	image = image.resize((int(image_size[0] * scale), int(image_size[1] * scale)))
	return image



if __name__ == "__main__":
	image = Image.open("preprocessed.jpg")
	image = cropObject(image)
	image.save("croped.jpg")