import csv

with open ("data.csv", "w+") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["Col 1", "Col 2", "Col 3"])
	writer.writerow(["Value", "Value", "Value"])
	writer.writerow(["Value", "Value", "Value"])

with open ("data.csv", "r") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)

with open ("data.csv", "r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)


with open ("dictionary.csv", "w+") as csvfile:
	fieldnames = ["id", "title"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()										# write header for csv file
	writer.writerow({"id": 123, "title": "value"})

with open ("dictionary.csv", "r") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)
