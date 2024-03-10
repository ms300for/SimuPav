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
    
    def all_in(self, values_to_verify: list):
        pass

def filter_by_values(list_to_search: list, values_to_filter: list):
    return [i for i in list_to_search if i in values_to_filter]

def filter_to_remove(list_to_search: list, ValuesToSearch: list):
    return [i for i in list_to_search if i not in ValuesToSearch]

def all_in(value_list: list, list_check: list):
    return len(filter_by_values(list_check, value_list)) == len(list_check)

def AllNotIn(ValuesList, ValuesToSearch):
    return len(SearchValuesNotInList(ValuesList, ValuesToSearch)) == len(ValuesList)

def AllIsTrue(BoolList):
    return AllIn(BoolList, [True])

def AllIsFalse(BoolList):
    return AllIn(BoolList, [False])

def AnyIn(ValuesList, ValuesToSearch):
    return len(SearchValuesInList(ValuesList, ValuesToSearch)) > 0

def AnyNotIn(ValuesList, ValuesToSearch):
    return len(SearchValuesNotInList(ValuesList, ValuesToSearch)) > 0


teste = LinqList([1, 2, 2, 3, 4])
print(teste.FilterListByValues([2, 3]))