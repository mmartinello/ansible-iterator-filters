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
            'in_list_multilist': self.in_list_multilist,
            'in_list_multidict': self.in_list_multidict,
            'string_in_dict_multilist': self.string_in_dict_multilist,
            'list_in_dict_multilist': self.list_in_dict_multilist
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
        """Checks if a given string is into the given dictionary.
        The function can compare key or values of the dictionary, based on the
        given type of comparison.

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
        type = type.lower()
        for key, value in dictionary.items():
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

    def in_list_multidict(self, string, dictionaries, type="values"):
        """Checks if a given string is into one of the dictionaries included
        into the given list.
        The function can compare key or values of the dictionaries, based on
        the given type of comparison.

        Args:
            string(str): the string to look for.
            dictionaries(list): the list of dictionaries in which the string
                should be searched.
            type(str): define if the given string should be searched into keys
                or values of the given dictionary (possible values:
                'keys|values', default 'values')

        Returns:
            True if the string is found, False otherwise.
        """
        for dictionary in dictionaries:
            if self.in_dict(string, dictionary, type):
                return True
        return False

    def string_in_dict_multilist(self, string, dictionary, type="values"):
        """Checks if a given value is into one of the lists included
        into the given dictionary.
        The function can compare key or values of the dictionary, based on
        the given type of comparison.

        Args:
            string(str): the string to look for.
            dictionary(dict): the dictionary of lists in which the string
                should be searched.
            type(str): define if the given string should be searched into keys
                or values of the given dictionary (possible values:
                'keys|values', default 'values')

        Returns:
            True if the string is found, False otherwise.
        """
        type = type.lower()

        for key, list in dictionary.items():
            if type == "keys":
                if string == key:
                    return True
            else:
                if self.in_list(string, list):
                    return True
        return False

    def list_in_dict_multilist(self, list, dictionary, type="values"):
        """Checks if at least one element of the given list is into one of the
        lists included into the given dictionary.
        The function can compare key or values of the dictionary, based on
        the given type of comparison.

        Args:
            list(list): the list of strings to look for.
            dictionary(dict): the dictionary of lists in which the strings
                should be searched.
            type(str): define if the given string should be searched into keys
                or values of the given dictionary (possible values:
                'keys|values', default 'values')

        Returns:
            True if at least one string is found, False otherwise.
        """
        type = type.lower()

        for string in list:
            if self.string_in_dict_multilist(string, dictionary, type):
                return True

        return False
