class LinqList():
    def __init__(self, array: list):
        self.array = array

    def FilterByValues(self, values_to_search: list, apply: bool = False):
        if (apply):
            self.array = FilterByValues(self.array, values_to_search)
            return self.array
        return FilterByValues(self.array, values_to_search)
    
    def FilterValuesToRemove(self, values_to_search: list, apply: bool = False):
        if (apply):
            self.array = FilterValuesToRemove(self.array, values_to_search)
            return self.array
        return FilterValuesToRemove(self.array, values_to_search)
    
    def AllIn(self, ) => bool:


def FilterByValues(ValuesList, ValuesToSearch):
    return [i for i in ValuesList if i in ValuesToSearch]

def FilterValuesToRemove(ValuesList, ValuesToSearch):
    return [i for i in ValuesList if i not in ValuesToSearch]

def AllIn(ValuesList, ValuesToSearch):
    return len(SearchValuesInList(ValuesList, ValuesToSearch)) == len(ValuesList)

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