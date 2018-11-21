"""iterator_filters.py
Ansible custom filter to check if a given value is present into a given list
of object.

Filters are available to check if the value is present in different type of
given objects:
- a single list
- a single dictionary
- a list containing multiple lists
- a list containing multiple dictionaries
- a dictionary containing multiple lists
- a dictionary containing multiple dictionaries
"""


class FilterModule(object):
    def filters(self):
        """Dictionary with the list of filters which can be used from Ansible.

        The dictionary must contain a list of filters in the form of:
        'filter_name': function to execute

        Example:
            Declare a filter named "foo_filter" which executed the
            self.bar_function function:

                return {
                    'foo_filter': self.bar_function,
                }
        """
        return {
            'in_list': self.in_list,
        }

    def in_list(self, string, list):
        """Checks if a given string is into one of the value of the given list.

        Args:
            string(str): the string to look for.
            list(list): the list in which the string should be searched.

        Returns:
            True if the string is included in at least one of the list's
                values, False otherwise.
        """
        return string in list

    def in_dict(self, string, dictionary):
        """Checks if a given string is into one of the value of the given list.

        Args:
            string(str): the string to look for.
            dictionary(dict): the dictionary in which the string should be
                searched.

        Returns:
            True if the string is included in at least one of the dictionary's
                values, False otherwise.
        """
        for key, value in dictionary.items():
            if string == value:
                return True
        return False
