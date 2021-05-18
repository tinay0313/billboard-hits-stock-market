import pandas as pd
import re 
from datetime import datetime, timedelta, date

def createJoinColumn(df):
    nameArtist = []
    for idx,row in df.iterrows():
        concat = row['Name'].lower() + '_' + row['Artist'].lower()
        nameArtist.append(concat)
    df['Name_Artist'] = nameArtist

def main():
    billboardDf = pd.read_csv("billboardHot100_1999-2019.csv")
    featuresDf = pd.read_csv("songAttributes_1999-2019.csv")

    createJoinColumn(billboardDf)
    billboardDf = billboardDf.drop(columns=['Lyrics','Features','Writing.Credits','Unnamed: 0'])
    print(billboardDf)

    createJoinColumn(featuresDf)
    featuresDf = featuresDf.drop(columns=['Album','Liveness','TimeSignature','Name','Artist','Unnamed: 0'])
    featuresDf = featuresDf.drop_duplicates(subset=['Name_Artist'])
    print(featuresDf)

    mergeDf = pd.merge(billboardDf, featuresDf, on='Name_Artist')
    mergeDf = mergeDf.drop(columns=['Name_Artist'])

    mergeDf['Week']= pd.to_datetime(mergeDf['Week'])

    mergeDf = mergeDf.sort_values(by=['Week','Weekly.rank'],ascending=True)

    #convert string True/False to 1/0
    mergeDf['Explicit'] = mergeDf['Explicit'].replace(True, 1).replace(False,0)

    #keep single top-ranking song for each week
    mergeDf = mergeDf.drop_duplicates(subset=['Week'])

    #remove features that aren't used for model building
    mergeDf = mergeDf.drop(columns=['Artist','Date','Genre'])

    print("Before: ")
    for i in range(mergeDf.shape[0]):
        currWeek = mergeDf.iloc[i].Week.to_pydatetime().date()
        if(currWeek.isoweekday() != 1):
            print(currWeek)

    for i in range(mergeDf.shape[0]):
        currWeek = mergeDf.iloc[i].Week.to_pydatetime().date()
        offset = currWeek.isoweekday() - 1
        newDate = currWeek - timedelta(days=offset)
        mergeDf.iloc[i, mergeDf.columns.get_loc('Week')] = newDate

    print("After: ")
    for i in range(mergeDf.shape[0]):
        currWeek = mergeDf.iloc[i]['Week']
        if(currWeek.isoweekday() != 1):
            print(currWeek)

    mergeDf.to_csv("billboard_input1.csv", index=False)
    print(mergeDf)


if __name__ == "__main__":
    main()
