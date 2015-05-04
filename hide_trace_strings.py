from find_placeholders import find_placeholders_in_format_string


class StringHider(object):
    """
    A class that is given calls to a trace function in a c code, and replaces the
    strings with secret strings,w hile returning a mapping from the previous strings
    to the new ones, for later documenting, so the secret strings can be reversed later
    """

    def __init__(self):
        self.id = 0
        self.string_map = dict()

    def hide_trace_call_strings(self, call_node):
        """
        Get a function calling node, get the string from it (the first call parameter),
        and replace it with an id, and then all the placeholders in the string
        """
        # The calling children are the funcname and the parameters
        children = call_node.children()
        # Get the 2nd child. Identify it because it's type is "args" rather than "name"
        args = [child for child in children if child[0] == "args"][0]
        # Now get the first children of "args", which is the first argument, which is the string
        string_paramter = args[1].children()[0][1]

        # Assert that we've found the string successfully
        assert string_paramter.type == "string"

        # Remove the quotes in the beginning of end of the string
        string_paramter.value = string_paramter.value[1:-1]

        placeholders = find_placeholders_in_format_string(string_paramter.value)

        # Put the id of the string, so it can identified
        new_string = str(self.id)
        self.id += 1

        # Append all the placeholders, and their original order
        for placeholder in placeholders:
            new_string += " "
            new_string += placeholder[1]

        self.string_map[string_paramter.value] = new_string