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

    def test_string_in_dict_values(self):
        dict = {
            'key1': "foo",
            'key2': "bar"
        }
        string = "foo"
        self.assertTrue(self.filter.in_dict(string, dict))

    def test_string_not_in_dict_values(self):
        dict = {
            'key1': "foo",
            'key2': "bar"
        }
        string = "baz"
        self.assertFalse(self.filter.in_dict(string, dict, "Values"))

    def test_string_in_dict_keys(self):
        dict = {
            'key1': "foo",
            'key2': "bar"
        }
        string = "key1"
        self.assertTrue(self.filter.in_dict(string, dict, "keys"))

    def test_string_not_in_dict_keys(self):
        dict = {
            'key1': "foo",
            'key2': "bar"
        }
        string = "key3"
        self.assertFalse(self.filter.in_dict(string, dict, "Keys"))

    def test_string_in_list_multilist(self):
        list = [
            ["foo", "bar"],
            ["baz", "qux", "quux"]
        ]
        string = "foo"
        self.assertTrue(self.filter.in_list_multilist(string, list))

    def test_string_not_in_list_multilist(self):
        list = [
            ["foo", "bar"],
            ["baz", "qux", "quux"]
        ]
        string = "corge"
        self.assertFalse(self.filter.in_list_multilist(string, list))

    def test_string_in_list_multidict(self):
        list = [
            {'key1': "foo", 'key2': "bar"},
            {'key3': "baz", 'key4': "qux"}
        ]
        string = "foo"
        self.assertTrue(self.filter.in_list_multidict(string, list))

    def test_string_not_in_list_multidict(self):
        list = [
            {'key1': "foo", 'key2': "bar"},
            {'key3': "baz", 'key4': "qux"}
        ]
        string = "quux"
        self.assertFalse(self.filter.in_list_multidict(string, list))

if __name__ == '__main__':
    unittest.main()
