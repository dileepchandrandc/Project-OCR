import csv

def makeCSV(inpt, location):
	with open(location + "\\file_csv.csv", "w", newline='') as csv_file:
		write = csv.writer(csv_file)
		write.writerows(inpt)


if __name__ == "__main__":
	lis_data = [["1", 2, 3], [4, "ss", 6]]
	makeCSV(lis_data)

