# This filter plugin will search a given value into every subkey of a given list
class FilterModule(object):
    def filters(self):
        return {
            'in_list': self.in_list,
        }

    def in_list(self, needle, haystack):
        if needle in haystack:
            return True
        else:
            return False
