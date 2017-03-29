import pandas as pd

data_tmp=pd.read_csv('classifications.csv',delimiter=',', index_col=False)
names_df=pd.DataFrame(data=data_tmp['subject_id'].unique(),columns=['subject_id'])
print len(data_tmp)
df=pd.merge(data_tmp,names_df,on='subject_id')

# print df