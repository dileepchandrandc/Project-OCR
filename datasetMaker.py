import sys
import os
from PIL import Image, ImageEnhance

def makeDatasets(org_image_path, back_image_path, parent_dir, count):
	org_image = Image.open(org_image_path)
	back_image = Image.open(back_image_path)
	brightness = ImageEnhance.Brightness(org_image)
	brightness.enhance(2)
	org_image_size = org_image.size
	back_image_size = back_image.size
	back_image = back_image.resize(org_image_size)
	print(org_image.size, back_image.size)
	org_image_pixels = org_image.load()
	back_image_pixels = back_image.load()
	size = org_image.size
	height = size[0]
	width = size[1]
	color_val = 150
	pixel_length = 50
	for h in range(0, height):
		for w in range(0, width):
			color = org_image_pixels[h, w]
			if color[0] > color_val and color[1] > color_val and color[2] > color_val:
				status = 1
				for temp in range(1, pixel_length):
					if h + temp >= height:
						break
					color_temp = org_image_pixels[h + temp, w]
					if color_temp[0] < color_val or color_temp[1] < color_val or color_temp[2] < color_val:
						status = 0
					break
				if status == 0:
					for temp in range(1, pixel_length):
						if h - temp <= height:
							break
						color_temp = org_image_pixels[h - temp, w]
						if color_temp[0] < color_val or color_temp[1] < color_val or color_temp[2] < color_val:
							status = 0
							break
				if status == 0:
					for temp in range(1, pixel_length):
						if w + temp >= width:
							break
						color_temp = org_image_pixels[h, w + temp]
						if color_temp[0] < color_val or color_temp[1] < color_val or color_temp[2] < color_val:
							status = 0
							break
				if status == 0:
					for temp in range(1, pixel_length):
						if w - temp <= width:
							break
						color_temp = org_image_pixels[h, w - temp]
						if color_temp[0] < color_val or color_temp[1] < color_val or color_temp[2] < color_val:
							status = 0
							break
				if status == 1:
					org_image_pixels[h, w] = back_image_pixels[h, w]
	org_image.save(parent_dir + '\\output\\out' + str(count) + '.jpg')


def processArguments(argu):
	src_dir = argu
	print(src_dir)
	for i in range(len(src_dir) - 1, -1, -1):
		if src_dir[i] == '\\':
			parent_dir = src_dir[:i]
			break
	return parent_dir

def main():
	arguments = sys.argv
	src_dir = arguments[1]
	parent_dir = processArguments(src_dir)
	background_dir = os.getcwd() + '\\background'
	#print(background_dir)
	image_list = os.listdir(src_dir)
	background_list = os.listdir(background_dir)
	count = 1
	for i in range(0, len(image_list)):
		for b in range(0, len(background_list)):
			makeDatasets(src_dir + '\\' + image_list[i], background_dir + '\\' + background_list[b], parent_dir, count)
			count += 1


if __name__ == '__main__':
	main()