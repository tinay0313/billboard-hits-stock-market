import pandas as pd
import re 
from datetime import datetime, timedelta, date

df = pd.read_csv("billboardHot100_1999_2019_result.csv")

df['Week']= pd.to_datetime(df['Week'])

df = df.sort_values(by=['Week','Weekly.rank'],ascending=True)

#convert string True/False to 1/0
df['Explicit'] = df['Explicit'].replace(True, 1).replace(False,0)

#keep single top-ranking song for each week
df = df.drop_duplicates(subset=['Week'])

#remove features that aren't used for model building
df = df.drop(columns=['Artist','Date','Genre'])

print("Before: ")
for i in range(df.shape[0]):
	currWeek = df.iloc[i].Week.to_pydatetime().date()
	if(currWeek.isoweekday() != 1):
		print(currWeek)

for i in range(df.shape[0]):
	currWeek = df.iloc[i].Week.to_pydatetime().date()
	offset = currWeek.isoweekday() - 1
	newDate = currWeek - timedelta(days=offset)
	df.iloc[i, df.columns.get_loc('Week')] = newDate

print("After: ")
for i in range(df.shape[0]):
	currWeek = df.iloc[i]['Week']
	if(currWeek.isoweekday() != 1):
		print(currWeek)

df.to_csv("billboard_input1.csv", index=False)
