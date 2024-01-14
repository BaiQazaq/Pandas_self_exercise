import numpy as np
import pandas as pd
import datetime
from datetime import datetime, date

dates = pd.date_range('2016-04-01', '2016-04-06')

# print(dates)

temps1 = pd.Series([80, 82, 85, 90, 83, 87], 
                   index=dates)

temps2 = pd.Series([70, 75, 69, 83, 79, 77], index= dates)

temps_df = pd.DataFrame(
    {"Missoula": temps1, 'Philadelphia': temps2})

#print(temps_df)
print(temps_df.Missoula)
print(temps_df.Missoula[0])
