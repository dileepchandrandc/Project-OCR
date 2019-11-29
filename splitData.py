import random
import csv
from PIL import Image
import os
import sys

def splitFileName(path):
	fname = ""
	for i in range(len(path) - 1, -1, -1):
		if path[i] == "\\":
			break
		fname = path[i] + fname
	return fname

def splitData(location_images, csv_file_location, input_file_name):
	#location_images = "C:\\Users\\user\\Desktop\\Project-Dataset\\Images\\normal\\"
	#csv_file_location = "C:\\Users\\user\\Desktop\\Project-Dataset\\Images\\"
	#input_file_name = "file_csv.csv"
	location_images += "\\"
	rows = []
	csv_file = open(csv_file_location + "\\" +input_file_name, "r")
	csv_ptr = csv.DictReader(csv_file)
	for row in csv_ptr:
		rows.append(row)
	random.shuffle(rows)
	index = int(len(rows) * 0.80)
	train = rows[0:index]
	test = rows[index :]
	##make traning set
	fields_csv = [["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"]]
	status = False
	if os.path.exists(csv_file_location + "\\train.csv"):
		train_csv_file = open(csv_file_location + "\\train.csv", "r", newline = "")
		train_csv_ptr = csv.DictReader(train_csv_file)
		rows_train = []
		for row_train in train_csv_ptr:
			rows_train.append([row_train["filename"], row_train["width"], row_train["height"], row_train["class"], row_train["xmin"], row_train["ymin"], row_train["xmax"], row_train["ymax"]])
			status = True
	train_csv_file = open(csv_file_location + "\\train.csv", "w", newline = "")
	train_csv_writer = csv.writer(train_csv_file)
	train_csv_writer.writerows(fields_csv)
	train_rows = []
	for row in train:
		image_file_name = splitFileName(row["filename"])
		image_readed = Image.open(location_images +image_file_name)
		try:
			os.mkdir(location_images + "train")
		except:
			pass
		image_file_location = location_images + "train\\" +image_file_name
		image_readed.save(image_file_location)
		row_value = [image_file_name, row["width"], row["height"], row["class"], row["xmin"], row["ymin"], row["xmax"], row["ymax"]]
		train_rows.append(row_value)
	if status:
		train_csv_writer.writerows(rows_train)
	train_csv_writer.writerows(train_rows)
	###test set
	##make traning set
	status = False
	if os.path.exists(csv_file_location + "\\test.csv"):
		test_csv_file = open(csv_file_location + "\\test.csv", "r", newline = "")
		test_csv_ptr = csv.DictReader(test_csv_file)
		rows_test = []
		for row_test in test_csv_ptr:
			rows_test.append([row_test["filename"], row_test["width"], row_test["height"], row_test["class"], row_test["xmin"], row_test["ymin"], row_test["xmax"], row_test["ymax"]])
			status = True
	test_csv_file = open(csv_file_location + "\\test.csv", "w", newline = "")
	test_csv_writer = csv.writer(test_csv_file)
	fields_csv = [["filename", "width", "height", "class", "xmin", "ymin", "xmax", "ymax"]]
	test_csv_writer.writerows(fields_csv)
	test_rows = []
	for row in test:
		image_file_name = splitFileName(row["filename"])
		image_readed = Image.open(location_images + image_file_name)
		try:
			os.mkdir(location_images + "test")
		except:
			pass
		image_file_location = location_images + "test\\" +image_file_name
		image_readed.save(image_file_location)
		row_value = [image_file_name, row["width"], row["height"], row["class"], row["xmin"], row["ymin"], row["xmax"], row["ymax"]]
		test_rows.append(row_value)
	if status:
		print(rows_test)
		test_csv_writer.writerows(rows_test)
	test_csv_writer.writerows(test_rows)



