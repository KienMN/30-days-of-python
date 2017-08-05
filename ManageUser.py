import datetime
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "example@gmail.com"
password = "password"
from_email = username
to_list = ["another@gmail.com"]

class ManageUser():
	user_details = []
	messages = []
	email_messages = []
	base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team KMN
"""
	def add_user(self, name = None, amount = None, email = None):
		if name != None and amount != None:
			name = name[0].upper() + name[1:].lower()
			amount = "%.2f" %(amount)
			details = {
				"name": name,
				"amount": amount
			}
			today = datetime.date.today()
			date_txt = '{today.day}/{today.month}/{today.year}'.format(today = today)
			details["date"] = date_txt
			if email is not None:
				details["email"] = email
			self.user_details.append(details)
	def get_user_details(self):
		return self.user_details
	def make_messages(self):
		self.email_messages.clear()
		self.messages.clear()
		if len(self.user_details) > 0:
			for detail in self.user_details:
				name = detail["name"]
				date = detail["date"]
				amount = detail["amount"]
				message = self.base_message.format(name = name, date = date, total = amount)		
				email = detail.get("email")
				if email:
					user_data = {
						"email": email,
						"message": message
					}
					self.email_messages.append(user_data)
				else:
					self.messages.append(message)
	def get_email_messages(self):
		return self.email_messages
	def get_messages(self):
		return self.messages
	def send_message(self):
		self.make_messages()
		if len(self.email_messages) > 0:			
			for email_message in self.email_messages:
				message = email_message["message"]
				email = email_message["email"]
				try:
					email_connection = SMTP(host, port)
					email_connection.ehlo()
					email_connection.starttls()
					email_connection.login(username, password)
					the_msg = MIMEMultipart("alternative")
					the_msg["Subject"] = "Send email to multiple users"
					the_msg["From"] = username
					the_msg["To"] = email
					content = MIMEText(message, "plain")
					the_msg.attach(content)
					email_connection.sendmail(username, [email], the_msg.as_string())
					email_connection.quit()
				except:
					print("Error sending message")
			return True
		return False

obj = ManageUser()
obj.add_user(name = "KienMN", amount = 189, email = "kienmn99@gmail.com")
obj.add_user(name = "MNKien", amount = 180, email = "kienmn99@gmail.com")
obj.add_user(name = "KMaiNgoc", amount = 199, email = "kienmn99@gmail.com")
obj.make_messages()
obj.get_email_messages()
obj.get_messages()

obj.send_message()
