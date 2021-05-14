import pandas as pd
df = pd.DataFrame({
 'broski': [1,2,3,4,5,6,7,8,9,10],    'result': [1,0,0,1,1,1,0,1,0,1]})
df.to_csv('broski1.csv')
print(df)