from lxml import etree
from helpers import *

dbPath = '/Users/kreitz/Library/Application Support/Cultured Code/Things/Database.xml'

class Tag:
	def __init__(self):
		self.id = None
		self.title = None
		
	def __str__(self):
		return self.title
	
	def __repr__(self):
		return '<tag {0}>'.format(self.id)

def main():
	
	
	db = get_file(dbPath)
	root = etree.ElementTree(etree.XML(db))
	
	tags = []
	
	# object type="TAG" id="z148">
	#         <attribute name="dateused" type="date">259456952.88088399171829223633</attribute>
	#         <attribute name="type" type="int32">0</attribute>
	#         <attribute name="shortcut" type="string">e</attribute>
	#         <attribute name="title" type="string">Errand</attribute>
	#         <attribute name="index" type="int32">3</attribute>
	#         <attribute name="identifier" type="string">CC-Things-Tag-Errand</attribute>
	#         <attribute name="compact" type="bool">0</attribute>
	#         <relationship name="parent" type="1/1" destination="THING"></relationship>
	#         <relationship name="record" type="1/1" destination="RECORD"></relationship>
	#         <relationship name="children" type="0/0" destination="THING" idrefs="z151"></relationship>
	#         <relationship name="notes" type="0/0" destination="NOTE" idrefs="z161 z173 z162 z160 z186"></relationship>
	#     </object>
	for t in root.iterfind("//object[@type='TAG']"):
		tag = Tag()
		tag.id = t.attrib['id']
		tag.title = t.find("attribute[@name='title']").text
		tags.append(tag)
	
	print tags

	# <relationship name="tags" type="0/0" destination="TAG" idrefs="z148"></relationship>
	
	# for c in root.iterfind("//object[@type='TODO']"):
	# 	title = c.find("attribute[@name='title']").text
	# 	tags = 
	# 	


if __name__ == '__main__':
	main()