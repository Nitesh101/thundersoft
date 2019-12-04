import pandas as pd
df = pd.read_csv('pokemon_data4.csv',skipinitialspace=True)
#print df[['Name','Type 1','HP']]
#print(df.head(4))
#print df.iloc[1:4]
#print df.iloc[2,1]
#for index,row in df.iterrows():
#	print index,row['Name']
#print df.loc[df['Type 1'] == "Grass"]
#print df.describe()
#print df.sort_values(['Type 1','HP'],ascending=[0,1])
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print df.head(5)
