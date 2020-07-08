import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from sklearn.datasets import load_breast_cancer
breast_cancer_data=load_breast_cancer()
df=pd.DataFrame(data=breast_cancer_data.data,columns=breast_cancer_data.feature_names)
print(df.head())

profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)
profile.to_file("output.html")