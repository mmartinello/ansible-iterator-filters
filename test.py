import unittest
from iterator_filters import FilterModule
 
class IteratorFiltersTest(unittest.TestCase):
 
    def setUp(self):
        self.filter = FilterModule()

    def test_string_in_list(self):
        a = ["foo", "bar"]
        self.assertTrue(self.filter.in_list("foo", a))
 
if __name__ == '__main__':
    unittest.main()
