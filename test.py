import unittest
from iterator_filters import FilterModule


class IteratorFiltersTest(unittest.TestCase):

    def setUp(self):
        self.filter = FilterModule()

    def test_string_in_list(self):
        list = ["foo", "bar"]
        string = "foo"
        self.assertTrue(self.filter.in_list(string, list))

    def test_string_not_in_list(self):
        list = ["foo", "bar"]
        string = "baz"
        self.assertFalse(self.filter.in_list(string, list))

    def test_string_in_dict(self):
        dict = {
            'key1': "foo",
            'key2': "bar"
        }
        string = "foo"
        self.assertTrue(self.filter.in_dict(string, dict))

    def test_string_not_in_dict(self):
        dict = {
            'key1': "foo",
            'key2': "bar"
        }
        string = "baz"
        self.assertFalse(self.filter.in_dict(string, dict))

if __name__ == '__main__':
    unittest.main()
