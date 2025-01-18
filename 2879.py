#2879. Display the First Three Rows

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(employees.head(3))
    
