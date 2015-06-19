from find_placeholders import find_placeholders_in_format_string


class StringHider(object):
    """
    A class that is given calls to a trace function in a C code, and replaces the
    strings with secret strings, while saving a mapping from the previous strings
    to the new ones, for later documenting, so the secret strings can be reversed later
    """

    def __init__(self):
        self.id = 0
        self.string_map = dict()

    def hide_trace_call_strings(self, call_node):
        """
        Get a function calling node, get the string from it (the first call parameter),
        and replace it with an ID, and then all the placeholders in the string
        :param call_node: The calling node to get the strings from
        """
        # The calling children are the function name and the parameters
        children = call_node.children()
        # Get the 2nd child. Identify it because it's type is "args" rather than "name"
        args = [child for child in children if child[0] == "args"][0]
        # Now get the first children of "args", which is the first argument, which is the string
        string_parameter = args[1].children()[0][1]

        # Assert that we've found the string successfully
        assert string_parameter.type == "string"

        # Remove the quotes in the beginning of end of the string
        string_parameter.value = string_parameter.value[1:-1]

        placeholders = find_placeholders_in_format_string(string_parameter.value)

        # Put the id of the string, so it can identified
        new_string = str(self.id)
        self.id += 1

        # Append all the placeholders, and their original order
        for placeholder in placeholders:
            new_string += " "
            new_string += placeholder[1]

        self.string_map[string_parameter.value] = new_string
