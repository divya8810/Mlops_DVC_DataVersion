import pandas as pd
import os
# create a sample dataframe
data={"name":['a','b','c'],
      'Age':[12,34,67],
      'city':['kanpur','delhi','mumbai']
      }
df=pd.DataFrame(data)
new_row={'name':'GINI','Age':20,'city':'agra'}
df.loc[len(df.index)]=new_row


data_dir='data'
os.makedirs(data_dir,exist_ok=True)
file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)
print(f"csv file saved to {file_path}")