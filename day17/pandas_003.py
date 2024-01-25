import pandas as pd

df = pd.read_csv('bycycle.csv',encoding='cp949')
startList = df['시작 대여소명'].tolist()
placs ={}
for i in startList:
    dong = i.split('_')[0]
    if dong in places:
        places[dong]+=1
    else:
        places[dong]=1
print(df)
