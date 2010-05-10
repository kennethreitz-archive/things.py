#!/usr/bin/env python
# encoding: utf-8

""" things.py -- Things.app interface for python
"""

from opster import command

dbPath = '~/Library/Application\ Support/Cultured\ Code/Things/Database.xml'

class db():
	"""Things Database Object"""
	def __init__(self, dbPath):
		self.dbPath = dbPath
		# self. = _parse_db
	
	def _parse_db(self, ):
		pass

class task():
	"""Things.app Task Object"""
	def __init__(self, **kwargs):
		self.kwargs = kwargs
		self.label = ''
		self.due = False
		self.tags = []
		self.project = False
		# self.
		
	def __repr__(self):
		
		tags = "({0}) ".format(', '.join(self.tags)) if len(tags) else ''
		
		
		return '{0} {1}{2}'.format(self.label, tags, self.project)
		


@command(usage='[options] today|next|inbox|logbook|trash')
def main(
		# options,
		mode):
		# database=('d', False, 'Use the specified Things database')
		# completed=('c', False, 'Shows only completed tasks'),
		# all=('a', False, 'Shows all tasks in the focus'),
		# help=('h', False,'Shows this help message'),
		# version=('v', False, 'Shows version')):
		
	"""things.py -- Things.app interface for python"""
	
	# if not database: database = dbPath
	database = dbPath
	
	print locals()
	print 'hello'

if __name__ == '__main__':
	main()
	
	
	
	
	
	