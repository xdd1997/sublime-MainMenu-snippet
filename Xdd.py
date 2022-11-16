import sublime
import sublime_plugin
import datetime
import os

class insert_time(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		selection = view.sel()
		for region in selection:
			view.replace(edit,region,'')
		nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.view.insert(edit, selection[0].begin(), nowStr)
		print(nowStr)


class insert_author(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		selection = view.sel()
		for region in selection:
			view.replace(edit,region,'')

		nowStr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		try:
			Filename = os.path.basename(view.file_name())
		except:
			Filename = ''

		author_info = '# -*- coding: utf-8 -*-\n# @Author    : xdd2026@qq.com\n# @CreateData: {}\n# @Filename  : {}\n# @Purpose   : \n\n'.format(nowStr,Filename)
		self.view.insert(edit, selection[0].begin(), author_info)

class insert_numpy_short_comment(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		selection = view.sel()
		for region in selection:
			view.replace(edit,region,'')

		comment = '''"""
Ex01.

:param int a:explain.
:param int b:explain.
:return int c:explain.

Examples
--------
>>> c = add(a,b)
	5
"""

'''


		self.view.insert(edit, selection[0].begin(), comment)		

class insert_numpy_long_comment(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		selection = view.sel()
		for region in selection:
			view.replace(edit,region,'')

		comment = '''"""
Ex01.

Parameters
----------
a : int
    explain.
b : int, optional
    explain.

Returns
-------
c : ndarray
    explain.
d : ndarray
    explain.

Examples
--------
>>> c = add(a,b)
>>> c
    5
"""

'''

		self.view.insert(edit, selection[0].begin(), comment)		