import numpy as np
import pandas as pd
import datetime
from datetime import datetime, date

dates = pd.date_range('2016-04-01', '2016-04-06')

# print(dates)

temps1 = pd.Series([80, 82, 85, 90, 83, 87], 
                   index=dates)

temps2 = pd.Series([70, 75, 69, 83, 79, 77], index= dates)


temp_diffs = temps1 - temps2

t3 = pd.Series([temps1[0],temps2[0]])
print(t3.mean())
print(t3)

# print(temps1)
# print(temps2)
# print(f'\ttemp_diffs,\n{temp_diffs}')