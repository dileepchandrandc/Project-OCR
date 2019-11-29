from PIL import Image, ImageDraw, ImageEnhance
import PIL
import os
import toCSV
import sys
import splitData

def start(image_name, label_name, src_path, dest_path):
	path_src = src_path + "\\"
	out_path = src_path + "\\edited\\"
	path = dest_path
	#path_src = "C:\\Users\\user\\Desktop\\Project-Dataset\\Images\\normal\\" + label_name + "\\"
	#path = "C:\\Users\\user\\Desktop\\Project-Dataset\\Images\\normal\\"
	#out_path = "C:\\Users\\user\\Desktop\\Project-Dataset\\Images\\edited\\"
	#scale = 0.2
	image = Image.open(path_src + image_name)
	image = image.rotate(-90, PIL.Image.NEAREST, expand = 1)
	image.save(path + "\\" + image_name)
	image_en = ImageEnhance.Brightness(image)
	image = image_en.enhance(1.5)
	#image = image.resize( [int(scale * s) for s in image.size] )
	out_image_path = out_path + image_name
	if not(os.path.exists(out_path)):
		os.mkdir(out_path)
	image.save(out_image_path)
	image_test = Image.open(out_image_path)
	image_test_width = image_test.size[0]
	image_test_height = image_test.size[1]
	#coordinate1__start
	status = 1
	for w in range(1, image_test_width):
		if status == 0:
			break
		list_value_width = image_test_width - 1
		for h in range(1, image_test_height):
			pixel_values = image_test.getpixel((w, h))
			pixel_red = pixel_values[0]
			pixel_green = pixel_values[1]
			pixel_blue = pixel_values[2]
			if pixel_red > 150 and pixel_green > 150 and pixel_blue > 150:
				continue
			else:
				if pixel_red < 130 or pixel_green < 130 or pixel_blue < 130:
					list_value_width = w
					status = 0
					break
	coordinate1 = (w, h)
	#coordinate1__end
	#coordinate2__start
	status = 1
	for h in range(1, image_test_height):
		if status == 0:
			break
		list_value_height = image_test_height - 1
		for w in range(1, image_test_width):
			pixel_values = image_test.getpixel((w, h))
			pixel_red = pixel_values[0]
			pixel_green = pixel_values[1]
			pixel_blue = pixel_values[2]
			if pixel_red > 150 and pixel_green > 150 and pixel_blue > 150:
				continue
			else:
				if pixel_red < 120 or pixel_green < 120 or pixel_blue < 120:
					list_value_height = h
					status = 0
					break

	coordinate2 = (w, h)
	#coordinate2__end
	#coordinate3__start
	status = 1
	for w in range(image_test_width - 1, 0, -1):
		if status == 0:
			break
		list_value_width = image_test_width - 1
		for h in range(1, image_test_height):
			pixel_values = image_test.getpixel((w, h))
			pixel_red = pixel_values[0]
			pixel_green = pixel_values[1]
			pixel_blue = pixel_values[2]
			if pixel_red > 150 and pixel_green > 150 and pixel_blue > 150:
				continue
			else:
				if pixel_red < 120 or pixel_green < 120 or pixel_blue < 120:
					list_value_width = w
					status = 0
					break
	coordinate3 = (w, h)
	#coordinate3__end
	#coordinate4__start
	status = 1
	for h in range(image_test_height - 1, 0, -1):
		if status == 0:
			break
		list_value_height = 1
		for w in range(1, image_test_width):
			pixel_values = image_test.getpixel((w, h))
			pixel_red = pixel_values[0]
			pixel_green = pixel_values[1]
			pixel_blue = pixel_values[2]
			if pixel_red > 150 and pixel_green > 150 and pixel_blue > 150:
				continue
			else:
				if pixel_red < 100 or pixel_green < 100 or pixel_blue < 100:
					list_value_height = h
					status = 0
					break
	coordinate4 = (w, h)
	#coordinate4__end
	draw = ImageDraw.Draw(image_test)
	point1 = (coordinate1[0], coordinate2[1])
	point2 = (coordinate3[0], coordinate4[1])
	point3 = (point1[0], point2[1])
	point4 = (point2[0], point1[1])
	draw.line((point1[0], point1[1], point3[0], point3[1]), fill = (255, 0, 0), width = 1)
	draw.line((point3[0], point3[1], point2[0], point2[1]), fill = (255, 0, 0), width = 1)
	draw.line((point2[0], point2[1], point4[0], point4[1]), fill = (255, 0, 0), width = 1)
	draw.line((point4[0], point4[1], point1[0], point1[1]), fill = (255, 0, 0), width = 1)
	image_test.save(out_image_path)
	return [image_test_width, image_test_height, str(point1[0]), str(point1[1]), str(point2[0]), str(point2[1])]


def processArguments(list_args):
	dict_args = {}
	for item in list_args:
		key = ""
		str_ = ""
		for ch in item:
			if ch == "=":
				key = str_
				str_ = ""
				continue
			str_ += ch
		dict_args[key] = str_
	return dict_args


if __name__ == "__main__":
	print(sys.argv)
	args = processArguments(sys.argv[1:])
	print(args)
	#sys.exit(0)
	csv_data = [["filename", "width", "height", "class", "xmin",	"ymin",	"xmax", "ymax"]]
	#label_names = ["W21126", "WL7302"]
	#path = "C:\\Users\\user\\Desktop\\Project-Dataset\\Images\\normal\\" + label_name
	dest = args['dest']
	path = args['src']
	label_name = args["class"]
	print("Reading files for class %s"%(label_name))
	images = os.listdir(path)
	total = len(images)
	c = 1
	for i in images:
		if not (i.endswith(".jpg")):
			continue
		print("Image :%d of %d" % (c, total))
		res = start(i, label_name, path, dest)
		res = [dest + "\\" + i] + res
		res.insert(3, label_name)
		csv_data.append(res)
		c += 1
	print("Creating CSV file")
	toCSV.makeCSV(csv_data, dest)
	print("Completed!!")
	print("Splitting dataset")
	splitData.splitData(dest, dest, "file_csv.csv")
	print("Datasets created")
	dest_images = os.listdir(dest)
	for im in dest_images:
		if not(im.endswith('.jpg')):
			continue
		os.remove(dest + "\\" + im)
