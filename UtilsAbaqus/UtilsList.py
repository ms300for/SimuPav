class LinqList():
    def __init__(self, array: list):
        self.array = array

    def filter_by_values(self, values_to_filter: list, apply: bool = False):
        if (apply):
            self.array = filter_by_values(self.array, values_to_filter)
            return self.array
        return filter_by_values(self.array, values_to_filter)
    
    def filter_to_remove(self, values_to_remove: list, apply: bool = False):
        if (apply):
            self.array = filter_to_remove(self.array, values_to_remove)
            return self.array
        return filter_to_remove(self.array, values_to_remove)
    
    def all_in(self, values_to_verify: list) -> bool:
        return all_in(self.array, values_to_verify)
    
    def all_not_in(self, values_to_verify: list) -> bool:
        return all_not_in(self.array, values_to_verify)
#_______________________________________________________________________________#
    
def filter_by_values(list_to_search: list, values_to_filter: list):
    return [i for i in list_to_search if i in values_to_filter]

def filter_to_remove(list_to_search: list, values_to_remove: list):
    return [i for i in list_to_search if i not in values_to_remove]

def all_in(value_list: list, list_check: list) -> bool:
    return len(filter_by_values(list_check, value_list)) == len(list_check)

def all_not_in(value_list: list, list_check: list) -> bool:
    return len(filter_to_remove(list_check, value_list)) == len(list_check)

def all_is_true(bool_list: list) -> bool:
    return len(bool_list) == len(filter_by_values(bool_list, [True]))

def all_is_false(bool_list: list) -> bool:
    return len(bool_list) == len(filter_by_values(bool_list, [False]))

def any_in(list_to_search: list, values_to_filter: list):
    return len(filter_by_values(list_to_search, values_to_filter)) > 0

def any_not_in(list_to_search: list, values_to_remove: list):
    return len(filter_to_remove(list_to_search, values_to_remove)) > 0
