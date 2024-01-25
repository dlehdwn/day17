import pandas as pd

data = {
    'age':[30,40,50,60,70],
    'name':['a','b','c','d','e']
}
df = pd.DataFrame(data)
print(df)
print(df.shape) # 행과 열의 수를 돌려줌
print(df.index) # 행
print(df.columns) # 열
print(df.values) # 데이터
print(df['age','name']) # 해당 열 뽑기
print(df[df['age']>30]) # 해당 열 뽑기[조건]
print(df[df['gender']=='f'][df['age']==40])
print(df.loc[0,'name']) # 행 뽑기


