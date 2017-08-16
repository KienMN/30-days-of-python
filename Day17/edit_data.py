import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

filepath = "user_data.csv"

def get_length(filepath = None):
	with open(filepath, "r") as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
	return len(reader_list)

print(get_length(filepath = filepath))

# with open("user_data.csv", "w+") as csvfile:
# 	fieldnames = ["id", "name", "email", "amount", "sent", "date"]
# 	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
# 	writer.writeheader()
	# writer.writerow({"id": 1, "name": "KienMn", "email": "kienmn@gmail.com", "amount": 189})

def append_data(filepath = None, name = None, email = None, amount = None):
	fieldnames = ["id", "name", "email", "amount", "sent", "date"]
	next_id = get_length(filepath)
	with open (filepath, "a") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email,
			"amount": amount,
			"date": datetime.datetime.now()
		})

# append_data(filepath = filepath, name = "KienMN", email = "kienmn97@gmail.com", amount = 189)

def find_user(filepath = None, id = None, email = None):
	with open(filepath, "r") as csvfile:
		reader = csv.DictReader(csvfile)
		unknown_id = None
		unknown_email = None
		for row in reader:
			if id is not None:
				if int(row.get("id")) == id:
					return row
				else:
					unknown_id = id
			if email is not None:
				if row.get("email") == email:
					return row
				else:
					unknown_email = email
		if unknown_id is not None:
			return "User with the id {user_id} not found".format(user_id = unknown_id)
		if unknown_email is not None:
			return "User with the email {user_email} not found".format(user_email = unknown_email)
	return None

# print(find_user(filepath=filepath, email = "kienmn97@gmail.com"))

# work fine for python 2, except python 3
def edit_data(filepath = filepath, edit_id = None, email = None, amount = None, sent = None):
	temp_file = NamedTemporaryFile(delete = False)
	print(temp_file.name)
	with open(filepath, "rb") as csvfile, temp_file:
		fieldnames = ["id", "name", "email", "amount", "sent", "date"]
		reader = csv.DictReader(csvfile)
		writer = csv.DictWriter(temp_file, fieldnames = fieldnames)
		writer.writeheader()
		
		for row in reader:
			print(row)
			if edit_id is not None:
				if int(row["id"]) == int(edit_id):
					row["amount"] = amount
					row["sent"] = sent
			elif email is not None:
				if str(row["email"]) == str(email):
					row["amount"] = amount
					row["sent"] = sent
			writer.writerow(row)
		shutil.move(temp_file.name, filepath)
		return True
	return False

		
edit_data(edit_id = 1, amount = 200)




