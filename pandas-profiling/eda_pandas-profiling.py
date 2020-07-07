import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from sklearn.datasets import load_diabetes
diab_data=load_diabetes()
df=pd.DataFrame(data=diab_data.data,columns=diab_data.feature_names)
print(df.head())

profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file("output.html")