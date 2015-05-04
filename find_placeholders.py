import re

def find_placeholders_in_format_string(format_string):
	"""
	Find inside a C-style format string, all the the placeholders for parameters
	i.e. for "Worker name is %s and id is %d" will return the indexes and the placeholders:
	[(15, "%s"), (28, "%d")]
	"""

	# According to printf format string specification from Wikipedia, the format is:
	# %[parameter][flags][width][.precision][length]type
	# see http://en.wikipedia.org/wiki/Printf_format_string#Format_placeholders
	PLACEHOLDERS_REGEX = """
	(										# Capture everything in group 1
	%										# Look for a literal '%'
	(?:
	(?:\d+\$)?								# Look for an optional paramter - number and then '$'
	[-+ 0#]{0,5}							# 0 to 5 optional flags
	(?:\d+|\*)?								# Optional width
	(?:\.(?:\d+|\*))?						# Optional precision
	(?:hh|h|l|ll|L|z|j|t|q|I|I32|I64|w)?	# Optional length
	[diufFeEgGxXoscqaAn]					# Type
	|										# OR
	%))										# literal "%%"
	"""

	matches = re.finditer(cfmt, format_string, flags=re.X)
	results = []
	for i in matches:
		# Remove all the "%%" found. These are literal "%", not placeholders
		if i.group(0) != "%%":
			results.append((i.start(0), i.group(0)))
	return results