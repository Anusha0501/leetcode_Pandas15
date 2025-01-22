#2890. Reshape Data: Melt

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=["product"], value_vars=report.columns[1:], var_name="quarter", value_name="sales")
    

