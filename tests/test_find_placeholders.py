import unittest

import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(SCRIPT_DIR, ".."))

from find_placeholders import find_placeholders_in_format_string

class TestFindPlaceholders(unittest.TestCase):
	def test_placeholders(self):
		str_to_test = """
							Worker name is %s and id is %d
							That is %i%%i
							%c
							Decimal: %d  Justified: %.6d
							%10c%5hc%5C%5lc
							The temp is %.*f
							%ss%lii
							%*.*s | %.3d | %lC | %s%%%02d
					  """

		expected_results = [(23, '%s'), (36, '%d'), (54, '%i'), (67, '%c'), (86, '%d'),	\
						    (101, '%.6d'), (113, '%10c'), (117, '%5hc'), (124, '%5lc'), \
						    (148, '%.*f'), (160, '%s'), (163, '%li'), (175, '%*.*s'), 	\
						    (183, '%.3d'), (196, '%s'), (200, '%02d')]

		func_result = find_placeholders_in_format_string(str_to_test)

		self.assertEqual(func_result, expected_results)

if __name__ == "__main__":
	unittest.main()