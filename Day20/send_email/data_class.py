import os
import csv
import datetime
from utils.template import get_template, render_context
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# email configuration
host = "smtp.gmail.com"
port = 587
username = "kienmn99@gmail.com"
password = "gaoblue123"
from_email = username
to_list = ["kienmn99@gmail.com"]

# data file
file_name = "user_data.csv"
file_path = os.path.join(os.path.dirname(__file__), file_name)
fieldnames = ["id", "name", "email", "amount", "date", "sent"]

class UserManager():
	def render_message(seft, user_data):
		file_text_path = 'templates/email_message.txt'
		file_html_path = 'templates/email_message.html'
		plain_txt = get_template(file_text_path)
		html_txt = get_template(file_html_path)
		if isinstance(user_data, dict):
			plain_ = render_context(plain_txt, user_data)
			html_ = render_context(html_txt, user_data)
			return (plain_, html_)
		return (None, None)


	def get_user_data(seft, user_id = None, user_email = None):
		unknown_id = None
		unknown_email = None
		with open(file_path, "r") as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				if user_id is not None:
					if int(row["id"]) == int(user_id):
						return row
					else:
						unknown_id = user_id
				elif user_email is not None:
					if row["email"] == user_email:
						return row
					else:
						unknown_email = user_email
		if unknown_email is not None:
			return "User with email {email} not found".format(email = unknown_email)
		if unknown_id is not None:
			return "User with id {id} not found".format(id = unknown_id)	


	def send_email(self, user_id = None, user_email = None, subject = "Billing update"):
		id_ = int(user_id)
		email_ = user_email
		user = self.get_user_data(user_id = id_, user_email = email_)

		email_ = user.get("email")

		try:
			email_connection = SMTP(host, port)
			email_connection.ehlo()
			email_connection.starttls()
			email_connection.login(username, password)

			the_msg = MIMEMultipart("alternative")
			the_msg['Subject'] = subject
			the_msg['From'] = from_email
			the_msg['To'] = email_

			plain_, html_ = self.render_message(user)
			# print(plain_)
			# print(html_)

			part1 = MIMEText(plain_, "plain")
			part2 = MIMEText(html_, "html")

			the_msg.attach(part1)
			the_msg.attach(part2)

			# print(the_msg.as_string())

			email_connection.sendmail(from_email, [email_], the_msg.as_string())
			email_connection.quit()
			return "Send successfully!"
		except:
			return "Some errors occured!"

