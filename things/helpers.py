def get_file(path):
	"""Returns a file as a string"""
	return open(path, 'r').read()
	
def enc(str):
	"""Encodes a string to ascii"""
	return str.encode('ascii', 'ignore')

def dec(str):
	"""Decodes a string to ascii"""
	return str.decode('ascii', 'ignore')