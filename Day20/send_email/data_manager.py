import os
import csv
import datetime

file_name = "user_data.csv"
file_path = os.path.join(os.path.dirname(__file__), file_name)
fieldnames = ["id", "name", "email", "amount", "date", "sent"]

def create_new_data(user_name = "KienMN", user_email = "Kienmn97@gmail.com", amount = 189, date = None):
	with open(file_path, "w") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow({
			"id": 1,
			"name": user_name,
			"email": user_email,
			"amount": amount,
			"date": datetime.datetime.now()
		})

def get_length_file():
	with open(file_path, "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)
		
def append_user_data(user_name = None, user_email = None, amount = None, date = None):
	next_id = get_length_file()
	with open(file_path, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writerow({
			"id": next_id,
			"name": user_name,
			"email": user_email,
			"amount": amount,
			"date": datetime.datetime.now()
		})