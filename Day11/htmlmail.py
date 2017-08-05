from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


try:
	host = "smtp.gmail.com"
	port = 587
	username = "example@gmail.com"
	password = "password"
	from_email = username
	to_list = ["example@gmail.com"]

	email_connection = SMTP(host, port)
	email_connection.ehlo()
	email_connection.starttls()
	email_connection.login(username, password)
	

	the_msg = MIMEMultipart("alternative")
	the_msg['Subject'] = "Email Testing"
	the_msg['From'] = from_email
	the_msg['To'] = to_list[0]

	plain_txt = "This is a greeting message"
	html_txt = """\
	<html>
		<head>
		</head>
		<body>
			<p>Hello,<br/>
				This is a message made by <a href="https://www.google.com">KienMN</a>
			</p>
		</body>
	</html>
	"""

	part_1 = MIMEText(plain_txt, "plain")
	part_2 = MIMEText(html_txt, "html")

	the_msg.attach(part_1)
	the_msg.attach(part_2)

	# print(the_msg.as_string())

	email_connection.sendmail(from_email, to_list, the_msg.as_string())
	email_connection.quit()

except:
	print("Some error occured")
