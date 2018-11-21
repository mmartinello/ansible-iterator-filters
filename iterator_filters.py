"""iterator_filters.py
Ansible custom filter to check if a given value is present into a given list
of object.

Filters are available to check if the value is present in different type of
given objects:
- a single list
- a list containing multiple lists
- a dictionary containing multiple lists
- a dictionary containing multiple dictionaries
"""


class FilterModule(object):
    def filters(self):
        return {
            'in_list': self.in_list,
        }

    def in_list(self, needle, haystack):
        return needle in haystack

#    def in_dict(self, needle, haystack):
