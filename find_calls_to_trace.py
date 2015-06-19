# This file creates a dictionary of strings in the file given, and what hidden strings to repalce them with

import os

import pycparser
from hide_trace_strings import StringHider


class FunctionCallVisitor(pycparser.c_ast.NodeVisitor):
    """
    A visitor that gets a function call node, checks if it's name
    interests us, and calls a given function if it is
    """

    def __init__(self, function_name, func_to_run):
        self.function_name = function_name
        self.function_to_run = func_to_run

    def visit_func_call(self, node):
        """
        Check if this is the interesting function name.
        If so - call function_to_run.
        :param node: The node to check and hand to function_to_run if necessary
        """
        if node.name.name == self.function_name:
            if self.function_to_run:
                self.function_to_run(node)
            else:
                print '%s called at %s' % (self.function_name, node.name.coord)


def find_calls_to_function(filename, function_name, function_to_run):
    """
    Call the given function, on all the function calls found in the given c file
    :param filename: The C file to search the function calls in
    :param function_name: The function to search the c file for calls to
    :param function_to_run: The function to call with the function call nodes, for handling
    """
    assert os.path.exists(filename), "Given file %s doesn't exist" % (filename,)
    ast = pycparser.parse_file(filename, use_cpp=True)
    visitor = FunctionCallVisitor(function_name, function_to_run)
    visitor.visit(ast)


if __name__ == "__main__":
    # An example of using this file. Notice: in real use-case you'll call find_calls_to_function()
    # numerous times with the same string_hider, to complete a full dictionary
    string_hider = StringHider()
    find_calls_to_function(
        os.path.join(os.path.dirname(__file__), "c_files", "main.c"), "TRACE", string_hider.hide_trace_call_strings
    )
    print string_hider.string_map
