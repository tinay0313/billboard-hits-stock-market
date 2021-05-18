import pandas as pd
import re 
from datetime import datetime, timedelta, date



def getSPIndex(time, df):
    temp = df[df.Date.dt.date >=time]
    temp = temp.sort_values(by=['Date'], ascending=True)
    return temp.iloc[0].Close


df = pd.read_csv("billboard_input1.csv")

sp500 = "sp500_1999_2020.csv"
DF_sp500 = pd.read_csv(sp500)

DF_sp500['Date']= pd.to_datetime(DF_sp500['Date'])

resultList = []

for i in range(df.shape[0]):
	currDate = datetime.strptime(df.iloc[i]['Week'], "%Y-%m-%d").date()

	currClose = getSPIndex(currDate, DF_sp500)
	nextClose = getSPIndex(currDate+timedelta(days = 7), DF_sp500)

	label = -1
	if(nextClose - currClose > 0):
		label = 1
	else:
		label = 0

	resultList.append([currDate,label])


resultDF = pd.DataFrame(resultList, columns = ['Week', 'Label'])


resultDF.to_csv("yLabel.csv", index=False)
