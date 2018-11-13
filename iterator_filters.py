# This filter plugin will search a given value into every subkey of a given list
class FilterModule(object):
    def filters(self):
        return {
            'in_list': self.in_list,
        }
    def in_list(self, needle, haystack):
        if isinstance(haystack, str):
            haystack = [haystack]
    
        found = False
        for k, v in haystack.items():
            if any(x in needle for x in v):
                found = True
        return found
