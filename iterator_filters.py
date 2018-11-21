"""iterator_filters.py
Ansible custom filter to check if a given value is present into a given list
of object.

Filters are available to check if the value is present in different type of
given objects:
- a single list
- a single dictionary (key or values)
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
            'in_dict': self.in_dict,
            'in_list_multilist': self.in_list_multilist
        }

    def in_list(self, string, list):
        """Checks if a given string is into one of the value of the given list.

        Args:
            string(str): the string to look for.
            list(list): the list in which the string should be searched.

        Returns:
            True if the string is found, False otherwise.
        """
        return string in list

    def in_dict(self, string, dictionary, type="values"):
        """Checks if a given string is into one of the value of the given list.

        Args:
            string(str): the string to look for.
            dictionary(dict): the dictionary in which the string should be
                searched.
            type(str): define if the given string should be searched into keys
                or values of the given dictionary (possible values:
                'keys|values', default 'values')

        Returns:
            True if the string is found, False otherwise.
        """
        for key, value in dictionary.items():
            type = type.lower()
            if type == "keys":
                compare = key
            else:
                compare = value

            if string == compare:
                return True
        return False

    def in_list_multilist(self, string, lists):
        """Checks if a given string is into one of the value of one of the
        lists present into the given list of lists.

        Args:
            string(str): the string to look for.
            lists(list): the list of lists in which the string should be
                searched.

        Returns:
            True if the string is found, False otherwise.
        """
        for list in lists:
            if self.in_list(string, list):
                return True
        return False
