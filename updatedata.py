import pandas as pd
import re 
from datetime import datetime, timedelta, date

# df = pd.read_csv("billboardHot100_1999_2019_result.csv")

# df = pd.read_csv("newdata1.csv")

# df['Week']= pd.to_datetime(df['Week'])

# df = df.sort_values(by=['Week','Weekly.rank'],ascending=True)

# df['Explicit'] = df['Explicit'].replace(True, 1).replace(False,0)

# df = df.drop_duplicates(subset=['Week'])

# df = df.drop(columns=['Artist','Date','Genre'])

# df.to_csv("billboard_input.csv", index=False)









df = pd.read_csv("billboard_input.csv")
df['Week']= pd.to_datetime(df['Week'])

print("Before: ")
for i in range(df.shape[0]):
	currWeek = df.iloc[i].Week.to_pydatetime().date()
	if(currWeek.isoweekday() != 1):
		print(currWeek)

for i in range(df.shape[0]):
	currWeek = df.iloc[i].Week.to_pydatetime().date()
	# if(currWeek.isoweekday() != 1):
	offset = currWeek.isoweekday() - 1
	newDate = currWeek - timedelta(days=offset)
	# df.iloc[i]['Week'] = newDate
	df.iloc[i, df.columns.get_loc('Week')] = newDate

print("After: ")
# print(df.iloc[0]['Week'].date())
for i in range(df.shape[0]):
	# currWeek = df.iloc[i].Week.to_pydatetime().date()
	currWeek = df.iloc[i]['Week']
	if(currWeek.isoweekday() != 1):
		print(currWeek)


df.to_csv("billboard_input1.csv", index=False)




# print(df)