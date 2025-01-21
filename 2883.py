#2883. Drop Missing Data

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students_cleaned = students.dropna(subset=['name'])
    return students_cleaned
