#!/usr/bin/env python
# encoding: utf-8

""" things.py -- Things.app interface for python
"""

from opster import command

@command(usage='[options] today|next|inbox|logbook|trash')
def main(options,
		mode,
		database=('d', '', 'Use the specified Things database'),
		completed=('c', False, 'Shows only completed tasks'),
		all=('a', False, 'Shows all tasks in the focus'),
		help=('h', False,'Shows this help message'),
		version=('v', False, 'Shows version')):
	"""things.py -- Things.app interface for python"""
	return 0




if __name__ == '__main__':
	main()