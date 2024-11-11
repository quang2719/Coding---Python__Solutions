import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    new_df = weather.pivot(
        index ='month',
        columns ='city',
        values='temperature')
    return new_df