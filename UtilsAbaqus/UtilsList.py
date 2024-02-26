def SearchValuesInList(ValuesList, ValuesToSearch):
    return [i for i in ValuesList if i in ValuesToSearch]

def SearchValuesNotInList(ValuesList, ValuesToSearch):
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