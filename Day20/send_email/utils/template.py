import os

def get_path(file_path = None):
	path = os.path.join(os.path.dirname(os.path.dirname(__file__)), file_path)
	if not os.path.isfile(path):
		raise Exception("The file %s is not existed" %(path))
	return path

def get_template(file_path = None):
	file_path = get_path(file_path)
	return open(file_path).read()

def render_context(template_string, context):
	return template_string.format(**context)


	
