import requests

twilio_number = "+18573424671"
number_to_text = "+18082013589"	# another twilio numbers 

username = "ACbfef22ec578cc7eced21d1864d11ccfa"
accountsid = username
password = "b84a28eaeb311482d745239bb4727080"

message_body = "Hi there, this is my message sent by Twilio"

def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

base_url = "https://api.twilio.com/2010-04-01/Accounts/"
auth_cred = (username, password)

url = base_url + accountsid + "/Messages"

post_data = {
	'From': twilio_number,
	'To': number_to_text,
	'Body': message_body
}

r = requests.post(url, data = post_data, auth = auth_cred)
print(r.status_code)
xml_pretty(r.text)