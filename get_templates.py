import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception("This file %s is not existed!" %(file_path))
	return file_path

def get_file(path):
	file_path = get_template_path(path)
	return open(file_path).read()

def render_context(template_string, context):
	return template_string.format(**context)

file_text_path = 'templates/email_message.txt'
file_html_path = 'templates/email_message.html'

text_message = get_file(file_text_path)
html_message = get_file(file_html_path)
context = {
	"name": "KienMN",
	"date": "10/08/2017",
	"total": 189
}

render_context(text_message, context)
render_context(html_message, context)