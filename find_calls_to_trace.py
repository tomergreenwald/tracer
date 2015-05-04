# This file creates a dictionary of strings in the file given, and what hidden strings to repalce them with

import os

import pycparser
from hide_trace_strings import StringHider

class FuncCallVisitor(pycparser.c_ast.NodeVisitor):
	"""
	A visitor that gets a function call node, checks if it's name
	interests us, and calls a given function if it is
	"""
	def __init__(self, funcname, func_to_run):
		self.funcname = funcname
		self.func_to_run = func_to_run

	def visit_FuncCall(self, node):
		if node.name.name == self.funcname:
			if self.func_to_run:
				self.func_to_run(node)
			else:
				print '%s called at %s' % (self.funcname, node.name.coord)

def find_calls_to_function(filename, funcname, func_to_run):
	"""
	call the given function, on all the function calls found in the given c file
	:param filename: The c file to search the funciton calls in
	:param funcname: The function to search the c file for calls to
	:param func_to_run: The function to call with the function call nodes, for handling
	"""
	assert os.path.exists(filename), "Given file doesn't exist - %s" % filename
	ast = pycparser.parse_file(filename, use_cpp=True)
	visitor = FuncCallVisitor(funcname, func_to_run)
	visitor.visit(ast)

if __name__ == "__main__":
	# An example of using this file. notivce in real use-case you'll call find_calls_to_function()
	# numerous times with the same string_hider, to complete a full dictionary
	string_hider = StringHider()
	find_calls_to_function(os.path.join(os.path.dirname(__file__), "c_files", "main.c"), "TRACE", string_hider.hide_trace_call_strings)
	print string_hider.string_map