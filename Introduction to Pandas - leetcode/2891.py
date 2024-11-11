import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    fillter_lst = animals[animals['weight']>100]
    sorted_lst = fillter_lst.sort_values('weight',ascending = False)
    return pd.DataFrame(sorted_lst['name'])